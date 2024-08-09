from qfluentwidgets.components import dialog_box, FolderListDialog
from PySide6.QtWidgets import QWidget
from view.Ui_id_rules_replace import Ui_Form
import logging

# 设置日志配置
logger = logging.getLogger("GlobalLogger")


class IdRulesReplaceInterface(QWidget, Ui_Form):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
