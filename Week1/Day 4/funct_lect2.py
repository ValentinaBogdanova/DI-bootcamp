students=['Lean','Luke','Darth Veider']

def welcome():
    for name in students:
        print(f'Welcome {name}')

welcome()
print(students)


def welcome():
    for index, name in enumerate(students):
        students[index] = f'Welcome {name}'

welcome()
print(students)


# *ARGS AND ** KWARGS ( кварги - сложная дата типо словарей)

def my_pets(*args):   #*ARG can be NOTHING - 0 # если мы не знаем сколько аргументов будетб *- говорит о том что аргументов может бысть сколько угодно
    total_pets = len(args)
    return total_pets
print(my_pets("cat","dog","fish","cat","dog","fish"))

#  **KWARGS (cREATING A DICTIONARY) KeyWordARGuments
#ДЕЛАЕТ СЛОВАРЬ
def user_info(**kwargs):
    print(kwargs)

user_info(name="Valentina", age = '30', telephone='054526890')



# def user_info(**kwargs):
#     for keyword in kwargs.keys():
#         if keyword 
#     print(kwargs)

# user_info(name="Valentina", age = '30', telephone='054526890')

    