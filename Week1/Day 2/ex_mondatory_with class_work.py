# #EX 1 
# my_fav_numbers={7,8,19,12} #Create a set called my_fav_numbers with all your favorites numbers.
# my_fav_numbers.add(1)#Add two new numbers to the set.
# my_fav_numbers.add(30)
# my_fav_numbers1=list(my_fav_numbers) #Remove the last number.
# my_fav_numbers1.pop() 
# my_fav_numbers1.pop()
# print(my_fav_numbers1)
# my_fav_numbers2=set(my_fav_numbers1)

# friend_fav_numbers={3, 6, 65, 12} #Create a set called friend_fav_numbers with your friend’s favorites numbers.
# set_num=my_fav_numbers2.union(friend_fav_numbers) #Concatenate my_fav_numbers and friend_fav_numbers to a new variable called our_fav_numbers.
# print(set_num)

#EX 2

#Its imposible to add new variable to a tuple

# # EX 3

# basket = ["Banana", "Apples", "Oranges", "Blueberries"] 
# del basket[0] # Remove “Banana” from the list.
# print(basket)

# basket.pop() # Remove “Blueberries” from the list.
# print(basket)

# basket.append("kiwi")# Add “Kiwi” to the end of the list.
# print(basket)

# basket.insert(0,"Apples") # Add “Apples” to the beginning of the list.
# print(basket)

# print(basket.count("Apples")) # Count how many apples are in the basket.

# basket.clear() # Empty the basket.
# print(basket) # Print(basket)


#EX 4
# integer = 4
# float = 4.5 
# list_num=[1.5,2,2.5,3,3.5,4,4.5,5]
# print(list_num)

#Can you think of another way to generate a sequence of floats?

# list_num1=[] 

# for i in range(1,6):   
#    if i==5:
#       break
#    list_num1.append(i)
#    list_num1.append(i+0.5)
#    print(list_num1[1:])
   

#EX 5 FOR LOOP
 #Use a for loop to print all numbers from 1 to 20, inclusive.


# for i in range(1,21):
#     print(i)


#Using a for loop, that loops from 1 to 20(inclusive), print out every element which has an even index.


# list_of_num = range(1,21) 
# even_list=[]
# for i in list_of_num:
#     if i % 2 == 0:
#         even_list.append(i)
# print(even_list)



#EX6 WHILE LOOP
#Write a while loop that will continuously ask the user for their name, unless the input is equal to your name.

# my_name="Valentina"

# while True:
#     user_name=input("What is your name?")
#     if user_name==my_name:
#         print('Wow I am Valentina too, nice to meet you!')
#         break
#     else:
#         print(f"Nice to meet you, {user_name}")

#EX7 Exercise 7: Favorite fruits
#Ask the user to input their favorite fruit(s) (one or several fruits).
#Store the favorite fruit(s) in a list (convert the string of words into a list of words)

# fruts=input("Write your favorite fruis in a string and saparate them with single space")
# list_fruts=fruts.split()
# print(list_fruts)

# for frut in list_fruts:
#     user_choose = input("Choose a frut")
#     if user_choose in list_fruts:
#         print("You chose one of your fav frut! Enjoy!")
#     else:
#         print("You chose a new frut. I hope you enjoy!")


#EX 8 who ordered a pizza?
#Write a loop that asks a user to enter a series of pizza toppings, when the user inputs ‘quit’ stop asking for toppings.
#As they enter each topping, print a message saying you’ll add that topping to their pizza.
#Upon exiting the loop print all the toppings on the pizza pie and what the total price is (10 + 2.5 for each topping).


# toppings=[]
# while True:
#     top=input("Write a topping for your pizza one by one. When you finish enter 'quit'")
#     toppings.append(top)
#     if top == "quit":
#         break
# print(f"You choose pizza with {toppings}")
# num_top=len(toppings)
# prise=int(num_top)*2.5 + 10
# print(f"Your pizza costs {prise}")


#EX 9 CINEMAX
#A movie theater charges different ticket prices depending on a person’s age
#Ask a family the age of each person who wants a ticket
#Store the total cost of all the family’s tickets and print it out.


# each_prise=[]
# while True:
#     age=input("Enter an age of each person of your family one by one, write 'stop' when finish")
#     if age.lower() == "stop":
#         break
#     if not age.isdigit():
#         print("Please enter a valid number.")
#         continue
#     age_num = int(age)
#     if age_num <3:
#         each_prise.append(0) # can add just continue
#     elif 3 <= age_num <= 12:
#         each_prise.append(10)
#     elif 12 < age_num:
#         each_prise.append(15)
# total_prise = sum(each_prise)




# family_size=int(input("how many ppl?")) 
# i = 0
# total_cost =0
# while i <= family_size:
#     age = int(input("How old is member?"))
#     if age<3:
#         total_cost+=0





#A group of teenagers are coming to your movie theater and want to watch a movie that is restricted for people between the ages of 16 and 21.
#Given a list of names, write a program that asks teenager for their age, if they are not permitted to watch the movie, remove them from the list.
#At the end, print the final list.


# list_teenagers=['Sara', 'Orly', 'Kevin', 'Yasha']
# for teen in list_teenagers:
#     age_teen=input(f"Hi,{teen}!How old are you?")
#     age_int=int(age_teen)
#     if age_int <= 16:
#         list_teenagers.remove(teen)
#         if 21 <= age_int:
#             list_teenagers.remove(teen)
# print(list_teenagers)


#EX 10 Sandwich Orders


# sandwich_orders = ["Tuna sandwich", "Pastrami sandwich", "Avocado sandwich", "Pastrami sandwich", "Egg sandwich", "Chicken sandwich", "Pastrami sandwich"]

# sandwich_run_out="Pastrami sandwich"
# while sandwich_run_out in sandwich_orders:
#     sandwich_orders.remove(sandwich_run_out)
# finished_sandwiches=[]
# while sandwich_orders:
#     sandwich=sandwich_orders.pop(0)
#     finished_sandwiches.append(sandwich)
#     print(f'I made your {sandwich}')
# print(f"All the sanwiches are ready {finished_sandwiches}")


