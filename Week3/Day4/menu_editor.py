from menu_manager import MenuManager
from menu_item import MenuItem
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



def show_user_menu():
    while True:
        print("______Program Menu______")
        print("View an Item (V)")
        print("Add an Item (A)")
        print("Delete an Item (D)")
        print("Update an Item (U)")
        print("Show the Menu (S)")
        print("Exit (E)")

        choice = input("Please choose an option: ").strip().upper()

        if choice == 'V':
            view_item()  
        elif choice == 'A':
            add_item_to_menu()
        elif choice == 'D':
            remove_item_from_menu()
        elif choice == 'U':
            update_item_from_menu()
        elif choice == 'S':
            show_restaurant_menu()
        elif choice == 'E':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
        
def add_item_to_menu():
    name = input ("Enter the name of the item: ").strip()
    price = float(input("Enter the price of the item: ").strip())
    item = MenuItem(name=name, price=price)
    item.save()
def remove_item_from_menu():
    name = input ("Enter the name of the item: ").strip()
    item = MenuItem(name=name)
    item.delete()
def update_item_from_menu():
    name = input ("Enter the name of the item: ").strip()
    new_name = input ("Enter the new name of the item: ").strip()
    new_price = float(input("Enter the new price of the item: ").strip())
    item = MenuItem(name=name)
    item.update(new_name,new_price)
def show_restaurant_menu():
    items = MenuManager.all_items()
    for item in items:
        print(f"{item['name']}: {item['price']}")
def view_item():
    name = input("Enter the name of the item to view: ").strip()
    item = MenuManager.get_by_name(name)

if __name__ == "__main__":
    show_user_menu()


