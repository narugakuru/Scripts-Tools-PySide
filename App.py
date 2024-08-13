from PySide6.QtWidgets import QApplication
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QIcon
from qfluentwidgets import SplitFluentWindow, FluentIcon
from utils import config_setup
from view.calculator_interface import CalculatorInterface
from view.id_rules_replace_interface import IdRulesReplaceInterface
from view.db_insert_interface import DBInsertInterface
import logging

# 设置日志配置
logger = logging.getLogger("GlobalLogger")
import sys, os


class MyWindow(SplitFluentWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("IT Tools")
        self.setWindowIcon(QIcon(":/qfluentwidgets/images/logo.png"))
        # self.set_window()
        self.showMaximized()

        self.calculatorInterface = CalculatorInterface()
        self.idRulesReplaceInterface = IdRulesReplaceInterface()
        self.DBInsertInterface = DBInsertInterface()
        self.addSubInterface(
            self.idRulesReplaceInterface, FluentIcon.EDIT, "IdRulesReplace"
        )
        self.addSubInterface(self.calculatorInterface, FluentIcon.ACCEPT, "Calculator")
        self.addSubInterface(self.DBInsertInterface, FluentIcon.ADD_TO, "DBInsert")

    def set_window(self, ratio=1):
        # 获取屏幕大小
        screen = QApplication.primaryScreen()

        screen_rect = screen.availableGeometry()

        # 计算窗口大小为屏幕的一半
        width = int(screen_rect.width() * ratio)
        height = int(screen_rect.height() * ratio)

        # 设置窗口大小
        self.resize(width, height)

        # 计算窗口位置以使其居中
        x = (screen_rect.width() - width) // 2
        y = (screen_rect.height() - height) // 2

        # 设置窗口位置
        self.move(x, y)


if __name__ == "__main__":
    cfg = config_setup.ConfigManager()
    print("配置文件路径：" + cfg.CONFIG_FILE_PATH)
    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.Ceil
    )

    app = QApplication()
    window = MyWindow()
    window.show()
    app.exec()
