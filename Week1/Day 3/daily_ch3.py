
#CHALLENGE 1
# Ask a user for a word
# Write a program that creates a dictionary. This dictionary stores the indexes of each letter in a list.

# Make sure the letters are the keys.
# Make sure the letters are strings.
# Make sure the indexes are stored in a list and those lists are values.


# user_word=input('write a word')
# print(user_word)

# dict_word={}
# for index, char in enumerate(user_word):
#      if char in dict_word:
#         dict_word[char].append(index)
#      else:
#         dict_word[char] = [index]
# print(dict_word)

# CHALLENGE 2

# Create a program that prints a list of the items you can afford in the store with the money you have in your wallet.
# Sort the list in alphabetical order.
# Return “Nothing” if you can’t afford anything from the store.
# Hint : make sure to convert the amount from dollars to numbers. Create a program that deletes the $ sign, and the comma (for thousands)

items_purchase = {
  "Milk": "$3",
  "Bread": "$2",
  "Soap": "$12",
  "Yogurt": "$4",
  "Meat": "$20",
  "Wine":"$30",
  "Microwave":"$150",
  "whiskey":'$60',
  "iphone":"$1,000"
}
wallet="$300"

items_format = {key: int(value[1:].replace(',', '')) for key, value in items_purchase.items()}
print(items_format)

wallet_int=int(wallet[1:])
print(wallet_int)
can_buy= {key: price for key, price in items_format.items() if price <= wallet_int}
buy_list = list(can_buy.keys())  
if buy_list:
    print(f"You can buy: {buy_list}")
else:
    print("You can't buy anything")