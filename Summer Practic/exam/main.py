import psycopg2
from tabulate import tabulate


class DataBase:
    def __init__(self):
        try:
            self.conn = psycopg2.connect(
                host='localhost',
                database='production_control',
                user='postgres',
                password='123',
                port='5432'
            )
            print("Успешное подключение к базе данных!")
        except psycopg2.Error as e:
            print(f"Ошибка подключения: {e}")
            self.conn = None

    def show_materials(self):
        if self.conn is None:
            print("Нет подключения.")
            return

        cur = self.conn.cursor()
        cur.execute("SELECT * FROM materials")
        rows = cur.fetchall()
        if not rows:
            print("Таблица материалы пуста")
            cur.close()
            return

        columns = []
        for desc in cur.description:
            columns.append(desc[0])

        print("\nСодержимое таблицы материалы:")
        print(tabulate(rows, headers=columns, tablefmt="grid"))
        cur.close()

    def add_material(self):
        print("\nДобавление нового материала:")
        name = input("Название материала: ")
        supplier = input("Поставщик: ")
        stock = float(input("Текущий запас: "))
        min_stock = float(input("Минимальный запас: "))
        cost = float(input("Цена за единицу: "))

        cur = self.conn.cursor()
        try:
            cur.execute("""
                INSERT INTO materials 
                (material_name, supplier, current_stock, min_stock_level, cost_per_unit)
                VALUES (%s, %s, %s, %s, %s)
            """, (name, supplier, stock, min_stock, cost))
            self.conn.commit()
            print("Материал успешно добавлен!")
        except psycopg2.Error as e:
            print(f"Ошибка при добавлении: {e}")
        cur.close()

    def delete_material(self):
        self.show_materials()
        material_id = input("\nВведите ID материала для удаления: ")

        cur = self.conn.cursor()
        try:
            cur.execute("DELETE FROM materials WHERE material_id = %s", (material_id,))
            if cur.rowcount > 0:
                self.conn.commit()
                print(f"Материал с ID {material_id} удален")
            else:
                print("Материал с таким ID не найден")
        except psycopg2.Error as e:
            print(f"Ошибка при удалении: {e}")
        cur.close()

    def show_products(self):
        if self.conn is None:
            print("Нет подключения.")
            return

        cur = self.conn.cursor()
        cur.execute("SELECT * FROM products")
        rows = cur.fetchall()
        if not rows:
            print("Таблица products пуста")
            cur.close()
            return

        columns = []
        for desc in cur.description:
            columns.append(desc[0])

        print("\nСодержимое таблицы products:")
        print(tabulate(rows, headers=columns, tablefmt="grid"))
        cur.close()

    def add_product(self):
        print("\nДобавление нового продукта:")
        name = input("Название продукта: ")
        stock_cost = float(input("Себестоимость: "))
        selling_price = float(input("Цена продажи: "))

        cur = self.conn.cursor()
        try:
            cur.execute("""
                INSERT INTO products 
                (product_name, stock_cost, selling_price)
                VALUES (%s, %s, %s)
            """, (name, stock_cost, selling_price))
            self.conn.commit()
            print("Продукт успешно добавлен!")
        except psycopg2.Error as e:
            print(f"Ошибка при добавлении: {e}")
        cur.close()

    def delete_product(self):
        self.show_products()
        product_id = input("\nВведите ID продукта для удаления: ")
