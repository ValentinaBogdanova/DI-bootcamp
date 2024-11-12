class Animal:
    def walk(self):
        return f'this animal is walking'

#some func not method 
#def addition(a,b)



# if __name__ =="__main__":

#     animal = Animal()
#     print(animal.walk())


#ATRIBUTES OF THE CLASS

class BankAccount:
    ACCOUNT_AVAILABLE_NUMBER = 1000  #атрибьют класса 
    BANK_NAME = "Hapoalim"
    def __init__(self, owner_name, number, balance = 0):
        self.__owner_name = owner_name
        #self.number = number     #можно удалить
        self.number = BankAccount.ACCOUNT_AVAILABLE_NUMBER
        self.transaction = []
        self._balance = balance #int
        BankAccount.ACCOUNT_AVAILABLE_NUMBER += 1 #изменяем атрибьют


    def show_balance(self):
        print(f"Your balance is {self._balance}")

    def deposit(self, amount):
        self._balance += amount
        self.show_balance()
        #add transaction track code
        self.transaction.append(f"deposit transaction: {amount}")
        return self # отсылка к my_account #self.balance - если делать так то
        
    def withdraw(self, amount):
        if amount < self._balance:
            self._balance -= amount
            self.show_balance()
            self.transaction.append(f"withdraw transaction: {- amount}")
        else:
            print("Your balance is minus")
        return self
    def show_trans(self):
        for i,track in enumerate(self.transaction):
            print(f"transaction {i+1}: {track}")
        return self.show_balance

my_account = BankAccount("Valentina Bogdanova", 156, 100)
print(my_account.number)
my_account1 = BankAccount("Valentina Bogdanova", 156, 100)
print(my_account1.number)
my_account2 = BankAccount("Valentina Bogdanova", 156, 100)
print(my_account2.number)
# print(my_account.balance)
# my_account.deposit(120).withdraw(25).deposit(200).withdraw(20).withdraw(140)
# # print(my_account.balance)
# my_account.show_trans()
# my_account.withdraw(500)

class Circle:
    color = "red"
    list_of_circles=[]
    def __init__(self, diameter, color):
        self.diameter = diameter
        self.color = color
        Circle.list_of_circles.append()

    def grow(self, factor=2):
        self.diameter = self.diameter * factor

    def get_color(self):
       return Circle.color

circle1 = Circle(2,"blue")
circle1.color = 'blue'
print(circle1.color)
print(Circle.color)        # вызвать атрибьют класса
print(circle1.get_color())
# circle1.grow(3)
# print(circle1.diameter)
c2 = Circle(4)
print(c2.color)