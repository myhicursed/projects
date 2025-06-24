import psycopg2
import pandas as pd

conn = psycopg2.connect(
    host = 'localhost',
    database = 'postgres',
    user = 'postgres',
    password = 'myhicursed',
    port = '5432'
)

df = pd.read_excel('Products_import.xlsx')
cursor = conn.cursor()
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO products(products_type, products_name, product_articul, products_price)
        VALUES(%s, %s, %s, %s)
    """, (
        row['Тип продукции'],
        row['Наименование продукции'],
        row['Артикул'],
        row['Минимальная стоимость для партнера']
    ))
conn.commit()
cursor.close()
conn.close()
