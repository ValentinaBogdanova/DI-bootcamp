class Animal():
    def __init__(self, number_legs, sound, type = None):
        self.type = type
        self.number_legs = number_legs
        self.sound = sound

    def make_sound(self):
        print(f"I am an animal, and I love saying {self.sound}")

class Canine(Animal):
    def __init__(self, number_legs, sound, color):
        super().__init__(number_legs, sound, "Canine")  #можно писать Animal. вместо super  # что забрать от родителя супер -функция
        self.is_color = color
    def fetch_ball(self):
        if self.is_trained:
            print("I am fetching balls vecause I am dog")
        else:
            print("The dog is not trained")