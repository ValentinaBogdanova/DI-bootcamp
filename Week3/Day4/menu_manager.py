import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

DB_HOST = os.getenv('HOST')
DB_NAME = os.getenv('DATABASE')
DB_USER = os.getenv('USER')
DB_PASSWORD = os.getenv('PASSWORD')
DB_PORT = os.getenv('PORT')

connection = psycopg2.connect(
    database=DB_NAME,
    user=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    port=DB_PORT
)

cursor = connection.cursor()



class MenuManager:
     @classmethod
     def get_by_name(cls, name):
        name = name.lower()
        cursor.execute("select * from Menu_Items WHERE name = %s", (name,))
        result = cursor.fetchone()
        if result:
            return print("Item found:",{
                "id": result[0],
                "name": result[1],
                "price": result[2]
            })
        else:
         print("Item not found.")
     @classmethod
     def all_items(cls):
        cursor.execute("select * from Menu_Items")
        results = cursor.fetchall()
        items = []
        for row in results:
            items.append({
                "id": row[0],
                "name": row[1],
                "price": row[2]
            })
        return items
     
item = MenuManager.get_by_name('milkshake')

all_items = MenuManager.all_items()
print("All items:", all_items)

