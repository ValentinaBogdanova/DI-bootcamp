# #EX 1
# What are you learning ?
# Instructions
# Write a function called display_message() that prints one sentence telling everyone what you are learning in this course.
# Call the function, and make sure the message displays correctly.

#CODE
# def display_message():
#     print("I am learning Python")
# display_message()
    

#  EX 2: What’s your favorite book ?
# Instructions
# Write a function called favorite_book() that accepts one parameter called title.
# The function should print a message, such as "One of my favorite books is <title>".
# For example: “One of my favorite books is Alice in Wonderland”
# Call the function, make sure to include a book title as an argument when calling the function.

#CODE
# def favorite_book(title):
#     print(f"One of my favorite book is {title}")
# title="Harry Potter"
# favorite_book(title)


# #EX 3  Some Geography
# Instructions
# Write a function called describe_city() that accepts the name of a city and its country as parameters.
# The function should print a simple sentence, such as "<city> is in <country>".
# For example “Reykjavik is in Iceland”
# Give the country parameter a default value.
# Call your function.


#CODE
# def describe_city(city,country):
#     print(f'{city} is in {country}')
# describe_city("Moscow","Russia")
# describe_city("Tel Aviv", "Israel")


#EX 4 Random
# Instructions
# Create a function that accepts a number between 1 and 100 and generates 
# another number randomly between 1 and 100. Use the random module.
# Compare the two numbers, if it’s the same number, display a success
# message, otherwise show a fail message and display both numbers.

#CODE
# def rand_f():
#     import random
#     random_num = random.randint(1,100)
#     return random_num
# x=rand_f()
# y=rand_f()

# user_num=input("Write the number from 0 to 100")
# def compare(user_num,y):
#     if user_num != y:
#         print(f"Upps these numbers {user_num} and {y} are different")
#     else:
#         print(f'Wooow, you r lucky!')

# compare(user_num,y)



#EX 5 
# Let’s create some personalized shirts !
# Instructions
# Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt.
# The function should print a sentence summarizing the size of the shirt and the message printed on it, such as "The size of the shirt is <size> and the text is <text>"
# Call the function make_shirt().

# Modify the make_shirt() function so that shirts are large by default with a message that reads “I love Python” by default.
# Call the function, in order to make a large shirt with the default message
# Make medium shirt with the default message
# Make a shirt of any size with a different message.

# Bonus: Call the function make_shirt() using keyword arguments.

#CODE
# #var1 
# def make_shirt(size, text):
#     print(f"The size of the shirt is {size} and the text is {text}")
# make_shirt(46, "'made in Italy'")

# #var2
# def make_shirt(size="large", text="'I love Python'"):
#     print(f"The size of the shirt is {size} and the text is {text}")
# make_shirt()

# #var3 
# def make_shirt(size, text="'I love Python'"):
#     print(f"The size of the shirt is {size} and the text is {text}")
# make_shirt("MEDIUM")

# #var4
# def make_shirt(size, text):
#     print(f"The size of the shirt is {size} and the text is {text}")
# make_shirt(size="SMALL",text='"Made with love"')


#EX 6 Magicians …
# Instructions
# Using this list of magician’s names

# Create a function called show_magicians(), which prints the name of each magician in the list.
# Write a function called make_great() that modifies the original list of magicians by adding the phrase "the Great" to each magician’s name.
# Call the function make_great().
# Call the function show_magicians() to see that the list has actually been modified.

#CODE
# magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']
# #1
# def show_magicans(magicians):
#     for magician in magicians:
#         print(magician)
# #2

# def make_great(magician_names):
#     for i in range(len(magician_names)):
#         magician_names[i]=f'The Great {magician_names[i]}'
#     return magician_names
# make_great(magician_names)
# print(magician_names)
# show_magicans(magician_names)




#EX 7 Temperature Advice
# Instructions
# Create a function called get_random_temp().
# This function should return an integer between -10 and 40 degrees (Celsius), selected at random.
# Test your function to make sure it generates expected results.

# Create a function called main().
# Inside this function, call get_random_temp() to get a temperature, and store its value in a variable.
# Inform the user of the temperature in a friendly message, eg. “The temperature right now is 32 degrees Celsius.”

# Let’s add more functionality to the main() function. Write some friendly advice relating to the temperature:
# below zero (eg. “Brrr, that’s freezing! Wear some extra layers today”)
# between zero and 16 (eg. “Quite chilly! Don’t forget your coat”)
# between 16 and 23
# between 24 and 32
# between 32 and 40

