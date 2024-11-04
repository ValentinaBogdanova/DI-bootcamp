#EX 1
print("Hello world"*4,"I love python" * 4)


#EX 2
users_month=input("Write tha numer of month")
users_month=int(users_month)
if 3<= users_month <=5:
    print("This is Spring!")
elif 6<= users_month <= 8:
    print("This is Summer!")
elif 9<= users_month <=11:
    print("This is Autumn!")
elif users_month==12 or users_month<=2:
    print("This is Winter!")
else:
    print("This is invalid number")
    