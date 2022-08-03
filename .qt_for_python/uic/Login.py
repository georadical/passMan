# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Login.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
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
from PySide6.QtWidgets import (QApplication, QDialog, QGridLayout, QLabel,
    QLayout, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(370, 300)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Login.sizePolicy().hasHeightForWidth())
        Login.setSizePolicy(sizePolicy)
        Login.setMinimumSize(QSize(370, 300))
        Login.setMaximumSize(QSize(500, 300))
        Login.setSizeIncrement(QSize(1, 0))
        self.lblLogin = QLabel(Login)
        self.lblLogin.setObjectName(u"lblLogin")
        self.lblLogin.setGeometry(QRect(150, 20, 70, 30))
        self.lblLogin.setMinimumSize(QSize(70, 30))
        self.lblLogin.setMaximumSize(QSize(100, 40))
        font = QFont()
        font.setPointSize(20)
        self.lblLogin.setFont(font)
        self.layoutWidget = QWidget(Login)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 70, 311, 131))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.lblUserName = QLabel(self.layoutWidget)
        self.lblUserName.setObjectName(u"lblUserName")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(2)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lblUserName.sizePolicy().hasHeightForWidth())
        self.lblUserName.setSizePolicy(sizePolicy1)
        self.lblUserName.setMinimumSize(QSize(77, 25))
        self.lblUserName.setMaximumSize(QSize(100, 25))

        self.gridLayout.addWidget(self.lblUserName, 0, 0, 1, 1)

        self.lineEditUser = QLineEdit(self.layoutWidget)
        self.lineEditUser.setObjectName(u"lineEditUser")
        sizePolicy1.setHeightForWidth(self.lineEditUser.sizePolicy().hasHeightForWidth())
        self.lineEditUser.setSizePolicy(sizePolicy1)
        self.lineEditUser.setMinimumSize(QSize(226, 25))
        self.lineEditUser.setMaximumSize(QSize(260, 25))

        self.gridLayout.addWidget(self.lineEditUser, 0, 1, 1, 1)

        self.lblPassword = QLabel(self.layoutWidget)
        self.lblPassword.setObjectName(u"lblPassword")
        sizePolicy1.setHeightForWidth(self.lblPassword.sizePolicy().hasHeightForWidth())
        self.lblPassword.setSizePolicy(sizePolicy1)
        self.lblPassword.setMinimumSize(QSize(77, 25))
        self.lblPassword.setMaximumSize(QSize(100, 25))

        self.gridLayout.addWidget(self.lblPassword, 1, 0, 1, 1)

        self.lineEditPassword = QLineEdit(self.layoutWidget)
        self.lineEditPassword.setObjectName(u"lineEditPassword")
        sizePolicy1.setHeightForWidth(self.lineEditPassword.sizePolicy().hasHeightForWidth())
        self.lineEditPassword.setSizePolicy(sizePolicy1)
        self.lineEditPassword.setMinimumSize(QSize(226, 25))
        self.lineEditPassword.setMaximumSize(QSize(260, 25))
        self.lineEditPassword.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.lineEditPassword, 1, 1, 1, 1)

        self.btnStartSesion = QPushButton(self.layoutWidget)
        self.btnStartSesion.setObjectName(u"btnStartSesion")
        sizePolicy1.setHeightForWidth(self.btnStartSesion.sizePolicy().hasHeightForWidth())
        self.btnStartSesion.setSizePolicy(sizePolicy1)
        self.btnStartSesion.setMinimumSize(QSize(226, 25))
        self.btnStartSesion.setMaximumSize(QSize(260, 25))

        self.gridLayout.addWidget(self.btnStartSesion, 2, 1, 1, 1)

        self.layoutWidget1 = QWidget(Login)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(110, 220, 231, 50))
        self.verticalLayout = QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.lblAccount = QLabel(self.layoutWidget1)
        self.lblAccount.setObjectName(u"lblAccount")
        sizePolicy1.setHeightForWidth(self.lblAccount.sizePolicy().hasHeightForWidth())
        self.lblAccount.setSizePolicy(sizePolicy1)
        self.lblAccount.setMinimumSize(QSize(229, 17))
        self.lblAccount.setMaximumSize(QSize(260, 17))
        self.lblAccount.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lblAccount)

        self.btnCreateAccount = QPushButton(self.layoutWidget1)
        self.btnCreateAccount.setObjectName(u"btnCreateAccount")
        self.btnCreateAccount.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.btnCreateAccount.sizePolicy().hasHeightForWidth())
        self.btnCreateAccount.setSizePolicy(sizePolicy1)
        self.btnCreateAccount.setMinimumSize(QSize(229, 25))
        self.btnCreateAccount.setMaximumSize(QSize(260, 25))

        self.verticalLayout.addWidget(self.btnCreateAccount)


        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Dialog", None))
        self.lblLogin.setText(QCoreApplication.translate("Login", u"Login", None))
        self.lblUserName.setText(QCoreApplication.translate("Login", u"User name:", None))
        self.lblPassword.setText(QCoreApplication.translate("Login", u"Password:", None))
        self.btnStartSesion.setText(QCoreApplication.translate("Login", u"Start sesion", None))
        self.lblAccount.setText(QCoreApplication.translate("Login", u"Do not have an account?", None))
        self.btnCreateAccount.setText(QCoreApplication.translate("Login", u"Create a new account", None))
    # retranslateUi

