#EX 1 
# Convert the two following lists, into dictionaries.
#Hint: Use the zip method

# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# print(dict(zip(keys,values)))



#EX 2 A movie theater charges different ticket prices depending on a person’s age.
# if a person is under the age of 3, the ticket is free.
# if they are between 3 and 12, the ticket is $10.
# if they are over the age of 12, the ticket is $15.

# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

# # #How much does each family member have to pay ?

# for name,age in family.items():
#      if age <3:
#          cost=0
#          print(f"Hey {name}, tha cost of tour ticket {cost}")
#      elif 3 <= age <= 12:
#          cost=10
#          print(f"Hey {name}, tha cost of tour ticket {cost}")
#      elif 12 < age:
#          cost=15
#          print(f"Hey {name}, tha cost of tour ticket {cost}")




#Print out the family’s total cost for the movies.

# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
# cost=0
# family_age=[]
# for value in family.values():
#     family_age.append(value)
#     print(family_age)
#     if value <3:
#         continue
#     elif 3 <= value <= 12:
#         cost += 10
#     elif 12 < value:
#         cost +=15
# print(f'Total cost is {cost}')



#Bonus: Ask the user to input the names and ages instead of using the provided family variable (Hint: ask the user for names and ages and add them into a family dictionary that is initially empty).

# new_member=input("Write your name and age wth the space")
# new_list=new_member.split()
# new_key=new_list[0]
# new_mem=new_list[1]
# family[new_key]=new_mem
# print(family)



#EX 3

#2. Create a dictionary called brand which value is the information from part one (turn the info into keys and values).
#The values type_of_clothes and international_competitors should be a list. The value of major_color should be a dictionary.

# brand={'name': 'Zara', 
#        'creation_date': 1975,
#        'creator_name': 'Amancio Ortega Gaona',
#        'type_of_clothes':['men', 'women', 'children', 'home'],
#        'international_competitors': ['Gap', 'H&M', 'Benetton'], 
#        'number_stores': 7000,
#        'major_color':{'France': 'blue', 'Spain': 'red', 'US': 'pink, green'},
# }

# #3 Change the number of stores to 2.

# # brand['number_stores']=2
# # print(brand)

# #4 Print a sentence that explains who Zaras clients are.

# # customers=brand['type_of_clothes']
# # customers=', '.join(customers[:-1])
# # print(f'Clients of Zara are {customers}')


# #5 Add a key called country_creation with a value of Spain.

# brand['country_creation']='Spain'
# print(brand)

# #Check if the key international_competitors is in the dictionary. If it is, add the store Desigual

# print('international_competitors' in brand.keys())
# new_compet='Desiqual'
# key='international_competitors'
# if key in brand:
#     brand['international_competitors'].append(new_compet)
# else:
#     brand[key]=[new_compet]
# print(brand)


# #7. Delete the information about the date of creation.

# del brand['creation_date']
# print(brand)

# #8 Print the last international competitor.

# print(brand['international_competitors'][-1])

# #9 Print the major clothes colors in the US.

# print(brand['major_color']['US'])

#10 Print the amount of key value pairs (ie. length of the dictionary).

# print(len(brand))

#11 Print the keys of the dictionary

# for key in brand.keys():
#     print(key)

# #12 Create another dictionary called more_on_zara with the following details:
# #13. Use a method to add the information from the dictionary more_on_zara to the dictionary brand.
# creation_date: 1975 
# number_stores: 10 000

# more_on_zara={"creation_date":'1975',
#               "number_stores":"10 000"
#               }
# brand.update(more_on_zara)
# print(brand)

#14 Print the value of the key number_stores. What just happened ?

# print(brand['number_stores'])  #invalid syntax DO NOT KNOW HOW TO FIX IT BY CODE


#Exercise 4 : Disney characters
#Use a for loop to recreate the 1st result. Tip : don’t hardcode the numbers.
users = ["Mickey","Minnie","Donald","Ariel","Pluto"]
users_dict={}

for index in range(len(users)):
    users_dict[users[index]]=index
print(users_dict)

#Use a for loop to recreate the 2nd result. Tip : don’t hardcode the numbers.

# for index in range(len(users)):
#     users_dict[index]=users[index]
# print(users_dict)


#Use a method to recreate the 3rd result. Hint: The 3rd result is sorted alphabetically.
#Only recreate the 1st result for:
# The characters, which names contain the letter “i”.
# The characters, which names start with the letter “m” or “p”.
# DONT UNDERSTAND HOW TO DO these 2 tasks
   
