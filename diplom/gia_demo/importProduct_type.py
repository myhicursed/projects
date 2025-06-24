import psycopg2
import pandas as pd

conn = psycopg2.connect(
    host = 'localhost',
    database = 'postgres',
    user = 'postgres',
    password = 'myhicursed',
    port = '5432'
)

df = pd.read_excel('Product_type_import.xlsx')

cursor = conn.cursor()
for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO product_type(product_name, product_k) VALUES(%s, %s)
    """, (
        row['Тип продукции'],
        row['Коэффициент типа продукции']
    ))
conn.commit()
cursor.close()
conn.close()