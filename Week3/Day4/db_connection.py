import psycopg2
import requests
import json
import random


####psycopg2
connection = psycopg2.connect(database = 'countries',
                              user = 'postgres',
                              password = '1994',
                              host='localhost',
                              port='5432')

cursor = connection.cursor()
cursor.execute('DROP TABLE IF EXISTS random_countries')

create_table_query = f'''CREATE TABLE random_countries (
                        id SERIAL PRIMARY KEY,
                        name VARCHAR(100) NOT NULL,
                        capital VARCHAR(100) NOT NULL,
                        flag_code VARCHAR(100),
                        population INTEGER,
                        subregion VARCHAR(100) )'''

cursor.execute(create_table_query)
connection.commit()

countries_api = requests.get('https://restcountries.com/v3.1/all')
data = countries_api.json()
# print(data[0])  # Impostant check the type of data you will get from the api

for i in range(10):    #or for_in 
    index =random.randint(0, len(data) -1)
    try:
        name = data[index]['name']['official']

        name =name.replace('\'', '`')
        capital = data[index].get('capital', [None])[0]
        flag_code = data[index].get('flag')
        subregion = data[index].get('subregion')
        population = data[index].get('population', 0)

        query = f'''INSERT INTO random_countries (name, capital, flag_code, population, subregion)
        VALUES ('{name}', '{capital}', '{flag_code}', '{population}', '{subregion}')'''      # or like that %s, %s, %s, %s, %s
        cursor.execute(query)
        connection.commit()
    except Exception as e:
        print(f'Error processing country at index {index}: {e}')
print('Sucessefully added to db ')
