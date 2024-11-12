# OOP - Obj orient Programming

# object = instance
# attributes = characteristics
# parameters = argumens (what we raise Exception("Blocked Door cannet be open") when creating ah instance of a class)
# example:

# class Zoo:
#     def __init__(self, zoo_name):   #zoo_name - atribute
#         self.zoo_name = zoo_name #this is both : an parameter and attribute
#         self.animals = [] # this just an attribute


# method = function (but when it is part of a class) 
# __init__ = method который иницирует присутствие
# Inheritance =
# Polymorphysem =
# Encapsulation = 

# class Grandpa:
#     def speak(self):
#         print("Grandpa is speaking")
#     def sleep(self):
#         print("Grandpa is sleeping")

# class Parent(Grandpa):
#     def speak(self):
#         print("Parent is speaking")

# class Child(Parent):
#     raise Exception("Blocked Door cannet be open")

# obj1 = Parent()
# obj1.speak()

# obj2 = Child()
# obj2.speak()


### Multipal Inheritance Class grandpa

# class Grandpa:
#     def speak(self):
#         print("Grandpa is speaking")
#     def sleep(self):
#         print("Grandpa is sleeping")

# class Parent(Grandpa):
#     def speak(self):
#         print("Parent is speaking")

# class Parent2(Grandpa):       #второй родитель
#     def speak(self):
#         print("Parent2 is speaking")
#     def eat(self):
#         print("Parent2 is eating")
# class Child(Parent, Parent2):
#     raise Exception("Blocked Door cannet be open")

# # obj1 = Parent()
# # obj1.speak()

# obj2 = Child()
# obj2.speak()
# obj2.eat()

# class Circle:
#     color = "red"

# class NewCircle(Circle):
#     color = "blue"

# nc = NewCircle
# print(nc.color)
# # >> What will be the output ? blue

# class Circle:
#     def __init__(self, diameter):
#       self.diameter = diameter

#     def grow(self, factor=2):
#         """grows the circle's diameter by factor"""
#         self.diameter = self.diameter * factor   #diameter*2

# class NewCircle(Circle):
#     def grow(self, factor=2):
#         """grows the area by factor..."""
#         self.diameter = (self.diameter * factor * 2)  # *4



# nc = NewCircle(1)
# print(nc.diameter)   #1

# nc.grow()   #4

# print(nc.diameter)
# # >> What will be the output

#the super function

# class Animal():
#     def __init__(self, number_legs, sound, type = None):
#         self.type = type
#         self.number_legs = number_legs
#         self.sound = sound

#     def make_sound(self):
#         print(f"I am an animal, and I love saying {self.sound}")
# class Canine(Animal):
#     def __init__(self, number_legs, sound, color):
#         super().__init__(number_legs, sound, "Canine")  #можно писать Animal. вместо super  # что забрать от родителя супер -функция
#         self.is_color = color
#     def fetch_ball(self):
#         if self.is_trained:
#             print("I am fetching balls vecause I am dog")
#         else:
#             print("The dog is not trained")

# class Dog(Animal, Canine):
#     def __init__(self, number_legs, sound, is_trained, color):
#         super().__init__(number_legs, sound, "dog")  #можно писать Animal. вместо super  # что забрать от родителя супер -функция
#         Canine.__init__(self, color)
#         self.is_trained = is_trained
#     def fetch_ball(self):
#         if self.is_trained:
#             print("I am a dog, and I love fetching balls")
#         else:
#             print("The dog is not trained")

#     def barking(self):
#         super(Dog, self).make_sound()  #вызов родительской функции через super


# animal1 = Animal("dog", 4, "Woouaf")
# dog1 = Dog(4, "Woolf", True)
# dog2 = Dog(4, "Woolf", False)
# dog1.fetch_ball()
# dog2.fetch_ball()
# dog1.barking()

#Polymorphism =  using the same name method in the Parent claaa
# and Child Class but changing the output to each one of them

#Inheritance = suing attributes and methods 

#Encapsulation = python convention to securife 

# class _BankAccount:
#     def __init__(self, owner_name, number, balance = 0):
#         self.__owner_name = owner_name #__private (должно быть темного)
#         self.number = number
#         self.transaction = []
#         self._balance = balance #_protected
    
#     def show_balance(self):
#         print(f"Your balance is {self._balance}")

#     def deposit(self, amount):
#         self._balance += amount
#         self.show_balance()
#         #add transaction track code
#         self.transaction.append(f"deposit transaction: {amount}")
#         return self # отсылка к my_account #self.balance - если делать так то
        
#     def withdraw(self, amount):
#         if amount < self._balance:
#             self._balance -= amount
#             self.show_balance()
#             self.transaction.append(f"withdraw transaction: {- amount}")
#         else:
#             print("Your balance is minus")
#         return self
#     def show_trans(self):
#         for i,track in enumerate(self.transaction):
#             print(f"transaction {i+1}: {track}")
#         return self.show_balance

# my_account = _BankAccount("Valentina Bogdanova", 156, 100)
# # print(my_account.balance)
# my_account.deposit(120).withdraw(25).deposit(200).withdraw(20).withdraw(140)
# # print(my_account.balance)
# my_account.show_trans()
# my_account.withdraw(500)

# print(my_account._balance)
# # print(my_account.__owner_name)
# print(my_account._BankAccount__owner_name) # достать прайвит информацию

# class Door:
#     def __init__(self,is_opened = True):
#         self.is_opened = is_opened
#     def open_door(self):
#         if self.is_opened:
#             print("The dor is already open")
#         else:
#             print("The dor is now open")
#     def close_door(self):
#         if not self.is_opened:
#             print("The dor was closed")
#         else:
#             print("The dor is now closed")
#             self.is_opened = False
        
# class BlockedDoor(Door):
#     def open_door(self):
#         raise Exception("Blocked Door cannet be open")
#     def close_door(self):
#         raise Exception("Blocked Door cannot be closed")

# door1 = Door()
# door2 = BlockedDoor()
# door1.close_door()
# print(door1.is_opened)
# door2.close_door()

