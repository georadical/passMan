import sys
import re
import sqlite3
from sqlite3 import Error
from PySide6.QtWidgets import (QDialog, QApplication, 
                            QTableWidgetItem, QMessageBox)
from passlib.hash import pbkdf2_sha256
from PassMan import *
from Login import *
from NewItem import *

class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.btnStartSesion.clicked.connect(self.openLogin)
        self.ui.btnNewItem.clicked.connect(self.openNewItem)

        self.show()

    def openLogin(self): # It opens sign form
        self.Login = QtWidgets.QDialog()
        self.ui = Ui_Login()
        self.ui.setupUi(self.Login)
        

        self.message = QMessageBox()
        self.message.setWindowTitle('Message')

        self.ui.btnStartSesion.clicked.connect(self.startSesion)
        self.ui.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.Password)

        patern = r'[a-z0-9]+@[a-z]+\.[a-z]+'
        self.validate = re.compile(patern)
        self.Login.show()

    def startSesion(self):
        email = self.ui.lineEditUser.text().strip()
        
        if len(email) > 0:
            if self.validate.match(email) is not None:
                password = self.ui.lineEditPassword.text().strip()
                
                if len(password) > 0:
                        
                    try:
                        
                        con = sqlite3.connect('user.db')
                        cur = con.cursor()
                        user = cur.execute("""SELECT * FROM users WHERE email = ?""", (email, )).fetchone()
                        
                        if user is not None:

                            hash_stored = user[2]
                            
                            if pbkdf2_sha256.verify(password, hash_stored):
                                print(email)
                                self.message.setText('You have started a new section')
                                self.message.setIcon(QMessageBox.Warning)
                                self.message.exec()
                            else:
                                print(user)
                                self.message.setText('Not valid information')
                                self.message.setIcon(QMessageBox.Warning)
                                self.message.exec()


                        else:
                            self.message.setText('This email does not match any user')
                            self.message.setIcon(QMessageBox.Warning)
                            self.message.exec()
                    except Error as e:
                        self.message.setText('A problem has occurred connecting to DB')
                        self.message.setIcon(QMessageBox.Warning)
                        self.message.exec()


                else:
                    self.message.setText('Type a password please')
                    self.message.setIcon(QMessageBox.Warning)
                    self.message.exec()

            else:
                self.message.setText('Type a valid email please')
                self.message.setIcon(QMessageBox.Warning)
                self.message.exec()

        else:
            self.message.setText('Type an email please')
            self.message.setIcon(QMessageBox.Warning)
            self.message.exec()

    def openNewItem(self):
        self.NewItem = QtWidgets.QDialog()
        self.ui = Ui_NewItem()
        self.ui.setupUi(self.NewItem)
        self.NewItem.show()

if __name__=="__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec())
     