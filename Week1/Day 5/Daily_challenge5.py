# CHALLENGE 1
# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
# Use List Comprehension

input_words=input("Write words and separete them with comma")
new_words = sorted([word.strip() for word in input_words.split(",")])
print(new_words)


#CHALLENGE 2
# Write a function that finds the longest word in a sentence. If two or more words are found, return the first longest word.
#Characters such as apostrophe, comma, period count as part of the word (e.g. O’Connor is 8 characters long).

# user_senten=input("Write a sentence")
# splited_sen=user_senten.split()
# largest_world=max(splited_sen, key=len)
# print(largest_world)