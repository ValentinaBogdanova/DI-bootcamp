some_variable="Valentina"
print(type(some_variable)) #Так можно узнать тип переменной. Внизу неск примеров
my_number=4.6
my_bool = False
print(type(my_number))
print(type(my_bool))

#STRINGS
greetings="Shabat Shalom"
#index is a location where variable is
#indexing of string
print(greetings[3])
#slicing a string
print(greetings[2:4]) #Разрезание строки по индексу буквы, индексы начинаются с 0 
print(greetings[2:5])
print(greetings[2:]) # в этом варианте до конса отрежет
print(greetings[2::])


#strings most usrd method
print(len(greetings)) #Пишет длину строки
print(greetings[2:len(greetings)]) #Чтобы отрезать до коца можно использовать такой метод
# Пробелы и знаки препинания учитываются
phrase = "Hello, world!"
print(len(phrase))  # Вывод: 13

# Строка с несколькими пробелами
phrase_with_spaces = "   Hello   "
print(len(phrase_with_spaces))  # Вывод: 11
# Пустая строка
empty_string = ""
print(len(empty_string))  # Вывод: 0

print('index of space', greetings.index("S"))

#string method
#-1 for last index for any string
print(greetings[2:-1])
print("***", greetings[2:-1]) # "***" удобно если что то в терминале надо увидеть

print('hello'.capitalize()) # Метод чтобы озаглавить фразу, 
#НЕ ЗАБЫВАТЬ круглые скобки 
print(greetings.title()) #все слова с большой буквы

print(greetings.replace("Shalom", "meburach")) # Замена чего то в строки, например слова на другое
# первое пишем слово которое меняем, второе на которое

print(greetings.replace("Shalom", "meburach").title()) # и озаглавить

greetings=greetings.replace("Shalom", "meburach").title()
print(greetings)
# Если надо заменить значение переменной на новое , через = , если новая переменная пишем новую

#greetings = greetings.replace("/n", "") # метод позволяющий заменить что то неудобное (мешающее например для анализа) на пустое место


student = " Harry Potter $"
student = student.strip() #убрать пробелы
print(student + " " + greetings) # соединить строчки
student = student.strip("$") #strip убирает только в начале или в конце строки
print(student)
text = "   Python   "
print(text.lstrip())  # Удаляет только начальные пробелы: "Python   "
print(text.rstrip())  # Удаляет только конечные пробелы: "   Python"

student.replace("r","l")
print(student.replace("r","l"))


#NUMBERS: integer, float, comple numbers , boolean (1-true, 0-false)
int_integ = 5
float_num = 6.9

#operation
print(type(float_num))
print(-6+49)
print(8-(-7))
print(10*3)
print(5**2)
print(greetings * 10) # string 10 times
#/n на строка на новой строчке #/t добавляет пробелы
print(greetings * 10)

print(round(5/3,4))
print(11//2) # разделит БЕЗ остатка чтобы был integer (float devisiom)
print(11%2)
print(1625%5)

if 12%3 == 0:
    print('yes')
my_age = 30
my_age1=my_age+123879
print(my_age1)

print(type(my_age))
my_age=str(my_age)
print(type(my_age)) #смена типа переменный с цифры на строку

#my_phone = "0556754789"
#my_phone = int(my_phone)
#print(type(my_phone))
#my_age = input('what is your age?') # спрашивает у пользователя
print(my_age)


#my_age = int(input('what is your age?'))
#if my_age < 18:
#    print('you can\'t dring vodka') # можно использовать \t чтобы программа не опращала внимание на апостроф
#else:
#    print("Uhuuu let's selebrate")

# COMPARISON OPERATOR
print(5 <= 7)
print(5 == 5)
print (40<30)
#print('3'>3) # give error

f_name = 'Hermione'
l_name = 'Granger'
print('Hello,' + f_name + " " +l_name +", welcome to Hogwart!")
# f string  чтоб побыстрее и логичнее писать
print(f"Hello, {f_name} {l_name}, welcome to Hogwarts!")
hermione_age = 15
print(f'Hello, {f_name}, your age is {hermione_age}')
first_name="Valentina"
second_name="Bogdanova"
print(f'Hello, my name is {first_name} {second_name}, i want to Horwarts too!')

# comparison as words
print("python" is "python")
print("python" is not "python")
print("HTML" is not "CSS" and "python" is "python")
print("HTML" is not "CSS" and "python" is "JAVA")
# Очень ВАЖНО при работе с if statements!!!
if "HTML" is not "CSS":
    print('That\'s right!')

    # JS - CAMEL CASE
    #myAge = 34 # JS way - NOT PYTHON!
    #JS - let, const, var = keywords to define if the variable should be change
    #PYTHON = Uppercase
    PASSWORD = '123456'
    my_age = 30
    my_age += 1
    # print(my_age)

    # print(f'Hello, your age is {my_age}')   #### ЧТОБЫ ЗАКОММЕНТИРОВАТЬ НАДО НАЖАТЬ
    # КОНТРЛ + СЛЕШ 
# function input ПРОСИТ ПОЛЬЗОВАТЕЛЯ ВВЕСТИ информацию

#id #condition TRUE code ll work

age =
