#lambda functions : don't have name and we don't have name and we dont need to call them
# we create them  and excute them on place

#sintax:
# to_power = lambda n, power: n ** power

# print(to_power(4,2))

# # map() = get another function argument
# #filter()
# #reduce()

# numbers =[1,2,3,4,5,6,7]
# squared_numder = map(lambda n: n**2, numbers) # map позволяет применять функцию ко всем элементам
# # map(function, iterable)
# #map позволяет избежать цикла for
# print(list(squared_numder))

#squared_numder = map(lambda n: n**2, numbers) # number здесь  sequence


# IN CONTEX: APPLYING TO A DATA SET 


#filter - фильтер данных

#reduce - нужно импортировать 

people = ["Rick", "Morty", "Beth", "Jerry", "Snowball"]
filt_people =list(filter(lambda n: len(n) <= 4, people))
print(filt_people)
hello_say =list(map(lambda n: f'hello, {n}' , filt_people))
print(hello_say)