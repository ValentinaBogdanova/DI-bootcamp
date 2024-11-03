#EX 1 Print the following output in one line of code:
# print("Hello world " * 4)

#EX 2 Write code that calculates the result of: (99^3)*8 (meaning 99 to the power of 3, times 8).
# x=(99**3)*8
# print(x) #7762392

#EX 3 Predict the output of the following code snippets:
#5 < 3 #False
# 3 == 3 #True
# 3 == "3" #False
# "3" > 3 #Error
# "Hello" == "hello" #False

#EX 4 Create a variable called computer_brand which value is the brand name of your computer.

#Using the computer_brand variable print a sentence that states the following: "I have a <computer_brand> computer".
# computer_brand="Acer"
# print(f'I have an {computer_brand} computer')

#EX 5
# Create a variable called name, and set it’s value to your name.
# Create a variable called age, and set it’s value to your age.
# Create a variable called shoe_size, and set it’s value to your shoe size.
# Create a variable called info and set it’s value to an interesting sentence about yourself. The sentence must contain all the variables created in parts 1, 2 and 3.
# Have your code print the info message.
# Run your code

# name = "Valentina"
# age = 30
# shoe_size = 39
# info=f"I am {name}, and for some people it's difficult to pronounce my name. I am {age}, so i'm sleep after 23.00. And it pissed me of that my {shoe_size} size is always over in Factory54!!!"
# print(info)

#EX 6
# Create two variables, a and b.
# Each variable value should be a number.
# If a is bigger then b, have your code print Hello World.

# a = 10
# b = 7
# if a > b:
#     print("Hello World")
# else:
#     print("False")

#EX 7  Write code that asks the user for a number and determines whether this number is odd or even.

# num = input("Please write an integer")
# num=int(num)

# if num % 2 == 0:
#     print("This number is even")
# else:
#     print("this number is odd")

#EX 8 Write code that asks the user for their name and determines whether or not you have the same name, print out a funny message based on the outcome.

# my_name="Valentina"
# my_name = my_name.lower()
# your_name=input("What's your name?")
# if my_name == your_name:
#     print("Woooow, you have the most beautiful name!")
# else:
#     print(f"You're the first {your_name} I've met!")


#EX 9
# guest_hight=input("What's your hight?")
# guest_hight=int(guest_hight)
# if guest_hight >= 145:
#     print("You are tall enough to ride")
# else:
#     print("You need to grow a bit more")