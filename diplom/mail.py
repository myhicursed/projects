import sys
import psycopg2
from PyQt5 import QtWidgets, QtCore
from design import Ui_MainWindow


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButtonAuthorization.clicked.connect(self.authorizationForUser)

    def authorizationToDatabaseFromDispatcher(self, user_a = 'dispatcher', password_a = '123'):
        try:
            global conn
            conn = psycopg2.connect(
                host = 'localhost',
                database = 'buspark',
                user = 'dispatcher',
                password = 123,
                port = '5432'
            )
        except:
            print('Не удалось установить соединение')

    def authorizationForUser(self):
        l_conn = psycopg2.connect(
            host = 'localhost',
            database = 'buspark',
            user = 'postgres',
            password = 'myhicursed',
            port = '5432'
        )
        u_login = self.lineEditLogin.text()
        u_password = self.lineEditPassword.text()
        cursor = l_conn.cursor()
        cursor.execute(""" SELECT user_password 
                                              FROM users
                                              WHERE user_login = %s;
""", (u_login,))
        record_password = cursor.fetchall()
        current_password = record_password[0]
        if u_password == current_password[0]:
            print('Авторизация пройдена')
            cursor.close()
            self.authorizationToDatabaseFromDispatcher()
            print(f'login: {u_login}')
            self.widget_3.setVisible(False)
        else:
            print('Неверный логин/пароль')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
