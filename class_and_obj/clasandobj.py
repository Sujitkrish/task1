# class car:
#     def __init__(self,model,year,brand):
#         self.model = model
#         self.brand = brand
#         self.year = year
#     def display_info(self):
#         print(f"{self.brand} {self.model} {self.year}")

#     def booked(self):
#         print(f"{self.brand} {self.model} {self.year}"".... is booked")
    
#     #object

# Tata = car("Tata","serra",2025)
# honda = car("honda","I10",2024)

# print(Tata.display_info(),Tata.booked())
# print (honda.display_info())

# - Create a BankAccount class with attributes: account_number, balance.
# - Add methods: deposit(amount), withdraw(amount), check_balance().
# - Create objects for two accounts and perform transactions.


class BankAccount:
        def __init__(self,account_number,balance):
                self.account_number = account_number
                self.balance = balance
#Methods
        def deposit(self,amount):
                print(f"balance before deposit = {self.balance}")
                self.balance = self.balance + amount
                print(f"balance After deposit = {self.balance}")
        def withdraw(self,amount):
                print(f"balance before withdraw = {self.balance}")
                self.balance = self.balance - amount
                print(f"balance After withdraw = {self.balance}")
        def check_balance(self):
                print(f"Your balance is : {self.balance}")
bhuvi = BankAccount("acc0001",180000)
# print(bhuvi.deposit(5000))
# print(bhuvi.withdraw(6000))
# print(bhuvi.check_balance())
                
                

                    