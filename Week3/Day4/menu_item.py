import psycopg2
from dotenv import load_dotenv
import os



load_dotenv()
print(os.getcwd())

DB_HOST = os.getenv('HOST')
DB_NAME = os.getenv('DATABASE')
DB_USER = os.getenv('USER')
DB_PASSWORD = os.getenv('PASSWORD')
DS_PORT = os.getenv('PORT')

# print(f"HOST: {os.getenv('HOST')}")
# print(f"DATABASE: {os.getenv('DATABASE')}")
# print(f"USER: {os.getenv('USER')}")
# print(f"PASSWORD: {os.getenv('PASSWORD')}")
# print(f"PORT: {os.getenv('PORT')}")

connection = psycopg2.connect(database = DB_NAME,
                              user = DB_USER ,
                              password = DB_PASSWORD,
                              host = DB_HOST,
                              port = DS_PORT)

cursor = connection.cursor()
#cursor.execute('DROP TABLE IF EXISTS random_countries')
#commit
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Menu_Items (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        price SMALLINT DEFAULT 0
    )
''')
connection.commit()
class MenuItem:
    def __init__(self, name, price = 0):
        self.name = name.lower()
        self.price = price

    def save(self):
            cursor.execute(
                "SELECT * FROM Menu_Items WHERE name = %s",
                (self.name,)
            )
            existing_item = cursor.fetchone()
            if existing_item:
                 print(f"Item '{self.name}' already exists!")
            else:
                query = "INSERT INTO Menu_Items (name, price) VALUES (%s, %s)"  
                cursor.execute(query, (self.name, self.price))
                connection.commit()
            print(f"Item '{self.name}' added successfully!")
    def delete(self):
         query = "DELETE FROM Menu_Items WHERE name = %s AND price = %s"  
         cursor.execute(query, (self.name, self.price))
         connection.commit()
         print(f"Item '{self.name}' deleted successfully!")
    def update (self, new_name, new_price):
         new_name = new_name.lower()
         query = "UPDATE Menu_Items SET name = %s, price = %s WHERE name = %s"  
         cursor.execute(query, (new_name, new_price, self.name))
         connection.commit()
         print(f"Item '{self.name}' updated to '{new_name}' with price '{new_price}' successfully!")




Hamburger = MenuItem(name='Hamburger', price=50)
# Pizza = MenuItem(name='Pizza', price=40)
# Milkshake = MenuItem(name='Milkshake', price=20)
# Hamburger.save()
# Pizza.save()
# Milkshake.save()
Hamburger.update(new_name = 'King cheeseburger', new_price = 70)
# Hamburger.delete()