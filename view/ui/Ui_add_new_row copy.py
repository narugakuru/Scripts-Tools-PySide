# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_new_row copy.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QHBoxLayout, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

from qfluentwidgets import (BodyLabel, ComboBox, LineEdit)

class Ui_Dialog_AddNewRow(object):
    def setupUi(self, Dialog_AddNewRow):
        if not Dialog_AddNewRow.objectName():
            Dialog_AddNewRow.setObjectName(u"Dialog_AddNewRow")
        Dialog_AddNewRow.resize(400, 300)
        self.verticalLayout_5 = QVBoxLayout(Dialog_AddNewRow)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.BodyLabel = BodyLabel(Dialog_AddNewRow)
        self.BodyLabel.setObjectName(u"BodyLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.BodyLabel.sizePolicy().hasHeightForWidth())
        self.BodyLabel.setSizePolicy(sizePolicy)
        self.BodyLabel.setMinimumSize(QSize(0, 20))
        self.BodyLabel.setMaximumSize(QSize(100, 30))
        self.BodyLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.BodyLabel)

        self.LineEdit = LineEdit(Dialog_AddNewRow)
        self.LineEdit.setObjectName(u"LineEdit")

        self.verticalLayout.addWidget(self.LineEdit)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.BodyLabel_2 = BodyLabel(Dialog_AddNewRow)
        self.BodyLabel_2.setObjectName(u"BodyLabel_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.BodyLabel_2.sizePolicy().hasHeightForWidth())
        self.BodyLabel_2.setSizePolicy(sizePolicy1)
        self.BodyLabel_2.setMinimumSize(QSize(0, 10))
        self.BodyLabel_2.setMaximumSize(QSize(100, 30))
        self.BodyLabel_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.BodyLabel_2)

        self.LineEdit_2 = LineEdit(Dialog_AddNewRow)
        self.LineEdit_2.setObjectName(u"LineEdit_2")

        self.verticalLayout_2.addWidget(self.LineEdit_2)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.BodyLabel_3 = BodyLabel(Dialog_AddNewRow)
        self.BodyLabel_3.setObjectName(u"BodyLabel_3")
        sizePolicy.setHeightForWidth(self.BodyLabel_3.sizePolicy().hasHeightForWidth())
        self.BodyLabel_3.setSizePolicy(sizePolicy)
        self.BodyLabel_3.setMinimumSize(QSize(0, 20))
        self.BodyLabel_3.setMaximumSize(QSize(100, 30))
        self.BodyLabel_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.BodyLabel_3)

        self.LineEdit_3 = LineEdit(Dialog_AddNewRow)
        self.LineEdit_3.setObjectName(u"LineEdit_3")

        self.verticalLayout_3.addWidget(self.LineEdit_3)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.BodyLabel_4 = BodyLabel(Dialog_AddNewRow)
        self.BodyLabel_4.setObjectName(u"BodyLabel_4")
        sizePolicy.setHeightForWidth(self.BodyLabel_4.sizePolicy().hasHeightForWidth())
        self.BodyLabel_4.setSizePolicy(sizePolicy)
        self.BodyLabel_4.setMinimumSize(QSize(0, 20))
        self.BodyLabel_4.setMaximumSize(QSize(100, 30))
        self.BodyLabel_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.BodyLabel_4)

        self.ComboBox = ComboBox(Dialog_AddNewRow)
        self.ComboBox.setObjectName(u"ComboBox")

        self.verticalLayout_4.addWidget(self.ComboBox)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)


        self.verticalLayout_5.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.buttonBox = QDialogButtonBox(Dialog_AddNewRow)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.horizontalLayout.addWidget(self.buttonBox)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_5.addLayout(self.horizontalLayout)


        self.retranslateUi(Dialog_AddNewRow)
        self.buttonBox.accepted.connect(Dialog_AddNewRow.accept)
        self.buttonBox.rejected.connect(Dialog_AddNewRow.reject)

        QMetaObject.connectSlotsByName(Dialog_AddNewRow)
    # setupUi

    def retranslateUi(self, Dialog_AddNewRow):
        Dialog_AddNewRow.setWindowTitle(QCoreApplication.translate("Dialog_AddNewRow", u"Dialog", None))
        self.BodyLabel.setText(QCoreApplication.translate("Dialog_AddNewRow", u"id", None))
        self.BodyLabel_2.setText(QCoreApplication.translate("Dialog_AddNewRow", u"rule", None))
        self.BodyLabel_3.setText(QCoreApplication.translate("Dialog_AddNewRow", u"comments", None))
        self.BodyLabel_4.setText(QCoreApplication.translate("Dialog_AddNewRow", u"table", None))
    # retranslateUi

