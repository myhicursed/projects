import psycopg2
import pandas as pd

conn = psycopg2.connect(
    host = 'localhost',
    database = 'postgres',
    user = 'postgres',
    password = 'myhicursed',
    port = '5432'
)

df = pd.read_excel("Partner_products_import.xlsx")

cursor = conn.cursor()
for _, row in df.iterrows():
    current = row['Дата продажи']
    current = current.strftime('%d.%m.%Y')
    cursor.execute("""
        INSERT INTO partner_products(products, partner_name, products_amount, date_resale) VALUES(%s, %s, %s, %s)
    """, (
        row['Продукция'],
        row['Наименование партнера'],
        row['Количество продукции'],
        current
    ))

conn.commit()
cursor.close()
conn.close()