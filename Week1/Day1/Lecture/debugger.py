age = input('How old are you?')
print(f'Your age is {age}')

if age > 18 and age < 35:
    print('You are enter the club')
elif age < 18 and age > 12:
    print('You can enter')
else: 
    print("You are too old")
