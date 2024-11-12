#OOP

#How to creatw a class

# class Dog():  #заведено что название классов с большой буквы
#     pass      #Если скобки пустые их можно не печать вообще

# #How to creatr an instance (object) of the new class we created

# shelter_dog = Dog()
# #print(type(shelter_dor))

# shelter_dog.name= "Rex" # pption 1 creating an atributes to an object
# print(shelter_dog.name)


# IN IT method
class Dog():    #е забывать про отступы
    def __init__(self):   # self - это отношение к обьекту
        print('The object was created')

shelter_dog = Dog()
puddle = Dog()

# class Dog():    #е забывать про отступы
#     def __init__(self,name,color,age): 
#         self.name = name
#         self.color = color
#         self.age = age

# shelter_dog = Dog("Rex", "black",7)
# puddle = Dog("Flufy", "white", 3)
# print(shelter_dog.name)
# print(puddle.name)


# class Person():
#     def __init__(self,name,age,group):
#         self.name= name
#         self.age = age
#         self.group = group
# my_person = Person("Valentina", 29, "Data Analytics")

# print(my_person.name, my_person.age, my_person.group)
# print(my_person) # так не получится
# print(my_person.__dict__) #creating dict
# #how to change an atribute after creating
# my_person.age += 1


# METHODS   (это функция внутри класса)
class Dog():    
    def __init__(self,name,color,age): 
        self.name = name
        self.color = color
        self.age = age

    def bark(self):
        print(f"{self.name} is barking")

    def walk(self, num_meters):
        return f'{self.name} walked {num_meters} meters today' #meters это информация внешняя тут self е нужно
    def rename(self, new_name):
        self.name = new_name

shelter_dog = Dog("Rex", "black",7)
puddle = Dog("Flufy", "white", 3)
print(shelter_dog.name)
print(puddle.name)
# shelter_dog.bark()

#call method brk gor class 
# exemple dell_computer.description("Mark")

Dog.bark(puddle) # метод вызова функции через класс и обьект

# print(puddle.walk(300))



#created a method called presentation

# class Person():
#     def __init__(self,name,age,group):
#         self.name= name
#         self.age = age
#         self.group = group
#     def presentation(self):
#         print(f"Hello, I am {self.name}, and I am {self.age} years old")
# my_person = Person("Valentina", 30, "Data Analytics")
# my_person.presentation()


# class Computer():

#     def description(self, name):
#         """
#         This is a totally useless function
#         """
#         print("I am a computer, my name is", name)
#         #Analyse the line below
#         print(self)

# mac_computer = Computer()
# mac_computer.brand = "Apple"
# print(mac_computer.brand)

# dell_computer = Computer()

# # Computer.description(dell_computer, "Mark")
# # IS THE SAME AS:
# dell_computer.description("Mark")