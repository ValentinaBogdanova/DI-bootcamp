#Exercise 1 : Pets
# Create another cat breed named Siamese which inherits from the Cat class.
# Create a list called all_cats, which holds three cat instances : one Bengal, one Chartreux and one Siamese.
# Those three cats are Sara’s pets. Create a variable called sara_pets which value is an instance of the Pet class, and pass the variable all_cats to the new instance.
# Take all the cats for a walk, use the walk method.

#CODE


# class Pets():
#     def __init__(self, animals):
#         self.animals = animals

#     def walk(self):
#         for animal in self.animals:
#             print(animal.walk())

# class Cat():
#     is_lazy = True
#     all_cats = []                    #creating an empty list of cats
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         Cat.all_cats.append(self)      #adding each cat to a list
#     def walk(self):
#         return f'{self.name} is just walking around'

# class Bengal(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# class Chartreux(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'
    
# class Siamese(Cat):
#     def sing(self, sounds):
#         return f'{sounds}'

# bengal_cat = Bengal("Demon", 2)
# chartreux_cat = Chartreux("Queen", 5)
# siamese_cat = Siamese("Sheron", 9)
# sara_pets = Pets(Cat.all_cats)

# sara_pets.walk()

#EX 2 Dogs
# Create a class called Dog with the following attributes name, age, weight.
# Implement the following methods in the Dog class:
# bark: returns a string which states: “<dog_name> is barking”.
# run_speed: returns the dogs running speed (weight/age*10).
# fight : takes a parameter which value is another Dog instance, called other_dog. This method returns a string stating which dog won the fight. The winner should be the dog with the higher run_speed x weight.

# Create 3 dogs and run them through your class.


# CODE

# class Dog:
#     def __init__(self, name, age, weight):
#         self.name = name
#         self.age = age
#         self.weight = weight
#     def bark(self):
#         print(f"{self.name} is barking!")
#     def run_speed(self):
#         speed = self.weight // self.age * 2 
#         print(f"{self.name}`s speed is {speed}")
#         return speed
#     def fight(self, other_dog):
#         dog_power = self.run_speed() * self.weight
#         other_dog_power = other_dog.run_speed() * other_dog.weight
#         if dog_power > other_dog_power:
#             return f'{self.name} wins the fight!'
#         elif dog_power < other_dog_power:
#             return f'{other_dog.name} wins the fight!'
#         else:
#             return "It's a tie!"
        

# dog1 = Dog("Patrik", 5, 30)
# dog2 = Dog("Luna", 2, 17)
# dog3 = Dog("Charli", 3, 32)
# dog_fight=dog1.fight(dog3)
# print(dog_fight)


# EX 4 FAMILY
# Instructions
# Create a class called Family and implement the following attributes:

# members: list of dictionaries
# last_name : (string)

# Implement the following methods:

# born: adds a child to the members list (use **kwargs), don’t forget to print a message congratulating the family.
# is_18: takes the name of a family member as a parameter and returns True if they are over 18 and False if not.
# family_presentation: a method that prints the family’s last name and all the members’ details.

# Create an instance of the Family class, with the last name of your choice, and the below members. Then call all the methods you created in Point 2.

#     [
#         {'name':'Michael','age':35,'gender':'Male','is_child':False},
#         {'name':'Sarah','age':32,'gender':'Female','is_child':False}
#     ]


#CODE

# class Family:
#     def __init__(self, members = None, last_name =""):
#         if members is None:
#             members = []
#         self.members = members
#         self.last_name = last_name
#     def born(self, **kwargs):
#         self.members.append(kwargs)
#         print(f"Conrats with new member in {self.last_name} family!")
#     def is_18(self, name):
#         for member in self.members:
#             if member["name"] == name:
#                 if member["age"] >= 18:
#                     print(f"{member["name"]} is an aduld")   
#                 else:
#                     print(f"{member["name"]} is a child")   
#     def family_presentation(self):
#         print(f"Family:  {self.last_name}")
#         print()
#         for member in self.members:
#             print(f"Name: {member['name']}, Age: {member['age']}, Gender: {member['gender']}, is_child: {member['is_child']}")


# members = [
#         {'name':'Michael','age':35,'gender':'Male','is_child':False},
#         {'name':'Sarah','age':32,'gender':'Female','is_child':False}
#          ]
# potter_family = Family(members, "Potter")

# potter_family.family_presentation()
# potter_family.born(**{'name':'Kevin', 'age':1, 'gender':'Male','is_child': True})
# potter_family.family_presentation()

# potter_family.is_18("Kevin")


#EX 5 Super Family    (THAT WAS VEEEEEEERRY HARD ONE )
'''
Create a class called TheIncredibles. This class should inherit from the Family class:
This is no random family they are an incredible family, therefore the members attributes, will be a list of dictionaries containing the additional keys : power and incredible_name. (See Point 4)
Add a method called use_power, this method should print the power of a member only if they are over 18 years old. If not raise an exception (look up exceptions) which stated they are not over 18 years old.
Add a method called incredible_presentation which :
Print a sentence like “*Here is our powerful family **”
Prints the family’s last name and all the members’ details (ie. use the super() function, to call the family_presentation method)
Call the incredible_presentation method.
Use the born method inherited from the Family class to add Baby Jack with the following power: “Unknown Power”.
Call the incredible_presentation method again.
'''

 
# class TheIncredibles(Family):
#     def __init__(self, members=None, last_name="", power=None, incredible_name=None):
#         super().__init__(members, last_name)
#         self.power = power
#         self.incredible_name = incredible_name
#     def use_power(self, name):
#             for member in self.members:
#                 if member["name"] == name:
#                     try:
#                         if member["age"] >= 18:
#                             print(f"{member['name']} is using {member['power']}")   
#                         else:
#                             print(f"{member['name']} is too young to use power.")
#                     except TypeError:
#                         print(f"{member['name']} is't found.")

#     def incredible_presentation(self):
#         print(f"**Here is our powerful family**")
#         for member in self.members:
#             presentation = f"Name: {member['name']}, Age: {member['age']}, Gender: {member['gender']}, is_child: {member['is_child']}"
#             if 'power' in member and 'incredible_name' in member:
#                 presentation += f", power: {member['power']}, incredible_name: {member['incredible_name']}"
#             print(presentation)

#     def super_born(self, name, incredible_name, power, **kwargs): 
#         super().born(name=name, **kwargs)
#         for member in self.members:
#             if member["name"] == name:
#                 member["power"] = power
#                 member["incredible_name"] = incredible_name

# members = [
#         {'name':'Michael','age':35,'gender':'Male','is_child':False,'power': 'fly','incredible_name':'Mike Fly'},
#         {'name':'Sarah','age':32,'gender':'Female','is_child':False,'power': 'read minds','incredible_name':'Super Woman'}
#             ]

# incredibles_family = TheIncredibles(members, "Incredibles")            
# incredibles_family.use_power("Michael")
# incredibles_family.super_born(name='Jack', age=0, gender='Male', is_child=True, incredible_name= "Baby Jack", power='Unknown Power')
# incredibles_family.incredible_presentation()