# Change the get_random_temp() function:
# Add a parameter to the function, named ‘season’.
# Inside the function, instead of simply generating a random number between -10 and 40, set lower and upper limits based on the season, eg. if season is ‘winter’, temperatures should only fall between -10 and 16.
# Now that we’ve changed get_random_temp(), let’s change the main() function:
# Before calling get_random_temp(), we will need to decide on a season, so that we can call the function correctly. Ask the user to type in a season - ‘summer’, ‘autumn’ (you can use ‘fall’ if you prefer), ‘winter’, or ‘spring’.
# Use the season as an argument when calling get_random_temp().

# Bonus: Give the temperature as a floating-point number instead of an integer.
# Bonus: Instead of asking for the season, ask the user for the number of the month (1 = January, 12 = December). Determine the season according to the month.

##1
# def get_random_temp():
#     import random 
#     temp_r=random.randint(-10,40)
#     return temp_r
##2
# def main():
#     temp_r=get_random_temp()
#     print(f"The temperature right now is {temp_r} degrees Celsius")

#3
# def main():
#     temp_r=get_random_temp()
#     print(f"The temperature right now is {temp_r} degrees Celsius")
#     if temp_r < 0:
#             print(f"Brrrrr it's freezing outside. Be careful on the road!")
#     elif 0 <= temp_r <= 16:
#             print(f"Don't forget the scarf!")
#     elif 16 < temp_r <= 23:
#             print(f"Pretty nice weather today. It may be cool in the evening!")
#     elif 24 <= temp_r < 32:
#             print(f"Don't forget the sunscreen cream ahd glasses")
#     elif 32 <= temp_r <= 40:
#             print(f"Extremely hot! Don't stay in the sun for long!")

# main()

##4 


# import random 
# def get_random_temp(season):
#     season=season.lower()  
#     if season == "winter":
#          temp_r=random.randint(-10,0)
#     elif season =="fall" or season =="autumn":
#           temp_r=random.randint(1,16)
#     elif season == "spring":
#          temp_r=random.randint(17,23)
#     elif season == "summer":
#         temp_r=random.randint(17,23)
#     else:
#          print(f"There is no season '{season}'")
#          return None
#     return temp_r


# def main():
#     season = input("Write a season: ") 
#     temp_r = get_random_temp(season)
#     if temp_r is None:
#         return
#     print(f"The temperature right now is {temp_r} degrees Celsius")
#     if temp_r < 0:
#             print(f"Brrrrr it's freezing outside. Be careful on the road!")
#     elif 0 <= temp_r <= 16:
#             print(f"Don't forget the scarf!")
#     elif 16 < temp_r <= 23:
#             print(f"Pretty nice weather today. It may be cool in the evening!")
#     elif 24 <= temp_r < 32:
#             print(f"Don't forget the sunscreen cream ahd glasses")
#     elif 32 <= temp_r <= 40:
#             print(f"Extremely hot! Don't stay in the sun for long!")
# main()


# #EX 8
# Instructions
# This project allows users to take a quiz to test their Star Wars knowledge.
# The number of correct/incorrect answers are tracked and the user receives different messages depending on how well they did on the quiz.

# Here is an array of dictionaries, containing those questions and answers.

data = [
    {
        "question": "What is Baby Yoda's real name?",
        "answer": "Grogu"
    },
    {
        "question": "Where did Obi-Wan take Luke after his birth?",
        "answer": "Tatooine"
    },
    {
        "question": "What year did the first Star Wars movie come out?",
        "answer": "1977"
    },
    {
        "question": "Who built C-3PO?",
        "answer": "Anakin Skywalker"
    },
    {
        "question": "Anakin Skywalker grew up to be who?",
        "answer": "Darth Vader"
    },
    {
        "question": "What species is Chewbacca?",
        "answer": "Wookiee"
    }
]

def quiz(data):
    point=0
    wrong_answers=[]
    wrong_q=[]
    for dictionary in data:
        question= dictionary['question']
        answer_correct=dictionary['answer']
        user_otvet=input(f'{question}')
        if user_otvet.lower() == answer_correct.lower():
            point=point +1
            print(f'Right! You score is {point}')
        else:
            wrong_answers.append(user_otvet)
            wrong_q.append(question)
            print(f'Wrong answer!')
    print(f'\nYour final score is {point}')
    if wrong_answers:
        print(f'Incorrect answers: {", ".join(wrong_answers)}')
        print(f'There are questions you answered wrong:{','.join(wrong_q)}')
    if point <= 3:
        print("Let's play again!")
    
quiz(data)



   