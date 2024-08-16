# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'id_rules_replace.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

from qfluentwidgets import (LineEdit, PushButton, TableView)

class Ui_Id_Replace(object):
    def setupUi(self, Id_Replace):
        if not Id_Replace.objectName():
            Id_Replace.setObjectName(u"Id_Replace")
        Id_Replace.resize(594, 552)
        self.verticalLayout_3 = QVBoxLayout(Id_Replace)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalSpacer = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.TableView_start = TableView(Id_Replace)
        self.TableView_start.setObjectName(u"TableView_start")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.TableView_start.sizePolicy().hasHeightForWidth())
        self.TableView_start.setSizePolicy(sizePolicy)
        self.TableView_start.setFrameShadow(QFrame.Sunken)
        self.TableView_start.setLineWidth(3)
        self.TableView_start.setMidLineWidth(3)
        self.TableView_start.setDragEnabled(True)
        self.TableView_start.horizontalHeader().setCascadingSectionResizes(True)
        self.TableView_start.horizontalHeader().setMinimumSectionSize(40)

        self.verticalLayout.addWidget(self.TableView_start)

        self.TableView_cyclic = TableView(Id_Replace)
        self.TableView_cyclic.setObjectName(u"TableView_cyclic")
        sizePolicy.setHeightForWidth(self.TableView_cyclic.sizePolicy().hasHeightForWidth())
        self.TableView_cyclic.setSizePolicy(sizePolicy)
        self.TableView_cyclic.setFrameShadow(QFrame.Sunken)
        self.TableView_cyclic.setLineWidth(3)
        self.TableView_cyclic.setMidLineWidth(3)
        self.TableView_cyclic.setDragEnabled(True)
        self.TableView_cyclic.verticalHeader().setMinimumSectionSize(30)

        self.verticalLayout.addWidget(self.TableView_cyclic)

        self.PushButton_Add = PushButton(Id_Replace)
        self.PushButton_Add.setObjectName(u"PushButton_Add")

        self.verticalLayout.addWidget(self.PushButton_Add)


        self.verticalLayout_2.addLayout(self.verticalLayout)

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


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.verticalLayout_3.addLayout(self.verticalLayout_2)


        self.retranslateUi(Id_Replace)

        QMetaObject.connectSlotsByName(Id_Replace)
    # setupUi

    def retranslateUi(self, Id_Replace):
        Id_Replace.setWindowTitle(QCoreApplication.translate("Id_Replace", u"Form", None))
        self.PushButton_Add.setText(QCoreApplication.translate("Id_Replace", u"\u65b0\u589e\u6570\u636e", None))
        self.PushButton_Select.setText(QCoreApplication.translate("Id_Replace", u"\u9009\u62e9\u6587\u4ef6\u5939", None))
        self.PushButton_Replace.setText(QCoreApplication.translate("Id_Replace", u"\u66ff\u6362", None))
    # retranslateUi

