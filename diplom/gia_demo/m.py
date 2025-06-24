from PyQt5 import QtCore, QtGui, QtWidgets
import psycopg2

conn = psycopg2.connect(
    host = 'localhost',
    database = 'postgres',
    user = 'postgres',
    password = 'myhicursed',
    port = '5432'
)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1174, 861)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(60, 40, 1041, 431))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()

        self.scrollLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)


        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1039, 429))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.widget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget.setGeometry(QtCore.QRect(30, 40, 961, 141))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(30, 20, 191, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(30, 50, 131, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(30, 80, 151, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(826, 20, 121, 20))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(30, 110, 121, 16))
        self.label_5.setObjectName("label_5")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.widget.hide()
        cursor = conn.cursor()
        cursor.execute("""SELECT partner_type, partner_name, director, telephone, rate 
                                    FROM partners """)
        rows = cursor.fetchall()
        for i, row in enumerate(rows):
            a, b, c, d, e = row
            new_card = self.CreateCard(a, b, c, d, e)
            self.scrollLayout.addWidget(new_card)

    def CreateCard(self, a, b, c, d, e):
        card = QtWidgets.QWidget()
        card.setFixedSize(self.widget.size())
        card.setStyleSheet(self.widget.styleSheet())

        label1 = QtWidgets.QLabel(card)
        label1.setGeometry(self.label.geometry())
        label1.setText(f'{a} | {b}')

        label2 = QtWidgets.QLabel(card)
        label2.setGeometry(self.label_2.geometry())
        label2.setText(c)

        label3 = QtWidgets.QLabel(card)
        label3.setGeometry(self.label_3.geometry())
        label3.setText(d)

        label4 = QtWidgets.QLabel(card)
        label4.setGeometry(self.label_4.geometry())
        label4.setText("")

        label5 = QtWidgets.QLabel(card)
        label5.setGeometry(self.label_5.geometry())
        label5.setText(f'Рейтинг: {e}')
        return card

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Тип | Партнер"))
        self.label_2.setText(_translate("MainWindow", "Директор"))
        self.label_3.setText(_translate("MainWindow", "Телефон"))
        self.label_4.setText(_translate("MainWindow", "%"))
        self.label_5.setText(_translate("MainWindow", "Рейтинг"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
