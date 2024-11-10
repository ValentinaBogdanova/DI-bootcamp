# DAILY CHALLENGE

#print(macdonald.get_info())

class Farm:
    def __init__(self, zoo_name):
        self.animal = {}
        self.zoo=zoo_name
    def add_animal(self, animal, amount=1):
        animal = str(animal)
        if animal in self.animal:
            self.animal[animal] += amount
        else:
            self.animal[animal] = amount
    def show_animals(self):
        result = ""
        for animal, count in self.animal.items():
            print(f"{animal} : {count}")
    def get_animal_types(self):
        animals_types=[]
        for types in self.animal.keys():
            animals_types.append(types)
        return sorted(animals_types)
    def get_info(self):
        print(f'{self.zoo}`s farm')
        print()
        self.show_animals()  #there is also "None" output in the end (dont know how to fix it)
    def get_short_info(self):
        animal_types = self.get_animal_types()
        print(f"McDonald’s farm has {animal_types[0]}s, {animal_types[1]}s and {animal_types[2]}")

macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)

print(macdonald.get_info())
print(macdonald.get_animal_types())
macdonald.get_short_info()