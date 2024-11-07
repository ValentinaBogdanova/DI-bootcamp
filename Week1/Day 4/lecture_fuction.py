# #FUNCTION

# #syntax

# def say_hello():
#     print('Hello Python')

# # calling the function
# say_hello()
# #_________________________#


# # ARGUMENT 

# def say_hello(greeting):
#     print(f'{greeting} Python')

# # calling the function
# say_hello("Hello")




# def say_hello(greeting):
#     print(f'{greeting} Python')  #snoud be sertain type of data

# # calling the function
# say_hello("Hello")

# #________________________________

# def say_hello(greeting):
#     name= input("Whats your name")
#     print(greeting, name)  # outside the function you can not acsess variasble
# # calling the function
# say_hello("Hello")


# def say_hello(name,language):
#     if language == "HE":
#         print(f'Shalom, {name}')
#     elif language == "PT":
#         print(f'Ola, {name}')
#     elif language == "RU":
#         print(f'Privet, {name}')  
#     else:
#         print(f"{language} is not supported")
# say_hello("Ari", 'RU')

# #KEY WORD ARGUMENT
# say_hello(language="RU",name="Ron")
# say_hello(name = "Vic") ### НЕ ПОНЯЛА


# LOCAP AND GLOBAL SCOPE

def say_hello(greeting):
    name=input("Whats u name")
    print(greeting,name)
#print (name) in tje global scope
global_var=100
def calculation(a,b):
    global global_var #GLOBAL отсылка к переменной вне функц
    addition= a+b
    substraction = a-b
    global_var += addition
    print(f'addition = {addition}\n substration={substraction}')
    print(global_var)

calculation(5,7)

#returning_value


def calculation(a,b):
    addition= a+b
    substraction = a-b
    
    print(f'addition = {addition}\n substration={substraction}')
    return(addition, substraction)
    
addition, substraction=calculation(12,10)  # NONETYPE # assign variable!!
total_val=0

def increase_total(addition,total_val,substraction):   #использование больше двух переменных
    result1 = total_val + addition
    result2=total_val-substraction
    return(result1,result2)

print(increase_total(addition,total_val,substraction)) #TO SEE FINAL RESULT
