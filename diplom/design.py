from PyQt5 import QtCore, QtGui, QtWidgets
import psycopg2


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1000, 800)
        MainWindow.setStyleSheet("background-color: rgb(246, 242, 235);\n"
"\n"
"\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(110, 0, 41, 801))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(130, 60, 881, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 70, 131, 731))
        self.widget.setStyleSheet("background-color: rgb(44, 54, 57);\n"
"border: none;\n"
"border-right: 2px solid rgb(68, 89, 90);\n"
"padding: 15px;")
        self.widget.setObjectName("widget")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(0, 460, 121, 41))
        self.pushButton.setStyleSheet("QPushButton {\n"
"    background-color: rgb(60, 70, 73);\n"
"    color: rgb(220, 220, 220);\n"
"    border: 1px solid rgb(68, 89, 90);\n"
"    border-radius: 6px;\n"
"    padding: 8px 12px;\n"
"    margin: 4px 8px;\n"
"    font-size: 14px;\n"
"    text-align: left;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(68, 89, 90);\n"
"    color: rgb(246, 242, 235);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(52, 72, 74);\n"
"    border: 1px solid rgb(50, 65, 66);\n"
"}\n"
"\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 510, 121, 41))
        self.pushButton_2.setStyleSheet("QPushButton {\n"
"    background-color: rgb(60, 70, 73);\n"
"    color: rgb(220, 220, 220);\n"
"    border: 1px solid rgb(68, 89, 90);\n"
"    border-radius: 6px;\n"
"    padding: 8px 12px;\n"
"    margin: 4px 8px;\n"
"    font-size: 14px;\n"
"    text-align: left;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(68, 89, 90);\n"
"    color: rgb(246, 242, 235);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(52, 72, 74);\n"
"    border: 1px solid rgb(50, 65, 66);\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setGeometry(QtCore.QRect(0, 560, 121, 41))
        self.pushButton_3.setStyleSheet("QPushButton {\n"
"    background-color: rgb(60, 70, 73);\n"
"    color: rgb(220, 220, 220);\n"
"    border: 1px solid rgb(68, 89, 90);\n"
"    border-radius: 6px;\n"
"    padding: 8px 12px;\n"
"    margin: 4px 8px;\n"
"    font-size: 14px;\n"
"    text-align: left;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(68, 89, 90);\n"
"    color: rgb(246, 242, 235);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(52, 72, 74);\n"
"    border: 1px solid rgb(50, 65, 66);\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 610, 121, 41))
        self.pushButton_4.setStyleSheet("QPushButton {\n"
"    background-color: rgb(60, 70, 73);\n"
"    color: rgb(220, 220, 220);\n"
"    border: 1px solid rgb(68, 89, 90);\n"
"    border-radius: 6px;\n"
"    padding: 8px 12px;\n"
"    margin: 4px 8px;\n"
"    font-size: 14px;\n"
"    text-align: left;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(68, 89, 90);\n"
"    color: rgb(246, 242, 235);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(52, 72, 74);\n"
"    border: 1px solid rgb(50, 65, 66);\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButtonMain = QtWidgets.QPushButton(self.widget)
        self.pushButtonMain.setGeometry(QtCore.QRect(0, 20, 121, 41))
        self.pushButtonMain.setStyleSheet("QPushButton {\n"
"    background-color: rgb(60, 70, 73);\n"
"    color: rgb(220, 220, 220);\n"
"    border: 1px solid rgb(68, 89, 90);\n"
"    border-radius: 6px;\n"
"    padding: 8px 12px;\n"
"    margin: 4px 8px;\n"
"    font-size: 14px;\n"
"    text-align: left;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(68, 89, 90);\n"
"    color: rgb(246, 242, 235);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(52, 72, 74);\n"
"    border: 1px solid rgb(50, 65, 66);\n"
"}")
        self.pushButtonMain.setObjectName("pushButtonMain")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(0, 0, 1001, 81))
        self.widget_2.setStyleSheet("background-color: rgb(68, 89, 90);\n"
"")
        self.widget_2.setObjectName("widget_2")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setGeometry(QtCore.QRect(10, 20, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(246, 242, 235);\n"
"    font-size: 24px;")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setGeometry(QtCore.QRect(200, 20, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(246, 242, 235);\n"
"    font-size: 24px;")
        self.label_2.setObjectName("label_2")
        self.line_3 = QtWidgets.QFrame(self.widget_2)
        self.line_3.setGeometry(QtCore.QRect(161, 10, 31, 61))
        self.line_3.setStyleSheet("")
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setGeometry(QtCore.QRect(740, 40, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(246, 242, 235);\n"
"    font-size: 24px;")
        self.label_3.setObjectName("label_3")
        self.line_4 = QtWidgets.QFrame(self.widget_2)
        self.line_4.setGeometry(QtCore.QRect(830, 0, 20, 71))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.label_4 = QtWidgets.QLabel(self.widget_2)
        self.label_4.setGeometry(QtCore.QRect(880, 40, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color: rgb(246, 242, 235);\n"
"    font-size: 24px;")
        self.label_4.setObjectName("label_4")
        self.line_5 = QtWidgets.QFrame(self.widget_2)
        self.line_5.setGeometry(QtCore.QRect(370, 10, 31, 61))
        self.line_5.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(300, 90, 481, 61))
        font = QtGui.QFont()
        font.setFamily("Lucida Fax")
        font.setPointSize(36)
        font.setItalic(True)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("")
        self.label_5.setObjectName("label_5")
        self.line_6 = QtWidgets.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(130, 150, 871, 21))
        self.line_6.setStyleSheet("")
        self.line_6.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_6.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_6.setObjectName("line_6")
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setEnabled(True)
        self.widget_3.setGeometry(QtCore.QRect(0, 0, 1001, 801))
        self.widget_3.setStyleSheet("background-color: rgb(44, 54, 57);")
        self.widget_3.setObjectName("widget_3")
        self.lineEditLogin = QtWidgets.QLineEdit(self.widget_3)
        self.lineEditLogin.setGeometry(QtCore.QRect(340, 300, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditLogin.setFont(font)
        self.lineEditLogin.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEditLogin.setObjectName("lineEditLogin")
        self.lineEditPassword = QtWidgets.QLineEdit(self.widget_3)
        self.lineEditPassword.setGeometry(QtCore.QRect(340, 360, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEditPassword.setFont(font)
        self.lineEditPassword.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.pushButtonAuthorization = QtWidgets.QPushButton(self.widget_3)
        self.pushButtonAuthorization.setGeometry(QtCore.QRect(330, 410, 281, 51))
        self.pushButtonAuthorization.setStyleSheet("QPushButton {\n"
"    background-color: rgb(60, 70, 73);\n"
"    color: rgb(220, 220, 220);\n"
"    border: 1px solid rgb(68, 89, 90);\n"
"    border-radius: 6px;\n"
"    padding: 8px 12px;\n"
"    margin: 4px 8px;\n"
"    font-size: 14px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(68, 89, 90);\n"
"    color: rgb(246, 242, 235);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(52, 72, 74);\n"
"    border: 1px solid rgb(50, 65, 66);\n"
"}")
        self.pushButtonAuthorization.setObjectName("pushButtonAuthorization")
        self.label_6 = QtWidgets.QLabel(self.widget_3)
        self.label_6.setGeometry(QtCore.QRect(230, 290, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Lucida Fax")
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(251, 255, 242);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.widget_3)
        self.label_7.setGeometry(QtCore.QRect(220, 350, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Lucida Fax")
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(251, 255, 242);")
        self.label_7.setObjectName("label_7")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Автобусы"))
        self.pushButton_2.setText(_translate("MainWindow", "Маршруты"))
        self.pushButton_3.setText(_translate("MainWindow", "Расписание"))
        self.pushButton_4.setText(_translate("MainWindow", "Аналитика"))
        self.pushButtonMain.setText(_translate("MainWindow", "Главная"))
        self.label.setText(_translate("MainWindow", "Bus Manager 1.0"))
        self.label_2.setText(_translate("MainWindow", "Welcome, user user"))
        self.label_3.setText(_translate("MainWindow", "message: 0"))
        self.label_4.setText(_translate("MainWindow", "help"))
        self.label_5.setText(_translate("MainWindow", "Сегодня 28.05.2025"))
        self.pushButtonAuthorization.setText(_translate("MainWindow", "Войти"))
        self.label_6.setText(_translate("MainWindow", "Логин"))
        self.label_7.setText(_translate("MainWindow", "Пароль"))



#if __name__ == "__main__":
#    import sys
#    app = QtWidgets.QApplication(sys.argv)
#    MainWindow = QtWidgets.QMainWindow()
#    ui = Ui_MainWindow()
#    ui.setupUi(MainWindow)
#    MainWindow.show()
#    sys.exit(app.exec_())
