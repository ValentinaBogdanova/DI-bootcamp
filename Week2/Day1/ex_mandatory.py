# EX 1
#Instantiate three Cat objects using the code provided above.
# Outside of the class, create a function that finds the oldest cat and returns the cat.
# Print the following string: “The oldest cat is <cat_name>, and is <cat_age> years old.”. Use the function previously created.

# class Cat:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# def oldest(cats):
#     oldest_cat = cats[0]
#     for cat in cats:
#         if cat.age > oldest_cat.age:
#             oldest_cat = cat
#     return oldest_cat

# maincoon_cat = Cat("Fedor",3)
# scotland_cat = Cat("Charles", 12)
# bengal_cat = Cat("Demon", 1)
# cats_list=[maincoon_cat, scotland_cat, bengal_cat]
# oldest_cat = oldest(cats_list)
# print(f'The oldest cat is {oldest_cat.name}, who is {oldest_cat.age}')


# EX 2 
#Create a class called Dog.
#In this class, create an __init__ method that takes two parameters : name and height. This function instantiates two attributes, which values are the parameters.
#Create a method called bark that prints the following string “<dog_name> goes woof!”
#Create a method called jump that prints the following string “<dog_name> jumps <x> cm high!”. x is the height*2.


# class Dog:
#     def __init__(self, name, height):
#         self.name = name
#         self.height = height
#     def bark(self):
#         print(f"{self.name} goes woof!")
#     def jump(self):
#         hight_jump = self.height*2
#         print(f"{self.name} jumps {hight_jump} cm high!")


#Outside of the class, create an object called davids_dog. His dog’s name is “Rex” and his height is 50cm.

# davids_dog = Dog("Rex", 50)

#Print the details of his dog (ie. name and height) and call the methods bark and jump.


# print(davids_dog.name)
# print(davids_dog.height)
# davids_dog.bark()
# davids_dog.jump()

# Create an object called sarahs_dog. Her dog’s name is “Teacup” and his height is 20cm.
# Print the details of her dog (ie. name and height) and call the methods bark and jump

# sarahs_dog = Dog("Teacup", 20)
# print(sarahs_dog.name)
# print(sarahs_dog.height)
# sarahs_dog.bark()
# sarahs_dog.jump()

#Create an if statement outside of the class to check which dog is bigger. Print the name of the bigger dog.

# if davids_dog.height > sarahs_dog.height:
#     print(davids_dog.name)
# else:
#     print(sarahs_dog.name)


#EX 3 Who’s the song producer?
#Define a class called Song, it will show the lyrics of a song.
#Its __init__() method should have two arguments: self and lyrics (a list).
#Inside your class create a method called sing_me_a_song that prints each element of lyrics on its own line.

#CODE

# class Song:
#     def __init__(self, lyrics):
#         self.lyrics= lyrics
#     def sing_me_a_song(self):
#         print("\n".join(self.lyrics))
              
# stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
# stairway.sing_me_a_song()



#EX 4 Afternoon at the Zoo
# Create a class called Zoo.
# In this class create a method __init__ that takes one parameter: zoo_name.
# It instantiates two attributes: animals (an empty list) and name (name of the zoo).
# Create a method called add_animal that takes one parameter new_animal. This method adds the new_animal to the animals list as long as it isn’t already in the list.
# Create a method called get_animals that prints all the animals of the zoo.
# Create a method called sell_animal that takes one parameter animal_sold. This method removes the animal from the list and of course the animal needs to exist in the list.

#These two parts i am not able to do (tried different ways and asked chat GPT, it's method doesnt work too)
# Create a method called sort_animals that sorts the animals alphabetically and groups them together based on their first letter.
# Create a method called get_groups that prints the animal/animals inside each group.

# Create an object called ramat_gan_safari and call all the methods.
# Tip: The zookeeper is the one who will use this class.


#CODE

# class Zoo:
#     def __init__(self,zoo_name):
#         self.animals = []
#         self.zoo_name = zoo_name
#     def add_animal(self,new_animal):
#         if new_animal not in self.animals:
#             self.animals.append(new_animal)
#         return self.animals
#     def get_animals(self):
#         print(self.animals)
#     def sell_animal(self, animal_sold):
#             if animal_sold in self.animals:
#                 self.animals.remove(animal_sold)
#             else:
#                 print(f"{animal_sold} is not in the Zoo")

    
             
# zoo = Zoo("Ramat Gan Safari")
# zoo.add_animal("Zebra")
# zoo.add_animal("Leon")
# zoo.add_animal("Lama")
# zoo.add_animal("Hipo")
# zoo.get_animals()
# zoo.sell_animal("Owl")












#####################################################

#var not worked

# def sort_animals(self):
#          sorted_animals = sorted(self.animals)
#          dict_group = {}
#          first_letter = ''
#          group_num = 1
#          sorted_group = []
#          for animal in sorted_animals:
#              if  animal[0] != first_letter:
#                  if sorted_group:
#                      self.animals[group_num] = sorted_group
#                      group_num += 1
#                  sorted_group = [animal]
#                  first_letter = animal[0]
#              else:
#                  sorted_group.append(animal)
#          if sorted_group:
#              dict_group[group_num] = sorted_group
#              self.animals = 

#var 2 (not worked)

    # def sort_animals(self):
    #      sorted_animals = sorted(self.animals)
    #      dict_group = {}
    #      group_num = 1
    #      for animal in sorted_animals:
    #         first_letter = animal[0]
    #         if first_letter not in dict_group:
    #                  dict_group[first_letter] = []
    #         dict_group[first_letter].append(animal)
            
    #         return self.animals

    # def groups(self):
    #     for group_num, animals in self.animals.items():
    #         print(f"Group {group_num}: {animals}")
