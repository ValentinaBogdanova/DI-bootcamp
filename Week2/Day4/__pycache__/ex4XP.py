#EX 1 Random Sentence Generator
# Instructions
# Description: In this exercise we will create a random sentence generator. We will do this by asking the user how long the sentence should be and then printing the generated sentence.

# Hint : The generated sentences do not have to make sense.

# Download this word list

# Save it in your development directory.

# Create a function called get_words_from_file. This function should read the file’s content and return the words as a collection. What is the correct data type to store the words?

# Create another function called get_random_sentence which takes a single parameter called length. The length parameter will be used to determine how many words the sentence should have. The function should:
# use the words list to get your random words.
# the amount of words should be the value of the length parameter.

# Take the random words and create a sentence (using a python method), the sentence should be lower case.

# Create a function called main which will:

# Print a message explaining what the program does.

# Ask the user how long they want the sentence to be. Acceptable values are: an integer between 2 and 20. Validate your data and test your validation!
# If the user inputs incorrect data, print an error message and end the program.
# If the user inputs correct data, run your code.



#CODE

# import random

# def main():
#     def get_words_from_file():
#         with open('C:\\Users\\Acer\\Desktop\\DI-bootcamp\\Week2\\Day4\\Exercises\\sowpods.txt', 'r', encoding="utf-8") as f:
#             file_words = f.read()
#             list_words = file_words.split()
#             return list_words

#     list_words1 = get_words_from_file() 

#     def get_random_sentence():
#         print("The program creates a random sentence in the length you choose.")
#         while True:
#             try:
#                 length = int(input("Enter a length of sentence from 2 to 20: "))
#                 if 2 <= length <= 20:   
#                     break
#                 else:
#                     print("Invalid length. Please enter a number between 2 and 20:  ")
#             except ValueError:
#                 print("Invalid input. Please enter a number between 2 and 20:  ")
#         sentence = [random.choice(list_words1) for _ in range(length)]
#         return " ".join(sentence)
#     result = get_random_sentence().lower()
#     print(result)
#     print("Program is finished")

# main()


#EX 2 

# Access the nested “salary” key from the JSON-string above.
# Add a key called “birth_date” to the JSON-string at the same level as the “name” key.
# Save the dictionary as JSON to a file.

import json
sampleJson = """{ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}"""
file_sample=json.loads(sampleJson) #    Так как samplejson это строка ее нужно преобразовать в словарь
salary = file_sample["company"]["employee"]["payable"]["salary"] #по уровням спускаемся к нужному ключу
print(salary)
file_sample["company"]["employee"]["birth_day"] = "1990-07-15"
print(file_sample)

with open("json_file.json", "w") as file:
    json.dump(file_sample, file, indent = 4)    # indent - добавляем количесво пробелов для лучшей читаемости


   