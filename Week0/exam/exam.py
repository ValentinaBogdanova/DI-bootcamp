from utils import unzip_with_7z

zip_file_path ='C:/Users/Acer/Desktop/Учеба/Python/exam/congrats.7z' # keep as is
dest_path = '.' # keep as is

find_me = '' # 2 letters are missing!
secret_password = find_me + 'bcmpda' 
import os
os.chdir("C:/Users/Acer/Desktop/Учеба/Python/exam")

import string
def hack_password():
    known_password = 'bcmpda'
    letters = string.ascii_lowercase + string.ascii_uppercase
    for letter_1 in letters:
        for letter_2 in letters:
            password1=letter_1+letter_2+known_password
            print(f'Trying pass:{password1}')
            if unzip_with_7z(zip_file_path,dest_path,password1):
                return password1
    return None
password=hack_password()
if password:
    print(f"True:{password}")
else:
    print(f"False")
