import sys
import psycopg2
import requests
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsPixmapItem
from PyQt5.QtWidgets import QTableWidgetItem
from design import Ui_MainWindow
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt



class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #########################################################################
        #СИГНАЛЫ
        self.pushButtonAuthorization.clicked.connect(self.authorizationForUser)
        self.pushButton.clicked.connect(self.open_bus_window)
        self.pushButton_2.clicked.connect(self.open_route_window)
        self.pushButtonMain.clicked.connect(self.open_main_window)
        self.pushButton_3.clicked.connect(self.open_graph_windows)
        self.pushButton_4.clicked.connect(self.open_stats_windows)
        self.pushButton_6.clicked.connect(self.AddNewBus)
        self.pushButton_7.clicked.connect(self.FindBusFromVin)
        #########################################################################
        self.map_scene = QGraphicsScene()
        self.graphicsView.setScene(self.map_scene)  # Используем уже созданный graphicsView


        # Первая загрузка карты
        self.load_static_map()


        ########################################################
        #БАЗОВЫЕ НАСТРОЙКИ ОТОБРАЖЕНИЯ
        self.widtegBus.setVisible(False)
        self.widgetRoutes.setVisible(False)
        self.widget_5.setVisible(False)
        self.widget_4.setVisible(False)
        #######################################################
        self.setup_chart()

    def setup_chart(self):
        """Альтернативный вариант без проверки layout"""
        # Полностью очищаем widget_5
        for child in self.widget_6.children():
            child.deleteLater()

        # Создаем новый layout
        new_layout = QtWidgets.QVBoxLayout(self.widget_6)
        new_layout.setContentsMargins(0, 0, 0, 0)

        # Создаем и добавляем график
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)
        new_layout.addWidget(self.canvas)

        # Рисуем данные
        self.ax.plot([1, 2, 3], [4, 5, 6])
        self.canvas.draw()

    def open_bus_window(self):
        self.widtegBus.setVisible(True)
        self.widgetRoutes.setVisible(False)
        self.widget_4.setVisible(False)
        self.widget_5.setVisible(False)
    def open_route_window(self):
        self.widgetRoutes.setVisible(True)
        self.widtegBus.setVisible(False)
        self.widget_4.setVisible(False)
        self.widget_5.setVisible(False)
    def open_main_window(self):
        self.widtegBus.setVisible(False)
        self.widgetRoutes.setVisible(False)
        self.widget_4.setVisible(False)
        self.widget_5.setVisible(False)
    def open_stats_windows(self):
        self.widget_5.setVisible(True)
        self.widtegBus.setVisible(False)
        self.widgetRoutes.setVisible(False)
        self.widget_4.setVisible(False)
    def open_graph_windows(self):
        self.widget_4.setVisible(True)
        self.widtegBus.setVisible(False)
        self.widgetRoutes.setVisible(False)
        self.widget_5.setVisible(False)


    def load_static_map(self):
        """Загружает статичную карту с маршрутом Подольск-Чехов"""
        try:
            # Координаты (Подольск → Чехов)
            podolsk = "37.5547,55.4242"  # Обратите порядок: долгота,широта!
            chekhov = "37.4873,55.1527"
            size = "650,450"  # Теперь с запятой, как требует API
            api_key = "08b76ad6-f685-4f52-b73d-ea6981593637"

            # Формируем URL строго по документации
            url = (
                f"https://static-maps.yandex.ru/v1?"
                f"size={size}"
                f"&pl=c:8822DDC0,w:5,{podolsk},{chekhov}"  # Ломаная линия
                f"&pt={podolsk},pm2rdm~{chekhov},pm2blm"  # Метки
                f"&apikey={api_key}"
            )

            print("Финальный URL:", url)  # Для отладки

            headers = {"User-Agent": "Mozilla/5.0"}
            response = requests.get(url, headers=headers, timeout=10)

            if response.status_code == 200:
                pixmap = QtGui.QPixmap()
                pixmap.loadFromData(response.content)

                self.map_scene.clear()
                self.map_scene.addPixmap(pixmap)
                print("Маршрут успешно загружен")
            else:
                raise Exception(f"{response.status_code}: {response.text[:200]}")

        except Exception as e:
            error_msg = f"Ошибка: {str(e)}"
            print(error_msg)

            # Создаём информативную заглушку
            error_pixmap = QtGui.QPixmap(871, 371)
            error_pixmap.fill(QtGui.QColor("#f0f0f0"))

            painter = QtGui.QPainter(error_pixmap)
            painter.setPen(QtGui.QColor("red"))
            painter.setFont(QtGui.QFont("Arial", 10))
            painter.drawText(20, 50, error_msg)
            painter.end()

            self.map_scene.addPixmap(error_pixmap)



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

    def AddNewBus(self):
        number = self.lineEdit_state_number.text()
        vin = self.lineEdit_vin.text()
        model = self.lineEdit_bus_model.text()
        year = self.lineEdit_bus_year.text()
        odometer = self.lineEdit_odometer.text()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO bus (state_number, VIN, model, year_of_release, odometer) VALUES (%s, %s, %s, %s, %s)",
                       (number, vin, model, year, odometer))
        conn.commit()
        cursor.close()
    def FindBusFromVin(self):
        vin = self.lineEdit_vin_find.text()
        cursor = conn.cursor()
        cursor.execute("""SELECT state_number AS "Гос.Номер", VIN, model as "Модель", year_of_release as "Год", odometer as "Пробег" FROM bus WHERE VIN = %s;""",
                       (vin, ))
        len_row = cursor.rowcount
        rows = cursor.fetchall()
        cols = cursor.description
        self.tableWidget.setColumnCount(len(cols))
        self.tableWidget.setRowCount(len_row)
        for i in range(len(cols)):
            self.tableWidget.setHorizontalHeaderItem(i, QTableWidgetItem(cols[i][0]))
        for i in range(len_row):
            for j in range(len(rows[i])):
                item = QTableWidgetItem(str(rows[i][j]))
                self.tableWidget.setItem(i, j, item)
        cursor.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
