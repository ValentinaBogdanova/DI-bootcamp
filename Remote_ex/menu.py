import psycopg2

HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = '1994'
DATABASE = 'Restaurant'

class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def save(self):
        try:
            # Подключение к PostgreSQL
            connection = psycopg2.connect(
                dbname=DATABASE,
                user=USERNAME,
                password=PASSWORD,
                host=HOSTNAME
            )
            cursor = connection.cursor()

            # Создание таблицы, если она не существует
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS Menu_Items (
                    item_id SERIAL PRIMARY KEY,
                    item_name VARCHAR(100) NOT NULL,
                    item_price NUMERIC(10, 2) DEFAULT 0
                )
            ''')

            # Вставка нового элемента
            cursor.execute(
                "INSERT INTO Menu_Items (item_name, item_price) VALUES (%s, %s)",
                (self.name, self.price)
            )

            connection.commit()
            print(f"Item '{self.name}' saved successfully!")
        except Exception as e:
            print("Error saving item:", e)
        finally:
            # Закрываем соединение
            cursor.close()
            connection.close()

    def delete(self):
        try:
            connection = psycopg2.connect(
                dbname=DATABASE,
                user=USERNAME,
                password=PASSWORD,
                host=HOSTNAME
            )
            cursor = connection.cursor()

            # Удаление элемента по имени
            cursor.execute(
                "DELETE FROM Menu_Items WHERE item_name = %s",
                (self.name,)
            )

            connection.commit()
            print(f"Item '{self.name}' deleted successfully!")
        except Exception as e:
            print("Error deleting item:", e)
        finally:
            cursor.close()
            connection.close()

    def update(self, new_name, new_price):
        try:
            connection = psycopg2.connect(
                dbname=DATABASE,
                user=USERNAME,
                password=PASSWORD,
                host=HOSTNAME
            )
            cursor = connection.cursor()

            # Обновление элемента
            cursor.execute(
                "UPDATE Menu_Items SET item_name = %s, item_price = %s WHERE item_name = %s",
                (new_name, new_price, self.name)
            )

            connection.commit()
            print(f"Item '{self.name}' updated successfully to '{new_name}' with new price '{new_price}'!")
        except Exception as e:
            print("Error updating item:", e)
        finally:
            cursor.close()
            connection.close()

# Пример использования
item = MenuItem('Shawarma', 45)
item.save()  # Сохранение нового элемента
item.update('Big Shawarma', 55)  # Обновление элемента
item.delete() 



        #     if existing_item:
        #         print(f"Item '{self.name}' already exists in the menu!")
        #     else:
        #         # Вставка нового элемента
        #         self.cursor.execute(
        #             "INSERT INTO Menu_Items (item_name, item_price) VALUES (%s, %s)",
        #             (self.name, self.price)
        #         )
        #         self.connection.commit()
        #         print(f"Item '{self.name}' saved successfully!")
        # except Exception as e:
        #     print("Error saving item:", e)

    # def delete(self):
    #     try:
    #         query = 'INSERT INTO...'
    #         # Удаление элемента по имени
    #         self.cursor.execute(
    #             "DELETE FROM Menu_Items WHERE item_name = %s",
    #             (self.name,)
    #         )
    #         self.connection.commit()
    #         print(f"Item '{self.name}' deleted successfully!")
    #     except Exception as e:
    #         print("Error deleting item:", e)

    # def update(self, new_name, new_price):
    #     try:
    #         query = 'INSERT INTO...'
    #         # Обновление элемента
    #         self.cursor.execute(
    #             "UPDATE Menu_Items SET item_name = %s, item_price = %s WHERE item_name = %s",
    #             (new_name, new_price, self.name)
    #         )
    #         self.connection.commit()
    #         print(f"Item '{self.name}' updated successfully to '{new_name}' with new price '{new_price}'!")
    #     except Exception as e:
    #         print("Error updating item:", e)





    # def remove_duplicates(self):
    #     try:
    #         # Используем CTE для идентификации дубликатов
    #         self.cursor.execute('''
    #             WITH CTE AS (
    #                 SELECT 
    #                     item_id,
    #                     ROW_NUMBER() OVER (PARTITION BY item_name, item_price ORDER BY item_id) AS rn
    #                 FROM Menu_Items
    #             )
    #             DELETE FROM Menu_Items
    #             WHERE item_id IN (
    #                 SELECT item_id
    #                 FROM CTE
    #                 WHERE rn > 1
    #             );
    #         ''')
    #         self.connection.commit()
    #         print("Duplicates removed successfully!")
    #     except Exception as e:
    #         print("Error removing duplicates:", e)

    # @staticmethod
    # def display_menu():
    #     """Метод для отображения всех элементов меню"""
    #     try:
    #         connection = psycopg2.connect(
    #             dbname=DATABASE,
    #             user=USERNAME,
    #             password=PASSWORD,
    #             host=HOSTNAME
    #         )
    #         cursor = connection.cursor()

    #         cursor.execute("SELECT item_name, item_price FROM Menu_Items")
    #         items = cursor.fetchall()

    #         if items:
    #             print("Current Menu Items:")
    #             for item in items:
    #                 print(f"- {item[0]}: {item[1]} USD")
    #         else:
    #             print("The menu is empty!")

    #         cursor.close()
    #         connection.close()
    #     except Exception as e:
    #         print("Error displaying menu:", e)

    # def close_connection(self):
    #     """Метод для закрытия соединения"""
    #     try:
    #         self.cursor.close()
    #         self.connection.close()
    #         print("Connection closed successfully!")
    #     except Exception as e:
    #         print("Error closing connection:", e)    

# Пример использования
# item = MenuItem('Shawarma', 45)
# item.save()  # Сохранение нового элемента
# item.update('Big Shawarma', 55)  # Обновление элемента
# item.delete() 
# item = MenuItem('Shakhuka', 30)
# item.save() 
# item = MenuItem('Humus', 35)
# item.save() 
# MenuItem.display_menu()
# menu = MenuItem()

# # Удаляем дубликаты
# menu.remove_duplicates()