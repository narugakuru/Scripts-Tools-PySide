# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calculator.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PySide6.QtGui import (
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PySide6.QtWidgets import (
    QApplication,
    QHBoxLayout,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)

from qfluentwidgets import LineEdit, PushButton


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName("Calculator")
        Form.resize(255, 289)
        Form.setMaximumSize(QSize(496, 16777215))
        self.horizontalLayout_5 = QHBoxLayout(Form)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.LineEdit = LineEdit(Form)
        self.LineEdit.setObjectName("LineEdit")
        self.LineEdit.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LineEdit.sizePolicy().hasHeightForWidth())
        self.LineEdit.setSizePolicy(sizePolicy)
        self.LineEdit.setMaximumSize(QSize(16777215, 80))
        self.LineEdit.setCursor(QCursor(Qt.CursorShape.ArrowCursor))

        self.verticalLayout.addWidget(self.LineEdit)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.PushButton_1 = PushButton(Form)
        self.PushButton_1.setObjectName("PushButton_1")

        self.horizontalLayout.addWidget(self.PushButton_1)

        self.PushButton_2 = PushButton(Form)
        self.PushButton_2.setObjectName("PushButton_2")

        self.horizontalLayout.addWidget(self.PushButton_2)

        self.PushButton_3 = PushButton(Form)
        self.PushButton_3.setObjectName("PushButton_3")

        self.horizontalLayout.addWidget(self.PushButton_3)

        self.PushButton_add = PushButton(Form)
        self.PushButton_add.setObjectName("PushButton_add")

        self.horizontalLayout.addWidget(self.PushButton_add)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.PushButton_4 = PushButton(Form)
        self.PushButton_4.setObjectName("PushButton_4")

        self.horizontalLayout_2.addWidget(self.PushButton_4)

        self.PushButton_5 = PushButton(Form)
        self.PushButton_5.setObjectName("PushButton_5")

        self.horizontalLayout_2.addWidget(self.PushButton_5)

        self.PushButton_6 = PushButton(Form)
        self.PushButton_6.setObjectName("PushButton_6")

        self.horizontalLayout_2.addWidget(self.PushButton_6)

        self.PushButton_sub = PushButton(Form)
        self.PushButton_sub.setObjectName("PushButton_sub")

        self.horizontalLayout_2.addWidget(self.PushButton_sub)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.PushButton_7 = PushButton(Form)
        self.PushButton_7.setObjectName("PushButton_7")

        self.horizontalLayout_3.addWidget(self.PushButton_7)

        self.PushButton_8 = PushButton(Form)
        self.PushButton_8.setObjectName("PushButton_8")

        self.horizontalLayout_3.addWidget(self.PushButton_8)

        self.PushButton_9 = PushButton(Form)
        self.PushButton_9.setObjectName("PushButton_9")

        self.horizontalLayout_3.addWidget(self.PushButton_9)

        self.PushButton_mul = PushButton(Form)
        self.PushButton_mul.setObjectName("PushButton_mul")

        self.horizontalLayout_3.addWidget(self.PushButton_mul)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.PushButton_0 = PushButton(Form)
        self.PushButton_0.setObjectName("PushButton_0")

        self.horizontalLayout_4.addWidget(self.PushButton_0)

        self.PushButton_dot = PushButton(Form)
        self.PushButton_dot.setObjectName("PushButton_dot")

        self.horizontalLayout_4.addWidget(self.PushButton_dot)

        self.PushButton_clear = PushButton(Form)
        self.PushButton_clear.setObjectName("PushButton_clear")

        self.horizontalLayout_4.addWidget(self.PushButton_clear)

        self.PushButton_div = PushButton(Form)
        self.PushButton_div.setObjectName("PushButton_div")

        self.horizontalLayout_4.addWidget(self.PushButton_div)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.PushButton_enter = PushButton(Form)
        self.PushButton_enter.setObjectName("PushButton_enter")

        self.verticalLayout.addWidget(self.PushButton_enter)

        self.PushButton_back = PushButton(Form)
        self.PushButton_back.setObjectName("PushButton_back")

        self.verticalLayout.addWidget(self.PushButton_back)

        self.horizontalLayout_5.addLayout(self.verticalLayout)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", "Form", None))
        self.PushButton_1.setText(QCoreApplication.translate("Form", "1", None))
        self.PushButton_2.setText(QCoreApplication.translate("Form", "2", None))
        self.PushButton_3.setText(QCoreApplication.translate("Form", "3", None))
        self.PushButton_add.setText(QCoreApplication.translate("Form", "+", None))
        self.PushButton_4.setText(QCoreApplication.translate("Form", "4", None))
        self.PushButton_5.setText(QCoreApplication.translate("Form", "5", None))
        self.PushButton_6.setText(QCoreApplication.translate("Form", "6", None))
        self.PushButton_sub.setText(QCoreApplication.translate("Form", "-", None))
        self.PushButton_7.setText(QCoreApplication.translate("Form", "7", None))
        self.PushButton_8.setText(QCoreApplication.translate("Form", "8", None))
        self.PushButton_9.setText(QCoreApplication.translate("Form", "9", None))
        self.PushButton_mul.setText(QCoreApplication.translate("Form", "*", None))
        self.PushButton_0.setText(QCoreApplication.translate("Form", "0", None))
        self.PushButton_dot.setText(QCoreApplication.translate("Form", ".", None))
        self.PushButton_clear.setText(QCoreApplication.translate("Form", "Clear", None))
        self.PushButton_div.setText(QCoreApplication.translate("Form", "/", None))
        self.PushButton_enter.setText(
            QCoreApplication.translate("Form", "Calculate", None)
        )
        self.PushButton_back.setText(QCoreApplication.translate("Form", "back", None))

    # retranslateUi
