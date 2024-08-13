import os  # 导入操作系统模块，用于与操作系统进行交互
import pandas as pd  # 导入 pandas 库，用于数据处理和分析
import re  # 导入正则表达式模块，用于字符串匹配和处理
import logging  # 导入日志模块，用于记录程序运行信息
from datetime import datetime  # 从 datetime 模块导入 datetime 类，用于处理日期和时间
from peewee import Model, CharField, PostgresqlDatabase  # 从 peewee ORM 导入模型相关类
from playhouse.shortcuts import (
    model_to_dict,
)  # 从 playhouse 中导入 model_to_dict 函数，用于将模型实例转换为字典
from utils.all_rule_replace import (
    CSVProcessor,
)  # 从 utils 模块导入 CSVProcessor 类，用于处理 CSV 文件
from utils.configManager import (
    load_config,
)  # 从 utils 模块导入 load_config 函数，用于加载配置文件

# 设置日志配置
logger = logging.getLogger("GlobalLogger")  # 创建全局日志记录器

from peewee import PostgresqlDatabase  # 再次导入 PostgresqlDatabase，可能是为了确保使用
from urllib.parse import urlparse  # 从 urllib.parse 导入 urlparse 函数，用于解析 URL


# 解析数据库 URL
def parse_db_url(db_url):
    parsed_url = urlparse(db_url)  # 解析数据库 URL
    return {
        "database": parsed_url.path[1:],  # 获取数据库名，去掉开头的 '/'
        "user": parsed_url.username,  # 获取数据库用户名
        "password": parsed_url.password,  # 获取数据库密码
        "host": parsed_url.hostname,  # 获取数据库主机名
        "port": parsed_url.port,  # 获取数据库端口
    }


# 数据库 URL
db_url = "postgresql+psycopg2://postgres:rootroot@localhost:5432/postgres?options=-csearch_path=takusai_tanntai"

# 使用 URL 连接数据库
db_config = parse_db_url(db_url)  # 解析数据库配置
db = PostgresqlDatabase(  # 创建 PostgresqlDatabase 实例
    database=db_config["database"],  # 数据库名
    user=db_config["user"],  # 用户名
    password=db_config["password"],  # 密码
    host=db_config["host"],  # 主机名
    port=db_config["port"],  # 端口
)


class BaseModel(Model):  # 定义基础模型类，所有模型都会继承这个类
    class Meta:  # Meta 类用于配置模型的元数据
        database = db  # 指定使用的数据库


class CSVtoPostgresInserter:  # 定义 CSVtoPostgresInserter 类，用于处理 CSV 文件并插入到数据库
    def __init__(self, id_replace=True):  # 初始化方法，默认 id_replace 为 True
        self.csv_folder = None  # 初始化 CSV 文件夹路径为 None
        self.id_replace = id_replace  # 保存 id_replace 属性
        logger.info("CSVtoPostgresInserter 初始化成功.")  # 记录初始化成功的日志

    def filter_latest_csv_files(self):  # 过滤最新的 CSV 文件
        latest_files = {}  # 存储最新文件的字典
        pattern = re.compile(
            r"^(.*?)(?:_(\d{8}\d{4}))?\.csv$"
        )  # 编译正则表达式，用于匹配文件名

        for filename in os.listdir(self.csv_folder):  # 遍历文件夹中的所有文件
            if filename.endswith(".csv"):  # 仅处理以 .csv 结尾的文件
                match = pattern.match(filename)  # 匹配文件名
                if match:  # 如果匹配成功
                    table_name = match.group(1)  # 提取表名
                    date_str = match.group(2)  # 提取日期字符串
                    file_date = (
                        datetime.min  # 如果没有日期字符串，则设置为最小日期
                        if not date_str
                        else datetime.strptime(
                            date_str, "%Y%m%d%H%M"
                        )  # 将日期字符串转换为 datetime 对象
                    )

                    if (
                        table_name not in latest_files  # 如果字典中不存在该表名
                        or latest_files[table_name][1]
                        < file_date  # 或者当前文件日期更晚
                    ):
                        latest_files[table_name] = (filename, file_date)  # 更新最新文件

        return [entry[0] for entry in latest_files.values()]  # 返回最新文件名列表

    def insert_csv_to_postgresql_with_transaction(
        self,
    ):  # 插入 CSV 数据到 PostgreSQL 数据库的事务方法
        try:
            # 过滤文件
            csv_list = self.filter_latest_csv_files()  # 获取最新 CSV 文件列表
            for filename in csv_list:  # 遍历每个文件
                file_path = os.path.join(self.csv_folder, filename)  # 构建文件路径
                df = pd.read_csv(
                    file_path, dtype=str
                )  # 读取 CSV 文件，数据类型设置为字符串
                table_name = re.match(r"^(.*?)(?:_\d{8}\d{4})?\.csv$", filename).group(
                    1
                )  # 获取表名

                with db.transaction():  # 开始数据库事务
                    try:
                        # 检查表是否存在
                        if not db.get_tables().count(table_name):  # 如果表不存在
                            logger.info(
                                f"Table {table_name} does not exist in the database. Skipping {filename}."
                            )  # 记录日志
                            continue  # 跳过此文件

                        # 清空表
                        db.execute_sql(f"DELETE FROM {table_name}")  # 清空表中所有数据

                        # 插入数据
                        df.to_sql(
                            table_name,
                            con=db.connection(),
                            if_exists="append",
                            index=False,
                        )  # 将数据插入表中
                        logger.info(
                            f"Inserted data from {filename} into {table_name} table."
                        )  # 记录成功插入日志
                    except Exception as e:  # 捕获插入过程中的异常
                        logger.info(
                            f"Failed to insert data from {filename} into {table_name} table."
                        )  # 记录错误日志
                        logger.info(f"Error: {e}")  # 记录具体错误信息
        except Exception as e:  # 捕获事务中的异常
            logger.info(
                f"Transaction failed and was rolled back. Error: {e}"
            )  # 记录事务失败的日志

    def repalce_csv_insert2db(self, csv_path):  # 将 CSV 数据处理并插入数据库的方法
        """输入一个文件夹/文件路径，先对数据做批量处理，再批量插入CSV数据到PostgreSQL数据库"""  # 方法说明
        csvProcessor = CSVProcessor()  # 创建 CSVProcessor 实例
        self.csv_folder = csvProcessor.process_csv(
            csv_path
        )  # 处理 CSV，获取 CSV 文件夹路径
        logger.info("CSV数据处理完成,开始连接数据库")  # 记录数据处理完成的日志
        try:
            self.insert_csv_to_postgresql_with_transaction()  # 调用插入方法
            logger.info("数据插入完成")  # 记录数据插入完成的日志
            return True  # 返回成功
        except Exception as e:  # 捕获插入过程中的异常
            logger.info(f"数据插入失败: {e}")  # 记录失败日志
            return False  # 返回失败


def insert_data(csv_path):  # 插入数据的外部函数
    inserter = CSVtoPostgresInserter(True)  # 创建 CSVtoPostgresInserter 实例
    inserter.repalce_csv_insert2db(csv_path)  # 调用数据插入方法


if __name__ == "__main__":  # 程序入口
    csv_path = r"Z:\WorkSpace\NADJ20007"  # CSV 文件夹路径
    insert_data(csv_path)  # 调用插入数据函数
