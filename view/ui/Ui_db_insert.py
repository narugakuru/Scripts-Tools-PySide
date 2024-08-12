# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'db_insert.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

from qfluentwidgets import (CheckBox, LineEdit, PushButton, TextEdit)

class Ui_DB_Insert(object):
    def setupUi(self, DB_Insert):
        if not DB_Insert.objectName():
            DB_Insert.setObjectName(u"DB_Insert")
        DB_Insert.resize(400, 295)
        self.horizontalLayout_3 = QHBoxLayout(DB_Insert)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.TextEdit_Log = TextEdit(DB_Insert)
        self.TextEdit_Log.setObjectName(u"TextEdit_Log")

        self.verticalLayout_2.addWidget(self.TextEdit_Log)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.LineEdit_Path = LineEdit(DB_Insert)
        self.LineEdit_Path.setObjectName(u"LineEdit_Path")

        self.horizontalLayout_2.addWidget(self.LineEdit_Path)

        self.PushButton_Select = PushButton(DB_Insert)
        self.PushButton_Select.setObjectName(u"PushButton_Select")

        self.horizontalLayout_2.addWidget(self.PushButton_Select)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.CheckBox = CheckBox(DB_Insert)
        self.CheckBox.setObjectName(u"CheckBox")

        self.horizontalLayout.addWidget(self.CheckBox)

        self.PushButton_Excu = PushButton(DB_Insert)
        self.PushButton_Excu.setObjectName(u"PushButton_Excu")

        self.horizontalLayout.addWidget(self.PushButton_Excu)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)


        self.retranslateUi(DB_Insert)

        QMetaObject.connectSlotsByName(DB_Insert)
    # setupUi

    def retranslateUi(self, DB_Insert):
        DB_Insert.setWindowTitle(QCoreApplication.translate("DB_Insert", u"Form", None))
        self.PushButton_Select.setText(QCoreApplication.translate("DB_Insert", u"\u9009\u62e9\u6587\u4ef6\u5939", None))
        self.CheckBox.setText(QCoreApplication.translate("DB_Insert", u"\u6570\u636e\u66ff\u6362", None))
        self.PushButton_Excu.setText(QCoreApplication.translate("DB_Insert", u"\u63d2\u5165\u6570\u636e", None))
    # retranslateUi

