# DAILY CHALLENGE

# Instructions :
# The goal is to create a class that represents a simple circle.
# A Circle can be defined by either specifying the radius or the diameter.
# The user can query the circle for either its radius or diameter.

# Other abilities of a Circle instance:

# Compute the circle’s area
# Print the attributes of the circle - use a dunder method
# Be able to add two circles together, and return a new circle with the new radius - use a dunder method
# Be able to compare two circles to see which is bigger, and return a Boolean - use a dunder method
# Be able to compare two circles and see if there are equal, and return a Boolean- use a dunder method
# Be able to put them in a list and sort them
# Bonus (not mandatory) : Install the Turtle module, and draw the sorted circles

import math
import turtle

class Circle:
    circles_list = []  # список в классе
    def __init__(self, radius):
        self.radius = radius
        self.__class__.circles_list.append(self)  # чобы сразу в список добавлял
    def area(self):
        area_cur = int(math.pi * self.radius ** 2)
        return area_cur
    def __repr__(self):
         return f'The circle with the radiuds {self.radius}'    
    def __add__(self, other):
        if isinstance(other, Circle):
            new_circle_r = self.radius + other.radius
            return Circle(new_circle_r)
        else:
            raise TypeError("Input information wrong, use numbers")
    def __lt__(self, other):
        if isinstance(other, Circle):
            return self.radius < other.radius
        return False
    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.radius == other.radius
        return False
    @classmethod                     # методы для класса добавить и отсортировать
    def add_to_list(cls, circle):
        cls.circles_list.append(circle)
    @classmethod
    def get_sorted_list(cls):
        return sorted(cls.circles_list)
    
        
radius_cir = Circle(int(input("Write a radius of the circle:  ")))
radius_cir2 = Circle(int(input("Write a radius of the circle:  ")))


print(radius_cir.area())
cir3 = radius_cir + radius_cir2
print(cir3)
print(radius_cir < radius_cir2)
print(radius_cir == radius_cir2)

circles_sorted = Circle.get_sorted_list()
print(circles_sorted)


#TURTLE
# def draw_circle(t, radius):
#         t.penup()
#         t.goto(0, -radius)  
#         t.pendown()
#         t.pensize(5) 
#         t.circle(radius)
        

# screen = turtle.Screen()
# screen.bgcolor("grey")
# t = turtle.Turtle()
# t.speed(10)

# draw_circle(t, radius_cir.radius)
# draw_circle(t, radius_cir2.radius)
# screen.exitonclick()
