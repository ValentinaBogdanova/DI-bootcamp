#EXERCISE 1 #Using the input function, ask the user for a string. The string must be 10 characters long.
# If it’s less than 10 characters, print a message which states “string not long enough”.
# If it’s more than 10 characters, print a message which states “string too long”.
# If it’s 10 characters, print a message which states “perfect string” and continue the exercise.

user_string =input("Please, write a string")
if len(user_string) > 10:
    print("This string is too long")
elif len(user_string) == 10:
    print("This string is perfect!")
else:
    print("this string is not long enough")


#EXERCISE 2
#Then, print the first and last characters of the given text

# user_ent="HelloWorld"
# print(user_ent[0])
# print(user_ent[-1:])


#EXERCISE 3
#Using a for loop, construct the string character by character: Print the first character, then the second, then the third, until the full string is printed. For example:

# first_greet=input("write a spell")   #for example "Alohomora" or "Avada Kedavra" :)
# for i in range(len(first_greet)):
#     print(first_greet[:i +1])

#BONUS EX Swap some characters around then print the newly jumbled string (hint: look into the shuffle method). 

# import random
# phrase=input("write any word")
# abrakadabra=list(phrase)
# random.shuffle(abrakadabra)
# abrakadabra=''.join(abrakadabra)
# print(abrakadabra)


