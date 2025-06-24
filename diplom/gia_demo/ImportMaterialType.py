import psycopg2
import pandas as pd

conn = psycopg2.connect(
    host = "localhost",
    database = "postgres",
    user = "postgres",
    password = "myhicursed",
    port = "5432"
)

cursor = conn.cursor()
df = pd.read_excel("Material_type_import.xlsx")
for _, row in df.iterrows():
    broken_str = row['Процент брака материала ']
    print(type(broken_str))
    #if(isinstance(broken_str, str)) and  '%' in broken_str:
    #    broken_str = broken_str.strip('%')
    #    broken_value = float(broken_str)
     #   print(broken_value)
    cursor.execute("""
        INSERT INTO material_type(material_type, material_broken) VALUES(%s, %s)
    """, (
        row['Тип материала'],
        round(broken_str * 100, 2)
    ))
conn.commit()
cursor.close()
conn.close()