from calendar import c
from utils.logger_setup import get_clear_logs
from PySide6.QtWidgets import QWidget, QFileDialog
from view.Ui_id_rules_replace import Ui_Id_Replace
from qfluentwidgets.components import (
    Flyout,
    InfoBarIcon,
    FlyoutAnimationType,
    MessageBox,
)
from utils.all_rule_replace import CSVProcessor
from utils.config_setup import ConfigManager
import logging
from PySide6.QtWidgets import QWidget
from PySide6.QtSql import QSqlDatabase
from view.common import bindDB

# 设置日志配置
logger = logging.getLogger("GlobalLogger")


class IdRulesReplaceInterface(QWidget, Ui_Id_Replace):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.log_text = ""
        self.configManager = ConfigManager()
        cfg = self.configManager.config_data
        self.csvProcessor = CSVProcessor()
        self.PushButton_Select.clicked.connect(self.show_fileDialog)
        self.LineEdit_Path.setText(cfg["work_path"])
        self.PushButton_Replace.clicked.connect(self.csv_replace)
        self.create_connection()
        bindDB(self)

    def create_connection(self):
        print("create_connection")
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName(ConfigManager().SQLITE_DB_PATH)
        if not self.db.open():
            print("Unable to open database")
            return False
        print("SQLITE is open")
        return True

    def csv_replace(self):
        path = self.LineEdit_Path.text().strip()
        logger.info("替换路径：" + path)
        self.csvProcessor.process_csv(path)
        self.configManager.update_yaml("work_path", path)
        self.log_text = get_clear_logs()
        print(f"List Handle{self.log_text}")
        self.show_log()

    def msg(self):
        w = MessageBox("执行成功", self.log_text, self)
        w.cancelButton.hide()
        w.buttonLayout.insertStretch(1)
        w.exec()

    def show_log(self):
        Flyout.create(
            icon=InfoBarIcon.SUCCESS,
            title="执行完毕",
            content=str(self.log_text),
            target=self.PushButton_Replace,
            parent=self,
            isClosable=True,
            aniType=FlyoutAnimationType.PULL_UP,
        )

    def show_fileDialog(self):
        folder_path = QFileDialog.getExistingDirectory(self, "选择文件夹", "")
        if folder_path:
            self.LineEdit_Path.setText(folder_path)
