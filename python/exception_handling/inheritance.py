# class Vehicle:
#     def start(self):
#         print("vehicle starts")

# class car(Vehicle):
#     def drive(self):
#         print("car is driving")

# class electricCar(car):
#     def charge(self):
#         print("electric car is charging")

# ob=electricCar()
# ob.start()
# ob.drive()
# ob.charge()

class Account:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance

    def show_balance(self):
        print("name:",self.name)
        print("Balance:",self.balance)

class SavingsAccount(Account):
    def add_interest(self):
        interest=self.balance*0.05
        self.balance+=interest
        print("Interest added:",interest)
                                    
class PremiumSavingsAccount(SavingsAccount):
    def cashback(self):
        cashback = 500
        self.balance += cashback
        print("Cashback added:", cashback)

ob= PremiumSavingsAccount("neha",10000)
ob.show_balance()     
ob.add_interest()    
ob.cashback()        
ob.show_balance()
