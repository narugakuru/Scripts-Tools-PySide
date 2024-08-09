from json import load
from turtle import up
from venv import logger
from utils.logger_setup import get_logs
from utils import config
from PySide6.QtWidgets import QWidget, QFileDialog
from view.Ui_id_rules_replace import Ui_Id_Replace
from qfluentwidgets.components import FolderListDialog
from utils.all_rule_replace import CSVProcessor
from utils.config import load_config, load_json_config, update_yaml
import logging

# 设置日志配置
logger = logging.getLogger("GlobalLogger")


class IdRulesReplaceInterface(QWidget, Ui_Id_Replace):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        cfg = load_config()
        self.csvProcessor = CSVProcessor()
        self.PushButton_Select.clicked.connect(self.show_fileDialog)
        self.LineEdit_Path.setText(cfg["work_path"])
        self.PushButton_Replace.clicked.connect(self.csv_replace)
        self.TextEdit_Rules.setText(load_json_config())

    def csv_replace(self):
        path = self.LineEdit_Path.text().strip()
        logger.info("替换路径：" + path)
        self.csvProcessor.process_csv(path)
        update_yaml("work_path", path)
        print(get_logs())

    def show_fileDialog(self):
        folder_path = QFileDialog.getExistingDirectory(self, "选择文件夹", "")
        if folder_path:
            self.LineEdit_Path.setText(folder_path)
