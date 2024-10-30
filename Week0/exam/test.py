import os

# Проверка, существует ли файл congrats.7z в текущей директории
zip_file_path = 'congrats.7z'
if os.path.exists(zip_file_path):
    print(f"Файл {zip_file_path} найден.")
else:
    print(f"Файл {zip_file_path} не найден. Проверьте путь и имя файла.")

# Вывод текущей рабочей директории
print("Текущая рабочая директория:", os.getcwd())