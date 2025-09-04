from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
import psycopg2

########################################
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(809, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("background-color: rgb(217, 217, 217);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setEnabled(True)
        self.widget.setGeometry(QtCore.QRect(0, 0, 120, 601))
        self.widget.setStyleSheet("background-color: rgb(103, 103, 103);")
        self.widget.setObjectName("widget")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(10, 220, 105, 35))
        self.pushButton.setStyleSheet("background-color: rgb(158, 158, 158);\n"
                                      "border-radius: 2px;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.widget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 270, 105, 35))
        self.pushButton_2.setStyleSheet("background-color: rgb(158, 158, 158);\n"
                                        "border-radius: 2px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 320, 105, 35))
        self.pushButton_3.setStyleSheet("background-color: rgb(158, 158, 158);\n"
                                        "border-radius: 2px;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 550, 105, 35))
        self.pushButton_4.setStyleSheet("background-color: rgb(158, 158, 158);\n"
                                        "border-radius: 2px;")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.widget)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 170, 105, 35))
        self.pushButton_5.setStyleSheet("background-color: rgb(158, 158, 158);\n"
                                        "border-radius: 2px;")
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(0, 60, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton_12 = QtWidgets.QPushButton(self.widget)
        self.pushButton_12.setGeometry(QtCore.QRect(10, 370, 105, 35))
        self.pushButton_12.setStyleSheet("background-color: rgb(158, 158, 158);\n"
                                         "border-radius: 2px;")
        self.pushButton_12.setObjectName("pushButton_12")
        self.label_10 = QtWidgets.QLabel(self.widget)
        self.label_10.setGeometry(QtCore.QRect(20, 90, 161, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_10.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton_3.raise_()
        self.pushButton_4.raise_()
        self.pushButton_5.raise_()
        self.pushButton_12.raise_()
        self.label_3.raise_()
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(0, 0, 811, 61))
        self.widget_2.setStyleSheet("background-color: rgb(77, 77, 77);")
        self.widget_2.setObjectName("widget_2")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setGeometry(QtCore.QRect(10, 10, 281, 51))
        font = QtGui.QFont()
        font.setFamily("Ink Free")
        font.setPointSize(26)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_9 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_9.setGeometry(QtCore.QRect(740, 10, 50, 50))
        self.pushButton_9.setStyleSheet("QPushButton {\n"
                                        " background-image: url(\'C:/databases/uv.jpg\');\n"
                                        " background-repeat: no-repeat;\n"
                                        " background-position: center;\n"
                                        " background-size: cover;\n"
                                        " border-radius: 10px;\n"
                                        "border: solid black 4px;\n"
                                        "}\n"
                                        "")
        self.pushButton_9.setText("")
        self.pushButton_9.setObjectName("pushButton_9")
        self.calendarWidget = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendarWidget.setGeometry(QtCore.QRect(490, 60, 312, 183))
        self.calendarWidget.setStyleSheet("background-color: rgb(234, 168, 169);")
        self.calendarWidget.setObjectName("calendarWidget")
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setEnabled(True)
        self.widget_3.setGeometry(QtCore.QRect(120, 60, 691, 541))
        self.widget_3.setObjectName("widget_3")
        self.pushButton_6 = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_6.setGeometry(QtCore.QRect(100, 320, 175, 40))
        self.pushButton_6.setStyleSheet("background-color: rgb(158, 158, 158);\n"
                                        "border-radius: 2px;")
        self.pushButton_6.setObjectName("pushButton_6")
        self.line = QtWidgets.QFrame(self.widget_3)
        self.line.setGeometry(QtCore.QRect(310, 0, 20, 541))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.pushButton_7 = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_7.setGeometry(QtCore.QRect(100, 370, 175, 40))
        self.pushButton_7.setStyleSheet("background-color: rgb(158, 158, 158);\n"
                                        "border-radius: 2px;")
        self.pushButton_7.setObjectName("pushButton_7")
        self.lineEdit = QtWidgets.QLineEdit(self.widget_3)
        self.lineEdit.setGeometry(QtCore.QRect(80, 170, 220, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget_3)
        self.lineEdit_2.setGeometry(QtCore.QRect(80, 210, 220, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget_3)
        self.lineEdit_3.setGeometry(QtCore.QRect(80, 250, 220, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_2 = QtWidgets.QLabel(self.widget_3)
        self.label_2.setGeometry(QtCore.QRect(10, 170, 41, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.widget_3)
        self.label_4.setGeometry(QtCore.QRect(10, 210, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.widget_3)
        self.label_5.setGeometry(QtCore.QRect(10, 250, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.tableWidget = QtWidgets.QTableWidget(self.widget_3)
        self.tableWidget.setGeometry(QtCore.QRect(320, 0, 361, 541))
        self.tableWidget.setStyleSheet("background-color: rgb(157, 157, 157);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.label_6 = QtWidgets.QLabel(self.widget_3)
        self.label_6.setGeometry(QtCore.QRect(90, 120, 200, 25))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.pushButton_8 = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_8.setGeometry(QtCore.QRect(100, 420, 175, 40))
        self.pushButton_8.setStyleSheet("background-color: rgb(158, 158, 158);\n"
                                        "border-radius: 2px;")
        self.pushButton_8.setObjectName("pushButton_8")
        self.checkBox = QtWidgets.QCheckBox(self.widget_3)
        self.checkBox.setGeometry(QtCore.QRect(10, 290, 141, 17))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.widget_5 = QtWidgets.QWidget(self.centralwidget)
        self.widget_5.setEnabled(True)
        self.widget_5.setGeometry(QtCore.QRect(130, 60, 681, 551))
        self.widget_5.setObjectName("widget_5")
        self.label_9 = QtWidgets.QLabel(self.widget_5)
        self.label_9.setGeometry(QtCore.QRect(90, 20, 531, 35))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(24)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.tableWidget_2 = QtWidgets.QTableWidget(self.widget_5)
        self.tableWidget_2.setGeometry(QtCore.QRect(0, 80, 671, 461))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(0)
        self.tableWidget_2.setRowCount(0)
        self.widget_4 = QtWidgets.QWidget(self.centralwidget)
        self.widget_4.setGeometry(QtCore.QRect(0, -10, 811, 611))
        self.widget_4.setStyleSheet("background-color: rgb(120, 120, 120);")
        self.widget_4.setObjectName("widget_4")
        self.label_7 = QtWidgets.QLabel(self.widget_4)
        self.label_7.setGeometry(QtCore.QRect(100, 270, 200, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(144, 255, 205);")
        self.label_7.setObjectName("label_7")
        self.pushButton_10 = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_10.setGeometry(QtCore.QRect(310, 340, 200, 75))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.pushButton_10.setFont(font)
        self.pushButton_10.setStyleSheet("background-color: rgb(16, 76, 66);\n"
                                         "border-radius: 10px;")
        self.pushButton_10.setObjectName("pushButton_10")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.widget_4)
        self.lineEdit_6.setGeometry(QtCore.QRect(310, 270, 200, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setAcceptDrops(True)
        self.lineEdit_6.setAutoFillBackground(False)
        self.lineEdit_6.setStyleSheet("border-color: rgb(96, 33, 255);\n"
                                      "background-color: rgb(255, 255, 255);\n"
                                      "border-radius: 10px;\n"
                                      "border: 3px  solid rgb(16, 76, 66);")
        self.lineEdit_6.setPlaceholderText("")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_8 = QtWidgets.QLabel(self.widget_4)
        self.label_8.setGeometry(QtCore.QRect(100, 170, 200, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(144, 255, 205);")
        self.label_8.setObjectName("label_8")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget_4)
        self.lineEdit_5.setGeometry(QtCore.QRect(310, 180, 200, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet("border-color: rgb(96, 33, 255);\n"
                                      "background-color: rgb(255, 255, 255);\n"
                                      "border-radius: 10px;\n"
                                      "border: 3px  solid rgb(16, 76, 66);")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.widget_6 = QtWidgets.QWidget(self.centralwidget)
        self.widget_6.setGeometry(QtCore.QRect(200, 190, 501, 281))
        self.widget_6.setStyleSheet("background-color: rgb(173, 173, 173);\n"
                                    "border: 2px solid black;\n"
                                    "border-radius: 20px;")
        self.widget_6.setObjectName("widget_6")
        self.label_11 = QtWidgets.QLabel(self.widget_6)
        self.label_11.setGeometry(QtCore.QRect(160, 10, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("border: 0px;")
        self.label_11.setObjectName("label_11")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget_6)
        self.lineEdit_4.setGeometry(QtCore.QRect(160, 60, 211, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.widget_6)
        self.lineEdit_7.setGeometry(QtCore.QRect(160, 100, 211, 31))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.dateEdit = QtWidgets.QDateEdit(self.widget_6)
        self.dateEdit.setGeometry(QtCore.QRect(160, 180, 211, 31))
        self.dateEdit.setObjectName("dateEdit")
        self.pushButton_13 = QtWidgets.QPushButton(self.widget_6)
        self.pushButton_13.setGeometry(QtCore.QRect(340, 230, 151, 35))
        self.pushButton_13.setStyleSheet("background-color: rgb(158, 158, 158);\n"
                                         "border-radius: 2px;")
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.widget_6)
        self.pushButton_14.setGeometry(QtCore.QRect(10, 230, 151, 35))
        self.pushButton_14.setStyleSheet("background-color: rgb(158, 158, 158);\n"
                                         "border-radius: 2px;")
        self.pushButton_14.setObjectName("pushButton_14")
        self.label_12 = QtWidgets.QLabel(self.widget_6)
        self.label_12.setGeometry(QtCore.QRect(50, 70, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("border: 0px;")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.widget_6)
        self.label_13.setGeometry(QtCore.QRect(50, 110, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("border: 0px;")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.widget_6)
        self.label_14.setGeometry(QtCore.QRect(50, 180, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("border: 0px;")
        self.label_14.setObjectName("label_14")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.widget_6)
        self.lineEdit_8.setGeometry(QtCore.QRect(160, 140, 211, 31))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_15 = QtWidgets.QLabel(self.widget_6)
        self.label_15.setGeometry(QtCore.QRect(50, 140, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet("border: 0px;")
        self.label_15.setObjectName("label_15")
        self.widget_7 = QtWidgets.QWidget(self.centralwidget)
        self.widget_7.setEnabled(True)
        self.widget_7.setGeometry(QtCore.QRect(130, 60, 681, 551))
        self.widget_7.setObjectName("widget_7")
        self.tableWidget_6 = QtWidgets.QTableWidget(self.widget_7)
        self.tableWidget_6.setGeometry(QtCore.QRect(0, 80, 671, 461))
        self.tableWidget_6.setObjectName("tableWidget_6")
        self.tableWidget_6.setColumnCount(0)
        self.tableWidget_6.setRowCount(0)
        self.label_17 = QtWidgets.QLabel(self.widget_7)
        self.label_17.setGeometry(QtCore.QRect(160, 10, 401, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.widget.raise_()
        self.widget_2.raise_()
        self.calendarWidget.raise_()
        self.widget_3.raise_()
        self.widget_5.raise_()
        self.widget_7.raise_()
        self.widget_4.raise_()
        self.widget_6.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

##################################################
        #базовая установка отображения
        self.widget.hide()
        self.widget_2.hide()
        self.widget_3.hide()
        self.calendarWidget.hide()
        self.widget_5.hide()
        self.widget_6.hide()
        self.widget_7.hide()

        # сигналы
        self.pushButton_5.clicked.connect(self.selectWindow1)
        self.pushButton.clicked.connect(self.selectWindow2)
        self.pushButton_4.clicked.connect(self.exit)
        self.pushButton_3.clicked.connect(self.showCustomers)
        self.pushButton_10.clicked.connect(self.autorization)
        self.pushButton_6.clicked.connect(self.addCustomers)
        self.pushButton_7.clicked.connect(self.findCustomers)
        self.pushButton_2.clicked.connect(self.selectWindow3)
        self.pushButton_12.clicked.connect(self.selectWindow4)
        self.pushButton_14.clicked.connect(self.closeWindow4)
        self.pushButton_13.clicked.connect(self.createMeeting)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Клиенты"))
        self.pushButton_2.setText(_translate("MainWindow", "Взаимодействие"))
        self.pushButton_3.setText(_translate("MainWindow", "Отчеты и анализ"))
        self.pushButton_4.setText(_translate("MainWindow", "Выход"))
        self.pushButton_5.setText(_translate("MainWindow", "Главная"))
        self.label_3.setText(_translate("MainWindow", "привет, "))
        self.pushButton_12.setText(_translate("MainWindow", "Назначить встречу"))
        self.label_10.setText(_translate("MainWindow", "username"))
        self.label.setText(_translate("MainWindow", "mhc CRM"))
        self.pushButton_6.setText(_translate("MainWindow", "Добавить клиента"))
        self.pushButton_7.setText(_translate("MainWindow", "Поиск по клиенту"))
        self.label_2.setText(_translate("MainWindow", "ФИО"))
        self.label_4.setText(_translate("MainWindow", "Телефон"))
        self.label_5.setText(_translate("MainWindow", "Компания"))
        self.pushButton_8.setText(_translate("MainWindow", "Удалить клиента"))
        self.checkBox.setText(_translate("MainWindow", "Договор подписан?"))
        self.label_9.setText(_translate("MainWindow", "История взаимодействия с клиентом"))
        self.label_7.setText(_translate("MainWindow", "Пароль"))
        self.pushButton_10.setText(_translate("MainWindow", "Подключиться"))
        self.label_8.setText(_translate("MainWindow", "Имя пользователя"))
        self.label_11.setText(_translate("MainWindow", "Заполните данные"))
        self.pushButton_13.setText(_translate("MainWindow", "Назначить встречу"))
        self.pushButton_14.setText(_translate("MainWindow", "Отмена"))
        self.label_12.setText(_translate("MainWindow", "ФИО"))
        self.label_13.setText(_translate("MainWindow", "Компания"))
        self.label_14.setText(_translate("MainWindow", "Дата"))
        self.label_15.setText(_translate("MainWindow", "Адрес"))
        self.label_17.setText(_translate("MainWindow", "Отчеты и анализ клиентов"))

    def selectWindow1(self):
        self.widget_3.hide()
        self.widget_5.hide()
        self.widget_7.hide()

    def selectWindow2(self):
        self.widget_3.show()
        self.widget_5.hide()
        self.widget_7.hide()

    def exit(self):
        self.close()

    def autorization(self):
        flag = False
        name = self.lineEdit_5.text()
        try:
            global conn
            conn = psycopg2.connect(
                host = 'localhost',
                database = 'postgres',
                user = self.lineEdit_5.text(),
                password = self.lineEdit_6.text(),
                port = '5432'
            )
            flag = True
        except:
            print('Не удалось установить соединение')
            flag = False
        if flag:
            self.widget_4.hide()
            self.widget.show()
            self.widget_2.show()
            self.calendarWidget.show()
            self.label_10.setText(name)

    def showCustomers(self):
        self.widget_7.show()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM customers")
        lenrow = cursor.rowcount
        rows = cursor.fetchall()
        cols = cursor.description
        self.tableWidget_6.setColumnCount(len(cols))
        self.tableWidget_6.setRowCount(lenrow)
        for i in range(lenrow):
            for j in range(len(rows[i])):
                item = QTableWidgetItem(str(rows[i][j]))
                self.tableWidget_6.setItem(i, j, item)
        cursor.close()

    def addCustomers(self):
        text1 = self.lineEdit.text()
        text2 = self.lineEdit_2.text()
        text3 = self.lineEdit_3.text()
        if text1 and text2 and text3:
            cursor = conn.cursor()
            text1 = self.lineEdit.text()
            text2 = self.lineEdit_2.text()
            text3 = self.lineEdit_3.text()
            res = self.checkBox.isChecked()
            if res:
                res = "Подписан"
            else:
                res = "Не подписан"
            cursor.execute("INSERT INTO customers (fio, telephone, company, contract) VALUES (%s, %s, %s, %s)",
                           (text1, text2, text3, res)
                           )
            conn.commit()
            cursor.close()
            self.label_6.setText('Клиент успешно добавлен')
        else:
            self.label_6.setText('Заполните все строки!')

    def findCustomers(self):
        cursor = conn.cursor()

        text1 = self.lineEdit.text()
        text2 = self.lineEdit_2.text()
        text3 = self.lineEdit_3.text()
        res = self.checkBox.isChecked()

        if not text2 and not text3:
            cursor.execute("SELECT * FROM customers WHERE fio = %s", (text1, ))
            lenrow = cursor.rowcount
            rows = cursor.fetchall()
            cols = cursor.description
            self.tableWidget.setColumnCount(len(cols))
            self.tableWidget.setRowCount(lenrow)
            for i in range(lenrow):
                for j in range(len(rows[i])):
                    item = QTableWidgetItem(str(rows[i][j]))
                    self.tableWidget.setItem(i, j, item)
        if not text1 and not text3:
            cursor.execute("SELECT * FROM customers WHERE telephone = %s", (text2, ))
            lenrow = cursor.rowcount
            rows = cursor.fetchall()
            cols = cursor.description
            self.tableWidget.setColumnCount(len(cols))
            self.tableWidget.setRowCount(lenrow)
            for i in range(lenrow):
                for j in range(len(rows[i])):
                    item = QTableWidgetItem(str(rows[i][j]))
                    self.tableWidget.setItem(i, j, item)
        if not text1 and not text2:
            cursor.execute("SELECT * FROM customers WHERE company = %s", (text3, ))
            lenrow = cursor.rowcount
            rows = cursor.fetchall()
            cols = cursor.description
            self.tableWidget.setColumnCount(len(cols))
            self.tableWidget.setRowCount(lenrow)
            for i in range(lenrow):
                for j in range(len(rows[i])):
                    item = QTableWidgetItem(str(rows[i][j]))
                    self.tableWidget.setItem(i, j, item)
        if text1 == True and text2 == True and text3 == True:
            cursor.execute("SELECT * FROM customers WHERE fio = %s AND telephone = %s AND company = %s", (text1, text2, text3, ))
            lenrow = cursor.rowcount
            rows = cursor.fetchall()
            cols = cursor.description
            self.tableWidget.setColumnCount(len(cols))
            self.tableWidget.setRowCount(lenrow)
            for i in range(lenrow):
                for j in range(len(rows[i])):
                    item = QTableWidgetItem(str(rows[i][j]))
                    self.tableWidget.setItem(i, j, item)

        cursor.close()

    def selectWindow3(self):
        self.widget_5.show()
        self.widget_7.hide()

        cursor = conn.cursor()

        cursor.execute("SELECT * FROM meeting ")
        lenrow = cursor.rowcount
        rows = cursor.fetchall()
        cols = cursor.description
        self.tableWidget_2.setColumnCount(len(cols))
        self.tableWidget_2.setRowCount(lenrow)
        for i in range(lenrow):
            for j in range(len(rows[i])):
                item = QTableWidgetItem(str(rows[i][j]))
                self.tableWidget_2.setItem(i, j, item)


    def selectWindow4(self):
        self.widget_6.show()

    def closeWindow4(self):
        self.widget_6.hide()

    def createMeeting(self):
        cursor = conn.cursor()
        fio = self.lineEdit_4.text()
        company = self.lineEdit_7.text()
        address = self.lineEdit_8.text()
        date = self.dateEdit.text()

        cursor.execute("INSERT INTO meeting (fio, company, address, date_meeting) VALUES (%s, %s, %s, %s)",
                       (fio, company, address, date)
                       )

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
