import psycopg2
from tabulate import tabulate


class DataBase:
    def __init__(self):
        try:
            self.conn = psycopg2.connect(
                host='localhost',
                database='postgres',
                user='postgres',
                password='myhicursed',
                port='5432'
            )
        except:
            print('Не удалось установить соединение')

    def showAllFromConsumer(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM consumers")
        rows = cursor.fetchall()
        columns = []
        for i in cursor.description:
            column = i[0]
            columns.append(column)

        print(tabulate(rows, headers=columns, tablefmt="grid"))
        cursor.close()

    def showAllFromDevice(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM device")
        rows = cursor.fetchall()
        columns = []
        for i in cursor.description:
            column = i[0]
            columns.append(column)
        print(tabulate(rows, headers=columns, tablefmt="grid"))
        cursor.close()

    def showWaterObject(self):
        cursor = self.conn.cursor()
        cursor.execute("""SELECT object, model, meter_type
                          FROM consumers
                          JOIN device ON consumer_id = object_id_fk
                          WHERE meter_type = 'вода'
                          ORDER BY date_install;
                       """)
        rows = cursor.fetchall()
        columns = []
        for i in cursor.description:
            column = i[0]
            columns.append(column)
        print(tabulate(rows, headers=columns, tablefmt="grid"))
        cursor.close()

    def InsertFromConsumer(self, u_object, u_address, u_object_type, u_contact, u_phone):
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO consumers (object, address, object_type, contact, phone) VALUES (%s, %s, %s, %s, %s)",
            (u_object, u_address, u_object_type, u_contact, u_phone))
        self.conn.commit()
        cursor.close()

    def __del__(self):
        self.conn.close()

def main():
    db = DataBase()

    while True:
        print('1. чтобы вывести всех потребителей')
        print('2. чтобы вывести все приборы')
        print('3. Вывести все объекты, которые подключены к воде')
        print('4. Добавить данные')
        print('5. Выход')

        select = input('Выбор: ')

        if select == '1':
            db.showAllFromConsumer()
        elif select == '2':
            db.showAllFromDevice()
        elif select == '3':
            db.showWaterObject()
        elif select == '4':
            text1 = input('Объект: ')
            text2 = input('Адрес: ')
            text3 = input('Тип объекта: ')
            text4 = input('Ответственное лицо: ')
            text5 = input('Телефон: ')
            db.InsertFromConsumer(text1, text2, text3, text4, text5)
            print('Данные успешно добавлены')
        elif select == '5':
            break
        else:
            print("Некорректный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()