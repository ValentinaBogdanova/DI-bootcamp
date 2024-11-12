# print('Hello World'))

# my_num = int(input("Gimme a number"))  #if an enter a letter i get ValueError

# Try and Except to handle

my_list = [2,3,1,2,"four",42,1,5,3,"imanumber"]
try:
    sum(my_list)
except:
    raise TypeError("There are strings in list")