import psycopg2
from tabulate import tabulate




def autorization():
    try:
        global conn
        conn = psycopg2.connect(
            host='localhost',
            database='postgres',
            user='postgres',
            password='myhicursed',
            port='5432'
        )
    except:
        print('Не удалось установить соединение')


def showAllFromConsumer():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM consumers")
    rows = cursor.fetchall()
    columns = []
    for desc in cursor.description:
        column_name = desc[0]
        columns.append(column_name)

    print(tabulate(rows, headers=columns, tablefmt="grid"))

    cursor.close()

def showAllFromDevice():
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM device")
    rows = cursor.fetchall()
    columns = []
    for desc in cursor.description:
        column_name = desc[0]
        columns.append(column_name)
    print(tabulate(rows, headers=columns, tablefmt="grid"))
    cursor.close()
def showWaterObject():
    cursor = conn.cursor()
    cursor.execute("""SELECT object, model, meter_type
                      FROM consumers
                      JOIN device  ON consumer_id = object_id_fk
                      WHERE meter_type = 'вода'
                      ORDER BY date_install;
                   """)
    rows = cursor.fetchall()
    columns = []
    for desc in cursor.description:
        column_name = desc[0]
        columns.append(column_name)
    print(tabulate(rows, headers=columns, tablefmt="grid"))
    cursor.close()

def InsertFromConsumer(u_object, u_address, u_object_type, u_contact, u_phone):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO consumers (object, address, object_type, contact, phone) VALUES (%s, %s, %s, %s, %s)",
                   (u_object, u_address, u_object_type, u_contact, u_phone, ))

    conn.commit()
    cursor.close()


autorization()
while True:
    print('1. чтобы вывести всех потребителей')
    print('2. чтобы вывести все приборы')
    print('3. Вывести все объекты, которые подключены к воде')
    print('4. Добавить данные')
    print('5.Выход')

    select = input('Выбор: ')

    if select  == '1':
        showAllFromConsumer()
    if select == '2':
        showAllFromDevice()
    if select == '3':
        showWaterObject()
    if select == '4':
        text1 = input('Объект: ')
        text2 = input('Адрес: ')
        text3 = input('Тип объекта')
        text4 = input('Ответственное лицо')
        text5 = input('Телефон')
        InsertFromConsumer(text1, text2, text3, text4, text5)
        print('Данные успешно добавлены')
    if select == '5':
        break





