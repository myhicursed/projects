import sys
import psycopg2
import requests
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsPixmapItem, QMessageBox
from PyQt5.QtWidgets import QTableWidgetItem
from design import Ui_MainWindow
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from datetime import date



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
        self.pushButton_8.clicked.connect(self.SendToService)
        self.pushButton_12.clicked.connect(self.load_static_map)
        self.pushButton_13.clicked.connect(self.openPlaneWindow)
        self.pushButton_14.clicked.connect(self.closePlaneWindow)
        self.pushButton_11.clicked.connect(self.CreateRoute)
        self.pushButton_14.clicked.connect(self.CreateOrder)
        self.pushButton_5.clicked.connect(self.OpenCreateBusWindow)
        self.pushButton_9.clicked.connect(self.CloseRouteCreateWindow)
        self.pushButton_16.clicked.connect(self.CloseBusCreateWindow)
        self.pushButton_15.clicked.connect(self.ShowAllBuses)
        #########################################################################
        self.map_scene = QGraphicsScene()
        self.graphicsView.setScene(self.map_scene)  # Используем уже созданный graphicsView


        # Первая загрузка карты
        #self.load_static_map()


        ########################################################
        #БАЗОВЫЕ НАСТРОЙКИ ОТОБРАЖЕНИЯ
        self.widtegBus.setVisible(False)
        self.widgetRoutes.setVisible(False)
        self.widget_5.setVisible(False)
        self.widget_4.setVisible(False)
        self.widget_8.setVisible(False)
        self.widget_9.setVisible(False)
        today = date.today()
        self.label_5.setText(f"Сегодня: {today.strftime('%d.%m.%Y')}")
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
        self.ShowAllOrders()
    def openPlaneWindow(self):
        self.widget_8.setVisible(True)
    def closePlaneWindow(self):
        self.widget_8.setVisible(False)
    def OpenCreateBusWindow(self):
        self.widget_9.setVisible(True)
    def CloseBusCreateWindow(self):
        self.widget_9.setVisible(False)
    def CloseRouteCreateWindow(self):
        self.widget_8.setVisible(False)

    def get_coordinates(self, place_name, api_key):
        geocoder_url = f"https://geocode-maps.yandex.ru/1.x/"
        params = {
            'apikey': api_key,
            'geocode': place_name,
            'format': 'json'
        }

        response = requests.get(geocoder_url, params=params)
        if response.status_code == 200:
            data = response.json()
            try:
                pos = data['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
                longitude, latitude = pos.split()
                return f"{longitude},{latitude}"
            except (KeyError, IndexError):
                return None
        return None

    def load_static_map(self):
        """Загружает статичную карту с маршрутом по 5 точкам"""
        try:
            # Получаем координаты для всех 5 точек
            points = []
            for line_edit in [self.lineEdit_13, self.lineEdit_14,
                              self.lineEdit_15, self.lineEdit_16,
                              self.lineEdit_17]:  # Добавьте ваши QLineEdit для точек C, D, E
                if line_edit.text().strip():
                    coords = self.get_coordinates(line_edit.text(), '017c25cb-c2fe-43ef-b58e-e49320ff407e')
                    if coords:
                        points.append(coords)

            if len(points) < 2:
                raise Exception("Необходимо указать минимум 2 точки маршрута")

            size = "650,450"
            api_key = "08b76ad6-f685-4f52-b73d-ea6981593637"

            # Формируем часть URL с линией маршрута
            pl_part = f"&pl=c:8822DDC0,w:5,{','.join(points)}" if len(points) > 1 else ""

            # Формируем часть URL с метками точек
            pt_parts = []
            for i, point in enumerate(points):
                # Разные иконки для первой, последней и промежуточных точек
                if i == 0:
                    marker = "pm2rdm"  # Красная метка
                elif i == len(points) - 1:
                    marker = "pm2blm"  # Синяя метка
                else:
                    marker = "pm2grm"  # Зеленая метка для промежуточных точек
                pt_parts.append(f"{point},{marker}")

            pt_part = f"&pt={'~'.join(pt_parts)}"

            url = (
                f"https://static-maps.yandex.ru/v1?"
                f"size={size}"
                f"{pl_part}"  # Ломаная линия
                f"{pt_part}"  # Метки
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
        self.label_8.setText("hello")

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
            self.authorizationToDatabaseFromDispatcher()
            print(f'login: {u_login}')
            self.widget_3.setVisible(False)
            cursor.execute(""" SELECT COUNT(bus_id) FROM bus; """)
            self.label_8.setText("Всего автобусов в парке: " + str(cursor.fetchall()[0][0]))
            cursor.execute(""" SELECT COUNT(bus_id) FROM bus WHERE service <> true; """)
            self.label_9.setText("Исправных: " + str(cursor.fetchall()[0][0]))
            cursor.execute(""" SELECT COUNT(bus_id) FROM bus WHERE service <> false; """)
            self.label_10.setText("В ремонте: " + str(cursor.fetchall()[0][0]))
            cursor.close()
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

    def SendToService(self):
        vin = self.lineEdit_vin_find.text()
        cursor = conn.cursor()
        cursor.execute(""" UPDATE bus SET service = true WHERE vin = %s; """,
                       (vin, ))
        conn.commit()
        cursor.execute(""" SELECT COUNT(bus_id) FROM bus; """)
        self.label_8.setText("Всего автобусов в парке: " + str(cursor.fetchall()[0][0]))
        cursor.execute(""" SELECT COUNT(bus_id) FROM bus WHERE service <> true; """)
        self.label_9.setText("Исправных: " + str(cursor.fetchall()[0][0]))
        cursor.execute(""" SELECT COUNT(bus_id) FROM bus WHERE service <> false; """)
        self.label_10.setText("В ремонте: " + str(cursor.fetchall()[0][0]))
        cursor.close()

    def CreateRoute(self):
        name = self.lineEdit_7.text()
        #number = self.lineEdit_8.text()
        start = self.lineEdit_9.text()
        end = self.lineEdit_10.text()
        #distance = self.lineEdit_11.text()
        route_time = self.lineEdit_12.text()
        try:
            number = int(self.lineEdit_8.text())
            distance = int(self.lineEdit_11.text())
        except ValueError:
            QMessageBox.critical(self, "Ошибка", "Номер маршрута и расстояние должны быть числами")
            return
        print(f'{type(name)}\n{type(number)}\n{type(start)}\n{type(end)}\n{type(distance)}\n{type(route_time)}')
        cursor = conn.cursor()
        cursor.execute(" INSERT INTO route (route_name, route_number, route_start, route_finally, route_distance, route_time) VALUES (%s, %s, %s, %s, %s, %s) ",
                       (name, number, start, end, distance, route_time))

        conn.commit()
        cursor.close()
        QMessageBox.information(self, "Создание маршрута", "Маршрут успешно создан!")

    def CreateOrder(self):
        name = self.lineEdit.text()
        bus_number = int(self.lineEdit_2.text())
        route_time = self.lineEdit_3.text()
        cursor = conn.cursor()
        cursor.execute(" SELECT route_start FROM route WHERE route_name = %s ", (name, ))
        start = cursor.fetchall()[0][0]
        cursor.execute(" SELECT route_finally FROM route WHERE route_name = %s ", (name, ))
        final = cursor.fetchall()[0][0]
        cursor.execute(""" INSERT INTO orders (route_name, bus_number, route_start, route_finally, route_time) 
                            VALUES (%s, %s, %s, %s, %s) """,
                       (name, bus_number, start, final, route_time))
        conn.commit()
        cursor.close()
        QMessageBox.information(self, "Создание рейса", "Рейс успешно запланирован!")
        self.ShowAllOrders()

    def ShowAllOrders(self):
        cursor = conn.cursor()
        cursor.execute(""" SELECT route_name AS "Маршрут", bus_number AS "Номер автобуса", route_start AS "Пункт отправки", route_finally AS "Пункт прибытия", route_time AS "Время отправки" FROM orders; """)
        len_row = cursor.rowcount
        rows = cursor.fetchall()
        cols = cursor.description
        self.tableWidget_2.setColumnCount(len(cols))
        self.tableWidget_2.setRowCount(len_row)
        for i in range(len(cols)):
            self.tableWidget_2.setHorizontalHeaderItem(i, QTableWidgetItem(cols[i][0]))
        for i in range(len_row):
            for j in range(len(rows[i])):
                item = QTableWidgetItem(str(rows[i][j]))
                self.tableWidget_2.setItem(i, j, item)
        cursor.close()
    def ShowAllBuses(self):
        cursor = conn.cursor()
        cursor.execute(""" SELECT state_number AS "Гос.Номер", VIN, model as "Модель", year_of_release as "Год", odometer as "Пробег" FROM bus;  """)
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
