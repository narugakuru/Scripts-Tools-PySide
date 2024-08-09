# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'id_rules_replace.ui'
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

from qfluentwidgets import (LineEdit, PushButton, TextEdit)

class Ui_Id_Replace(object):
    def setupUi(self, Id_Replace):
        if not Id_Replace.objectName():
            Id_Replace.setObjectName(u"Id_Replace")
        Id_Replace.resize(459, 393)
        self.verticalLayout_2 = QVBoxLayout(Id_Replace)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer = QSpacerItem(5, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.TextEdit_Rules = TextEdit(Id_Replace)
        self.TextEdit_Rules.setObjectName(u"TextEdit_Rules")

        self.verticalLayout.addWidget(self.TextEdit_Rules)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.LineEdit_Path = LineEdit(Id_Replace)
        self.LineEdit_Path.setObjectName(u"LineEdit_Path")

        self.horizontalLayout.addWidget(self.LineEdit_Path)

        self.PushButton_Select = PushButton(Id_Replace)
        self.PushButton_Select.setObjectName(u"PushButton_Select")

        self.horizontalLayout.addWidget(self.PushButton_Select)

        self.PushButton_Replace = PushButton(Id_Replace)
        self.PushButton_Replace.setObjectName(u"PushButton_Replace")

        self.horizontalLayout.addWidget(self.PushButton_Replace)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Id_Replace)

        QMetaObject.connectSlotsByName(Id_Replace)
    # setupUi

    def retranslateUi(self, Id_Replace):
        Id_Replace.setWindowTitle(QCoreApplication.translate("Id_Replace", u"Form", None))
        self.PushButton_Select.setText(QCoreApplication.translate("Id_Replace", u"\u9009\u62e9\u6587\u4ef6\u5939", None))
        self.PushButton_Replace.setText(QCoreApplication.translate("Id_Replace", u"\u66ff\u6362", None))
    # retranslateUi

