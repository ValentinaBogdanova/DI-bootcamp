###### DICTIONARIES

# Keyvalue 

#DIFFERENCES BETWEEN LISRTS AND DICTIONARIES

# fruits= ['banana', 'apple', 'kiwi']
# print(fruits[1])


# user_info = ['Juliana', 'ju@gmail.com', 34, True, 1.59]

# user_info_dict = {'name':'Juliana',
#                   'email':'ju@gmail.com',
#                   'age':34,
#                   'is_male': False,
#                   'pets':['Caramelo', 'Nico', 'Floffy'],
#                   'family':[{'name':'Ariel',
#                             'age':5,
#                             'relation':'son'}],
#                     'hobbies':[('yoga', 3), ('tennis', 1), ('chess', 3)]
                            # }  #### в словари можно много что добавлянь, например словарь в словарь
# print(user_info_dict['name'])
# print(user_info_dict['pets'][1])  # так можно достать информацию из списка в словаре
# print(user_info_dict['family']['relation'])
# print(user_info_dict['hobbies'][2][1]) # достать в словаре из TUPLE  по индексу 


# for key in user_info_dict.keys():   #КАК ДОСТАТЬ КЛЮЧИ
#     print(key)

# dict_keys =[]
# for key in user_info_dict.keys():   #ДОБАВИТЬ КЛЮЧИ В СПИСОК(СОЗДАТЬ ЛИСТ)
#     dict_keys.append(key)


# for value in user_info_dict.values():  # достать значения
#     print(value)

# # CHANGING A VALUE
# user_info_dict['email'] = 'schmidt@gmail.com'  #изменить переменную по ключу
# print(user_info_dict)

# # ADDING A VALUE
# user_info_dict['profession']= 'Web developer teacher'  
# print(user_info_dict)

# # DELETE A KEY VALUE PAIR (AN ENTRY) OF THE DIRECT
# del user_info_dict['profession']

#CHECKING IF A KEY EXIST 

# print('pets' in user_info_dict.keys()) # проверить есть ли ключ

# print("Juliana" in user_info_dict.values()) # проверить есть ли паременная

# UPDATE ( ) merge dicts or update an entry

# user_info_dict['family'].append({'name':'DANIEL',
#                                  'age':35,
#                                  'relation':'brother'})
# print(user_info_dict)

# #EX
# sample_dict = { 
#    "class":{ 
#       "student":{ 
#          "name":"Mike",
#          "marks":{ 
#             "physics":70,
#             "history":80
#          }
#       }
#    }
# }
# print(sample_dict['class']['student']['marks']['history'])  #как достать информацию  пошагово



# user_name = input('whats your name?')
# user_email = input('your email:')

# user_dict = {
#     'Name':user_name,
#     'email':user_email        #KEYWORD может быть также переменной !!!
#     }
# print(user_dict)


# ДОБАВЛЕНИЕ ИНФОРМАЦИИ через создание нового словаря

# user_info2= {'origin':'Brazil',
#              'nickname': 'ju05',
#              'phone_num':'05558846'}

# user_info_dict.update(user_info2)
# print(user_info_dict)








#ADVANCED KISR DICTIONARIES
#FOR LOOP 

my_book={
    "title":"Harry Potter",
    "author":"JK Rowling"
}

for key, value in my_book.items():
    print(f'The key is {key} and value is {value}')
#_________

#range () and enumerate()

# range JUST numbers
#enumerate work with string
#Функция range() создает последовательность чисел и возвращает объект range.
#  Ее часто используют в циклах for для повторения 
# определенного количества раз. range() принимает параметры:

#Функция enumerate() применяется для перебора элементов последовательности 
# (например, списка) и возвращает кортеж, содержащий индекс элемента и сам элемент. 
# Это удобно, если нужно одновременно получить и индекс, и значение.

odd_list=list(range(1,20,2))
print(list)


even_num=[]
for i in range(1,20):
    if i %2 ==0:
        even_num.append(i)
print(even_num)

students = ["John", "Anna", "Cathe", "Lucy"]

for index, name in enumerate(students):
    print(index,name)

students[1]='Maria'

for index, name in enumerate(students):
    students[index]= f'Hello{name}'

print(students)

# students[1]='Maria'

for each_student in students:
    if each_student == "Hello Cathe":
        continue
    else:
        print(f'{each_student}, how are you')

#pass
if students[0]is 'Hello Harry':
    pass #a developer keyword to help to structure the code
else:
    print("Not Harry")





# sample_dict = {
#   "name": "Kelly",
#   "age":25,
#   "salary": 8000,
#   "city": "New york"

# }
# keys_to_remove = ["name", "salary"]

# del sample_dict['name']
# del sample_dict['salary']
# print(sample_dict)


#__________
#ZIP

# list1 = [1,2,3]
# list2 = ['a','b','c']
# list4 = [1.1, 2.2, 3.3, 4.4, 5.5]
# list3= list(zip(list1,list2))
# print(list3)







# for item in zip(list1, list2, list3): # only go as far it is possible
#     print(item)
# >>
# (1, 'a', 1.1)
# (2, 'b', 2.2)
# (3, 'c', 3.3)



# list1=[1,2,3,4]
# list2=['a','b','c','d']
# list3=[1.1, 2.2, 3.3, 4.4]

### print(zip(list1,list2, list3)) так не получится

# print(list(zip(list1,list2, list3)))    
###print(dict(zip(list1,list2, list3))) #чтобы чделать слооооварь


#break --- остановись
#continue ----
#pass-----


#while True   #instead of___ WHILE <condition>:___
# можно использовать например если условие еще не прописано и переменная не указана
# total_fem=[]
# while True:
#     family_member = input('Give me the age, type "quit" when finish')
#     if family_member =='quit':
#         break
#     total_fem.append(family_member)
# print(total_fem)

#COMPREHENSIVE list   обычно используется с циклом for
even_num=[]
# for i in range(1,20):
#     if i %2 ==0:
#         even_num.append(i)
# print(even_num)

even_num = [i for i in range(1,20) if i%2 ==0]
print(even_num)

even_num =tuple((i for i in range(1,20) if i%2 ==0))
print(type(even_num))   #можно и с set и tuple использовать

