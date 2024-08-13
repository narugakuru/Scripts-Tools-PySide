import os
import pandas as pd
import re
import logging
from datetime import datetime
from peewee import PostgresqlDatabase
from utils.all_rule_replace import CSVProcessor  # 确保这个模块在你的环境中可用
from utils.config_setup import ConfigManager  # 确保这个模块在你的环境中可用

# 设置日志配置
logger = logging.getLogger("GlobalLogger")
logging.basicConfig(level=logging.INFO)

# 定义数据库连接参数
db_url = "postgresql+psycopg2://postgres:rootroot@localhost:5432/postgres?options=-csearch_path=takusai_tanntai"

# 解析数据库 URL
pattern = re.compile(
    r"postgresql\+psycopg2://(?P<user>[^:]+):(?P<password>[^@]+)@(?P<host>[^:]+):(?P<port>\d+)/(?P<database>[^\?]+)\?options=-csearch_path=(?P<schema>[^\&]+)"
)
match = pattern.match(db_url)

if match:
    db_config = match.groupdict()
else:
    raise ValueError("Invalid database URL")

# 创建数据库实例
db = PostgresqlDatabase(
    db_config["database"],
    user=db_config["user"],
    password=db_config["password"],
    host=db_config["host"],
    port=int(db_config["port"]),
    options=f"-c search_path={db_config['schema']}",
)

# 连接数据库
db.connect()


class CSVtoPostgresInserter:
    def __init__(self, id_replace=True):
        self.csv_folder = None
        self.id_replace = id_replace
        logger.info("CSVtoPostgresInserter 初始化成功.")

    def filter_latest_csv_files(self):
        latest_files = {}
        pattern = re.compile(r"^(.*?)(?:_(\d{8}\d{4}))?\.csv$")

        for filename in os.listdir(self.csv_folder):
            if filename.endswith(".csv"):
                match = pattern.match(filename)
                if match:
                    table_name = match.group(1)
                    date_str = match.group(2)
                    file_date = (
                        datetime.min
                        if not date_str
                        else datetime.strptime(date_str, "%Y%m%d%H%M")
                    )

                    if (
                        table_name not in latest_files
                        or latest_files[table_name][1] < file_date
                    ):
                        latest_files[table_name] = (filename, file_date)

        return [entry[0] for entry in latest_files.values()]

    def insert_csv_to_postgresql_with_transaction(self):
        try:
            csv_list = self.filter_latest_csv_files()
            for filename in csv_list:
                file_path = os.path.join(self.csv_folder, filename)
                df = pd.read_csv(file_path, dtype=str)
                table_name = re.match(r"^(.*?)(?:_\d{8}\d{4})?\.csv$", filename).group(
                    1
                )
                schema_name = db_config["schema"]

                with db.atomic():  # 使用原子事务
                    try:
                        # 检查表是否存在
                        if table_name not in db.get_tables(schema=schema_name):
                            logger.info(
                                f"Table {table_name} does not exist in the database. Skipping {filename}."
                            )
                            continue

                        # 清空表
                        db.execute_sql(f"DELETE FROM {schema_name}.{table_name}")

                        # 插入数据
                        for _, row in df.iterrows():
                            columns = ", ".join(row.index)
                            values = ", ".join(
                                [
                                    f"'{x}'" if x is not None else "NULL"
                                    for x in row.values
                                ]
                            )
                            insert_query = f"INSERT INTO {schema_name}.{table_name} ({columns}) VALUES ({values})"
                            db.execute_sql(insert_query)

                        logger.info(
                            f"Inserted data from {filename} into {table_name} table."
                        )
                    except Exception as e:
                        logger.error(
                            f"Failed to insert data from {filename} into {table_name} table."
                        )
                        logger.exception(e)
        except Exception as e:
            logger.error("Transaction failed and was rolled back.")
            logger.exception(e)

    def repalce_csv_insert2db(self, csv_path):
        csvProcessor = CSVProcessor()
        self.csv_folder = csvProcessor.process_csv(csv_path)
        logger.info("CSV数据处理完成,开始连接数据库")
        try:
            self.insert_csv_to_postgresql_with_transaction()
            logger.info("数据插入完成")
            return True
        except Exception as e:
            logger.error(f"数据插入失败: {e}")
            return False


def insert_data(csv_path):
    inserter = CSVtoPostgresInserter(True)
    inserter.repalce_csv_insert2db(csv_path)


if __name__ == "__main__":
    csv_path = r"Z:\WorkSpace\NADJ20007"
    insert_data(csv_path)
