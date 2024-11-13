# from datetime import date

# # class Person:
# #     def __init__(self, name, birthday):
# #         self.name = name
# #         self.birthday = birthday

# #     def lived_days(self):
# #         return(date.today() - self.birthday).days
# #     @property
# #     def birthday(self):
# #         return(self._birthday)
# #     @birthday.setter  #изменить
# #     def birthday(self, value):
# #         if not isinstance(value, date):
# #             raise ValueError("")
# #         self._birthday = value



# # p1= Person("Jack", date(1999, 12, 3))  
# # p2= Person("Ann", "03/08/1999")
# # print(p1.birthday)
# # print(p1.lived_days())

# # print(p2.lived_days())

# from datetime import date

# class Person:
#     def __init__(self, name, birthday):
#         self.name = name
#         self.birthdayirthday = birthday

#     @property #getter
#     def birthday(self):
#         return self._birthday

#     @birthday.setter #setter
#     def birthday(self, value):
#         if not isinstance(value, date):
#             raise ValueError('birthday argument has to be a datetime object date(year, month, day)')
#         self._birthday = value
#         return self

#     @property
#     def name(self):
#         self._name = self._name.tittle()
#         return
    
#     @name.setter
#     def name(self, value):
#         self._name = value.tittle()  #???????
#         return self

#     def lived_days(self):
#         return(date.today() - self.birthday).days



# # p1 = Person('john doe', date(1999,5,5))
# # print(type(p1.name)) #title()

# # create a getter and a setter for the attribute name:
# # using @property define that the name will always be printed with capital letter, even if when creating the object it was passed with lower case
# # create the setter that will allow this property to be changed

# p2 =Person('maria gonzales', date(1990,5,6))
# print(p2.name)