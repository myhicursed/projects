import sys
import psycopg2
import requests
from PyQt5.QtCore import pyqtSignal
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsPixmapItem, QMessageBox
from PyQt5.QtWidgets import QTableWidgetItem
from design import Ui_MainWindow
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from datetime import datetime
from bot import BusBot
import threading
from collections import Counter
#import datetime




class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    send_tg_id_signal = pyqtSignal(str, str)
    def __init__(self):
        super().__init__()
        self.setupUi(self)


        self.bot = BusBot()
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
        self.pushButton_10.clicked.connect(self.SendSelectedId)

        self.bot.message_signal.connect(self.update_label_from_bot)
        self.bot.message_route_name_signal.connect(self.update_route_from_bot)
        self.bot.message_end_route_signal.connect(self.endRoute)
        self.bot.message_check_repair_signal.connect(self.SendMessageRepair)

        self.send_tg_id_signal.connect(self.bot.Accept)

        #########################################################################
        threading.Thread(target=self.bot.run, daemon=True).start()

        self.map_scene = QGraphicsScene()
        self.graphicsView.setScene(self.map_scene)  # Используем уже созданный graphicsView


        # Первая загрузка карты
        #self.load_static_map()


        ########################################################
        #БАЗОВЫЕ НАСТРОЙКИ ОТОБРАЖЕНИЯ
        self.tableWidget_3.setColumnCount(4)
        self.tableWidget_3.setHorizontalHeaderLabels(["Имя", "Гос.номер", "Время", "Ситуация"])
        self.widtegBus.setVisible(False)
        self.widgetRoutes.setVisible(False)
        self.widget_5.setVisible(False)
        self.widget_4.setVisible(False)
        self.widget_8.setVisible(False)
        self.widget_9.setVisible(False)
        self.pushButton_8.setVisible(False)
        today = datetime.today()
        self.label_5.setText(f"Сегодня: {today.strftime('%d.%m.%Y')}")
        #######################################################

    def LoadDriversToComboBox(self):
        cursor = conn.cursor()
        cursor.execute(" SELECT drivers_fio, telegram_id FROM drivers ")
        rows = cursor.fetchall()
        self.comboBox.clear()

        for fio, tg_id in rows:
            self.comboBox.addItem(fio, tg_id)

    def GetSelectedTgId(self, comboBox):
        index = comboBox.currentIndex()
        if index >= 0:
            return comboBox.itemData(index)
        return None

    def SendSelectedId(self):
        tg_id = self.GetSelectedTgId(self.comboBox)
        msg = self.lineEdit_4.text()
        if tg_id:
            print(f'Отправляется tg_id: {tg_id}')
        self.send_tg_id_signal.emit(tg_id, msg)



    def SendMessageRepair(self, tgid, number):
        row_position = self.tableWidget_3.rowCount()
        self.tableWidget_3.insertRow(row_position)
        time_str = datetime.now().strftime("%H:%M:%S")
        cursor = conn.cursor()
        cursor.execute(" SELECT drivers_fio FROM drivers WHERE telegram_id = %s ", (str(tgid),))
        mn = cursor.fetchall()[0][0]
        self.tableWidget_3.setItem(row_position, 0, QTableWidgetItem(mn))
        self.tableWidget_3.setItem(row_position, 1, QTableWidgetItem(number))
        self.tableWidget_3.setItem(row_position, 2, QTableWidgetItem(time_str))
        self.tableWidget_3.setItem(row_position, 3, QTableWidgetItem("Поломка"))
        cursor.close()

    def endRoute(self, tgid, number):
        row_position = self.tableWidget_3.rowCount()
        self.tableWidget_3.insertRow(row_position)
        time_str = datetime.now().strftime("%H:%M:%S")
        cursor = conn.cursor()
        cursor.execute(" SELECT drivers_fio FROM drivers WHERE telegram_id = %s ", (str(tgid),))
        mn = cursor.fetchall()[0][0]
        self.tableWidget_3.setItem(row_position, 0, QTableWidgetItem(mn))
        self.tableWidget_3.setItem(row_position, 1, QTableWidgetItem(number))
        self.tableWidget_3.setItem(row_position, 2, QTableWidgetItem(time_str))
        self.tableWidget_3.setItem(row_position, 3, QTableWidgetItem("Завершил смену"))
        cursor.close()

    def update_route_from_bot(self, tgid, number):
        row_position = self.tableWidget_3.rowCount()
        self.tableWidget_3.insertRow(row_position)
        time_str = datetime.now().strftime("%H:%M:%S")
        cursor = conn.cursor()
        cursor.execute(" SELECT drivers_fio FROM drivers WHERE telegram_id = %s ", (str(tgid),))
        mn = cursor.fetchall()[0][0]
        self.tableWidget_3.setItem(row_position, 0, QTableWidgetItem(mn))
        self.tableWidget_3.setItem(row_position, 1, QTableWidgetItem(number))
        self.tableWidget_3.setItem(row_position, 2, QTableWidgetItem(time_str))
        self.tableWidget_3.setItem(row_position, 3, QTableWidgetItem("Начал смену"))
        cursor.close()

    def update_label_from_bot(self, tgid, text):
        row_position = self.tableWidget_3.rowCount()
        self.tableWidget_3.insertRow(row_position)
        time_str = datetime.now().strftime("%H:%M:%S")
        cursor = conn.cursor()
        cursor.execute(" SELECT drivers_fio FROM drivers WHERE telegram_id = %s ", (str(tgid),))
        mn = cursor.fetchall()[0][0]
        self.tableWidget_3.setItem(row_position, 0, QTableWidgetItem(mn))
        self.tableWidget_3.setItem(row_position, 1, QTableWidgetItem(text))
        self.tableWidget_3.setItem(row_position, 2, QTableWidgetItem(time_str))
        self.tableWidget_3.setItem(row_position, 3, QTableWidgetItem("ДТП"))

        cursor.execute(""" INSERT INTO logs(logs_time, logs_status, logs_number)
                           VALUES(%s, %s, %s) """, 
                           (time_str, "ДТП", text))
        conn.commit()
        cursor.close()

    def setup_chart(self):
        """График соотношения исправных и сломанных автобусов"""

        # Очистка виджета
        for child in self.widget_6.children():
            child.deleteLater()

        # Создание layout
        new_layout = QtWidgets.QVBoxLayout(self.widget_6)
        new_layout.setContentsMargins(0, 0, 0, 0)

        # Создание графика
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)
        new_layout.addWidget(self.canvas)

        # Данные (в реальности — получи из БД)
        cursor = conn.cursor()
        cursor.execute(" SELECT COUNT(bus_id) FROM bus ")
        working = cursor.fetchall()[0][0]
        cursor.execute(" SELECT COUNT(bus_id) FROM bus WHERE service = 'true' ")
        broken = cursor.fetchall()[0][0]

        labels = ['Исправные', 'Сломанные']
        sizes = [working, broken]
        colors = ['#4CAF50', '#F44336']  # зелёный и красный

        self.ax.clear()  # очищаем ось (если график перерисовывается)
        self.ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=colors)
        self.ax.axis('equal')  # чтобы круг не был эллипсом
        self.canvas.draw()

    from datetime import datetime
    from collections import Counter
    from PyQt5 import QtWidgets
    from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
    import matplotlib.pyplot as plt

    def setup_chart_2(self):
        """График динамики старения автопарка (распределение автобусов по годам выпуска)"""

        # Очистка предыдущих виджетов
        for child in self.widget_7.children():
            child.deleteLater()

        # Создание нового layout
        new_layout = QtWidgets.QVBoxLayout(self.widget_7)
        new_layout.setContentsMargins(0, 0, 0, 0)

        # Получение данных из базы
        cursor = conn.cursor()
        cursor.execute("SELECT year_of_release FROM bus")
        results = cursor.fetchall()

        years = []
        for row in results:
            date_str = row[0]
            try:
                if date_str:
                    # Преобразуем строку в дату, формат: DD-MM-YYYY
                    date_obj = datetime.strptime(date_str.strip(), "%d-%m-%Y")
                    years.append(date_obj.year)
            except Exception as e:
                print(f"Ошибка обработки даты '{date_str}': {e}")
                continue

        if not years:
            label = QtWidgets.QLabel("Нет корректных дат для построения графика")
            new_layout.addWidget(label)
            return

        # Подсчет количества автобусов по годам
        total = len(years)
        count_by_year = Counter(years)
        sorted_years = sorted(count_by_year.items())
        labels = [str(year) for year, _ in sorted_years]
        sizes = [count / total * 100 for _, count in sorted_years]

        # Построение графика
        figure2, ax2 = plt.subplots()
        canvas2 = FigureCanvas(figure2)
        new_layout.addWidget(canvas2)

        ax2.bar(labels, sizes, color='#2196F3')
        ax2.set_ylabel("Процент автобусов")
        ax2.set_xlabel("Год выпуска")
        ax2.set_title("Динамика старения автопарка")
        canvas2.draw()

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
            self.LoadDriversToComboBox()
            self.setup_chart()
            self.setup_chart_2()
            cursor.close()
        else:
            print('Неверный логин/пароль')

    def AddNewBus(self):
        number = self.lineEdit_state_number.text()
        vin = self.lineEdit_vin.text()
        model = self.lineEdit_bus_model.text()
        year = self.lineEdit_bus_year.text()
        odometer = self.lineEdit_odometer.text()
        odometer = int(odometer)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO bus (state_number, VIN, model, year_of_release, odometer) VALUES (%s, %s, %s, %s, %s)",
                       (number, vin, model, year, odometer))
        conn.commit()
        cursor.execute(""" SELECT COUNT(bus_id) FROM bus; """)
        self.label_8.setText("Всего автобусов в парке: " + str(cursor.fetchall()[0][0]))
        cursor.execute(""" SELECT COUNT(bus_id) FROM bus WHERE service <> true; """)
        self.label_9.setText("Исправных: " + str(cursor.fetchall()[0][0]))
        cursor.execute(""" SELECT COUNT(bus_id) FROM bus WHERE service <> false; """)
        self.label_10.setText("В ремонте: " + str(cursor.fetchall()[0][0]))
        cursor.close()
        self.widget_9.setVisible(False)
        QMessageBox.information(self, "Регистрация автобуса", "Автобус успешно зарегистрирован в базе")

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
        self.pushButton_8.setVisible(True)

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
        QMessageBox.information(self, "Подтверждение отправки", "Автобус отправлен на ТО")

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
    window.setWindowTitle("Автобусный парк")
    window.show()
    sys.exit(app.exec_())
