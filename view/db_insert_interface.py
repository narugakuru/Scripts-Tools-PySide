from PySide6.QtWidgets import QWidget, QFileDialog
from utils.config_setup import ConfigManager
from view.Ui_db_insert import Ui_DB_Insert
from utils.db_insertor import CSVtoPostgresInserter
from utils.logger_setup import get_clear_logs
import logging
import utils.logger_setup as log
from PySide6.QtWidgets import QWidget
from PySide6.QtSql import QSqlDatabase, QSqlRelationalTableModel, QSqlRelation
import sys, os
from concurrent.futures import ThreadPoolExecutor

# 设置日志配置
logger = logging.getLogger("GlobalLogger")


class DBInsertInterface(QWidget, Ui_DB_Insert):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        config = ConfigManager()
        self.csv_path = config.config_data["work_path"]
        self.LineEdit_Path.setText(self.csv_path)
        self.PushButton_Select.clicked.connect(self.show_fileDialog)
        self.PushButton_Excu.clicked.connect(self.start_insertion)
        # self.DBInsertor = CSVtoPostgresInserter()
        self.executor = ThreadPoolExecutor(max_workers=1)
        self.TextEdit_Log.append(self.get_files_in_directory())

    def show_fileDialog(self):
        self.csv_path = QFileDialog.getExistingDirectory(self, "选择文件夹", "")
        if self.csv_path:
            self.LineEdit_Path.setText(self.csv_path)

    def start_insertion(self):
        self.csv_path = self.LineEdit_Path.text()
        if self.csv_path:
            self.TextEdit_Log.append("Starting insertion...")
            # 异步执行数据库插入任务
            self.future = self.executor.submit(self.insert_data)
            self.future.add_done_callback(self.handle_result)

    def insert_data(self):
        DBInsertor = CSVtoPostgresInserter()
        # 提交任务并获取 Future 对象
        logger.info("CSV执行路径:" + self.csv_path)
        return DBInsertor.replace_csv_insert2db(self.csv_path)

    def handle_result(self, future):
        try:
            result = future.result()  # 获取返回值
            if result:
                self.TextEdit_Log.append(get_clear_logs())
                self.TextEdit_Log.append("数据插入结束")
            else:
                self.TextEdit_Log.append("Data insertion failed.")
        except Exception as e:
            self.TextEdit_Log.append(f"Task failed with exception: {str(e)}")

    def get_files_in_directory(self):
        # 获取路径下的所有文件和文件夹
        all_entries = os.listdir(self.csv_path)
        # 过滤掉文件夹，只保留文件
        files = [
            entry
            for entry in all_entries
            if os.path.isfile(os.path.join(self.csv_path, entry))
        ]
        # 将文件列表转换为字符串，每个文件名一行
        return "当前文件下的csv文件 \n".join(files)
