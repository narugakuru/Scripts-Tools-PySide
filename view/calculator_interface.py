from PySide6.QtWidgets import (
    QWidget,
)
from view.Ui_calculator import Ui_Form
import logging

# 设置日志配置
logger = logging.getLogger("GlobalLogger")


def update_display(func):
    def wrapper(self, *args, **kwargs):
        result = func(self, *args, **kwargs)
        self.LineEdit.setText(self.res)
        return result

    return wrapper


class CalculatorInterface(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.res = " "
        self.bind()

    def bind(self):
        buttons = {
            "0": self.PushButton_0,
            "1": self.PushButton_1,
            "2": self.PushButton_2,
            "3": self.PushButton_3,
            "4": self.PushButton_4,
            "5": self.PushButton_5,
            "6": self.PushButton_6,
            "7": self.PushButton_7,
            "8": self.PushButton_8,
            "9": self.PushButton_9,
            "+": self.PushButton_add,
            "-": self.PushButton_sub,
            "*": self.PushButton_mul,
            "/": self.PushButton_div,
            ".": self.PushButton_dot,
            # "=": self.PushButton_enter,
        }

        for key, button in buttons.items():
            button.clicked.connect(lambda ch, key=key: self.addNumber(key))

        self.PushButton_enter.clicked.connect(self.equal)
        self.PushButton_clear.clicked.connect(self.clear)
        self.PushButton_back.clicked.connect(self.back)

    @update_display
    def addNumber(self, number):
        self.res += number

    @update_display
    def equal(self):
        try:
            if self.res == "":
                return
            self.res = str(eval(self.res))
        except Exception as e:
            self.res = "Error"

    @update_display
    def clear(self):
        self.res = ""

    @update_display
    def back(self):
        self.res = self.res[:-1]
