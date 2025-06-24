import pandas as pd
import psycopg2

df = pd.read_excel("Partners_import.xlsx")

try:
    conn = psycopg2.connect(
        host = "localhost",
        database = "postgres",
        user = "postgres",
        password = "myhicursed",
        port = "5432"
    )
except Exception as e:
    print(f'Не удалось подключиться к БД{e}')

cursor = conn.cursor()

for _, row in df.iterrows():
    cursor.execute("""
        INSERT INTO partners(partner_type, partner_name, director, email, telephone,
            adress, inn, rate) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (
        row['Тип партнера'],
        row['Наименование партнера'],
        row['Директор'],
        row['Электронная почта партнера'],
        row['Телефон партнера'],
        row['Юридический адрес партнера'],
        row['ИНН'],
        row['Рейтинг']
    ))
conn.commit()
cursor.close()
conn.close()



