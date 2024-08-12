# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calculator.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QSizePolicy,
    QWidget)

from qfluentwidgets import (LineEdit, PushButton)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(410, 526)
        Form.setMaximumSize(QSize(496, 16777215))
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.LineEdit = LineEdit(Form)
        self.LineEdit.setObjectName(u"LineEdit")
        self.LineEdit.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.LineEdit.sizePolicy().hasHeightForWidth())
        self.LineEdit.setSizePolicy(sizePolicy)
        self.LineEdit.setMinimumSize(QSize(0, 50))
        self.LineEdit.setMaximumSize(QSize(16777215, 150))
        self.LineEdit.setCursor(QCursor(Qt.CursorShape.ArrowCursor))

        self.gridLayout_3.addWidget(self.LineEdit, 0, 0, 1, 2)

        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.PushButton_1 = PushButton(Form)
        self.PushButton_1.setObjectName(u"PushButton_1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.PushButton_1.sizePolicy().hasHeightForWidth())
        self.PushButton_1.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.PushButton_1, 0, 0, 1, 1)

        self.PushButton_2 = PushButton(Form)
        self.PushButton_2.setObjectName(u"PushButton_2")
        sizePolicy1.setHeightForWidth(self.PushButton_2.sizePolicy().hasHeightForWidth())
        self.PushButton_2.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.PushButton_2, 0, 1, 1, 1)

        self.PushButton_4 = PushButton(Form)
        self.PushButton_4.setObjectName(u"PushButton_4")
        sizePolicy1.setHeightForWidth(self.PushButton_4.sizePolicy().hasHeightForWidth())
        self.PushButton_4.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.PushButton_4, 1, 0, 1, 1)

        self.PushButton_5 = PushButton(Form)
        self.PushButton_5.setObjectName(u"PushButton_5")
        sizePolicy1.setHeightForWidth(self.PushButton_5.sizePolicy().hasHeightForWidth())
        self.PushButton_5.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.PushButton_5, 1, 1, 1, 1)

        self.PushButton_7 = PushButton(Form)
        self.PushButton_7.setObjectName(u"PushButton_7")
        sizePolicy1.setHeightForWidth(self.PushButton_7.sizePolicy().hasHeightForWidth())
        self.PushButton_7.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.PushButton_7, 2, 0, 1, 1)

        self.PushButton_8 = PushButton(Form)
        self.PushButton_8.setObjectName(u"PushButton_8")
        sizePolicy1.setHeightForWidth(self.PushButton_8.sizePolicy().hasHeightForWidth())
        self.PushButton_8.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.PushButton_8, 2, 1, 1, 1)

        self.PushButton_0 = PushButton(Form)
        self.PushButton_0.setObjectName(u"PushButton_0")
        sizePolicy1.setHeightForWidth(self.PushButton_0.sizePolicy().hasHeightForWidth())
        self.PushButton_0.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.PushButton_0, 3, 0, 1, 1)

        self.PushButton_dot = PushButton(Form)
        self.PushButton_dot.setObjectName(u"PushButton_dot")
        sizePolicy1.setHeightForWidth(self.PushButton_dot.sizePolicy().hasHeightForWidth())
        self.PushButton_dot.setSizePolicy(sizePolicy1)

        self.gridLayout_2.addWidget(self.PushButton_dot, 3, 1, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout_2, 1, 0, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.PushButton_3 = PushButton(Form)
        self.PushButton_3.setObjectName(u"PushButton_3")
        sizePolicy1.setHeightForWidth(self.PushButton_3.sizePolicy().hasHeightForWidth())
        self.PushButton_3.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.PushButton_3, 0, 0, 1, 1)

        self.PushButton_add = PushButton(Form)
        self.PushButton_add.setObjectName(u"PushButton_add")
        sizePolicy1.setHeightForWidth(self.PushButton_add.sizePolicy().hasHeightForWidth())
        self.PushButton_add.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.PushButton_add, 0, 1, 1, 1)

        self.PushButton_6 = PushButton(Form)
        self.PushButton_6.setObjectName(u"PushButton_6")
        sizePolicy1.setHeightForWidth(self.PushButton_6.sizePolicy().hasHeightForWidth())
        self.PushButton_6.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.PushButton_6, 1, 0, 1, 1)

        self.PushButton_sub = PushButton(Form)
        self.PushButton_sub.setObjectName(u"PushButton_sub")
        sizePolicy1.setHeightForWidth(self.PushButton_sub.sizePolicy().hasHeightForWidth())
        self.PushButton_sub.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.PushButton_sub, 1, 1, 1, 1)

        self.PushButton_9 = PushButton(Form)
        self.PushButton_9.setObjectName(u"PushButton_9")
        sizePolicy1.setHeightForWidth(self.PushButton_9.sizePolicy().hasHeightForWidth())
        self.PushButton_9.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.PushButton_9, 2, 0, 1, 1)

        self.PushButton_mul = PushButton(Form)
        self.PushButton_mul.setObjectName(u"PushButton_mul")
        sizePolicy1.setHeightForWidth(self.PushButton_mul.sizePolicy().hasHeightForWidth())
        self.PushButton_mul.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.PushButton_mul, 2, 1, 1, 1)

        self.PushButton_clear = PushButton(Form)
        self.PushButton_clear.setObjectName(u"PushButton_clear")
        sizePolicy1.setHeightForWidth(self.PushButton_clear.sizePolicy().hasHeightForWidth())
        self.PushButton_clear.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.PushButton_clear, 3, 0, 1, 1)

        self.PushButton_div = PushButton(Form)
        self.PushButton_div.setObjectName(u"PushButton_div")
        sizePolicy1.setHeightForWidth(self.PushButton_div.sizePolicy().hasHeightForWidth())
        self.PushButton_div.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.PushButton_div, 3, 1, 1, 1)


        self.gridLayout_3.addLayout(self.gridLayout, 1, 1, 1, 1)

        self.PushButton_enter = PushButton(Form)
        self.PushButton_enter.setObjectName(u"PushButton_enter")
        sizePolicy1.setHeightForWidth(self.PushButton_enter.sizePolicy().hasHeightForWidth())
        self.PushButton_enter.setSizePolicy(sizePolicy1)

        self.gridLayout_3.addWidget(self.PushButton_enter, 2, 0, 1, 2)

        self.PushButton_back = PushButton(Form)
        self.PushButton_back.setObjectName(u"PushButton_back")
        sizePolicy1.setHeightForWidth(self.PushButton_back.sizePolicy().hasHeightForWidth())
        self.PushButton_back.setSizePolicy(sizePolicy1)

        self.gridLayout_3.addWidget(self.PushButton_back, 3, 0, 1, 2)


        self.horizontalLayout.addLayout(self.gridLayout_3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.PushButton_1.setText(QCoreApplication.translate("Form", u"1", None))
        self.PushButton_2.setText(QCoreApplication.translate("Form", u"2", None))
        self.PushButton_4.setText(QCoreApplication.translate("Form", u"4", None))
        self.PushButton_5.setText(QCoreApplication.translate("Form", u"5", None))
        self.PushButton_7.setText(QCoreApplication.translate("Form", u"7", None))
        self.PushButton_8.setText(QCoreApplication.translate("Form", u"8", None))
        self.PushButton_0.setText(QCoreApplication.translate("Form", u"0", None))
        self.PushButton_dot.setText(QCoreApplication.translate("Form", u".", None))
        self.PushButton_3.setText(QCoreApplication.translate("Form", u"3", None))
        self.PushButton_add.setText(QCoreApplication.translate("Form", u"+", None))
        self.PushButton_6.setText(QCoreApplication.translate("Form", u"6", None))
        self.PushButton_sub.setText(QCoreApplication.translate("Form", u"-", None))
        self.PushButton_9.setText(QCoreApplication.translate("Form", u"9", None))
        self.PushButton_mul.setText(QCoreApplication.translate("Form", u"*", None))
        self.PushButton_clear.setText(QCoreApplication.translate("Form", u"Clear", None))
        self.PushButton_div.setText(QCoreApplication.translate("Form", u"/", None))
        self.PushButton_enter.setText(QCoreApplication.translate("Form", u"Calculate", None))
        self.PushButton_back.setText(QCoreApplication.translate("Form", u"back", None))
    # retranslateUi

