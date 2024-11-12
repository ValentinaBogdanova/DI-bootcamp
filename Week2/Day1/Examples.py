# class BankAccount:
#     def __init__(self, owner_name, number, balance = 0):
#         self.owner_name = owner_name
#         self.number = number
#         self.transaction = []
#         self.balance = balance #int
    
#     def show_balance(self):
#         print(f"Your balance is {self.balance}")

#     def deposit(self, amount):
#         self.balance += amount
#         self.show_balance()
#         #add transaction track code
#         self.transaction.append(f"deposit transaction: {amount}")
#         return self # отсылка к my_account #self.balance - если делать так то
        
#     def withdraw(self, amount):
#         if amount < self.balance:
#             self.balance -= amount
#             self.show_balance()
#             self.transaction.append(f"withdraw transaction: {- amount}")
#         else:
#             print("Your balance is minus")
#         return self
#     def show_trans(self):
#         for i,track in enumerate(self.transaction):
#             print(f"transaction {i+1}: {track}")
#         return self.show_balance

# my_account = BankAccount("Valentina Bogdanova", 156, 100)
# # print(my_account.balance)
# my_account.deposit(120).withdraw(25).deposit(200).withdraw(20).withdraw(140)
# # print(my_account.balance)
# my_account.show_trans()
# my_account.withdraw(500)

#implement all theese methods (exepts show_balance() 
# a code that wii add ther actiond to thansactions list)
# and do a deposit and withdraw and then print the transaction list to see 
#the tracked informaition


# def add_animal(self, *args, amount = 1):
#     for animal in *args:
#         self.animals.append(animal)
# macdonalds = Farm()
# macdonalds.add_animal("cow", "hourse", "duck")
