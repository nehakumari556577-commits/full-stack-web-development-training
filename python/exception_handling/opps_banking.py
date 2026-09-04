class BankAccount:
    def __init__(self):
        self.balance = 5000
    
    def add_amount(self, amount):
        self.balance += amount
        print(f"The amount is credited. Current balance: {self.balance}")

    def withdraw_amount(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"The amount is debited. Current balance: {self.balance}")

    def check_balance(self):
        print(f"Current balance: {self.balance}")
        
ob= BankAccount()

while True:
    print("\n--- Menu ---")
    print("1. Add Amount")
    print("2. Withdraw Amount")
    print("3. Check Balance")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        amount = float(input("Enter amount to add: "))
        ob.add_amount(amount)
    elif choice == 2:
        amount = float(input("Enter amount to withdraw: "))
        ob.withdraw_amount(amount)
    elif choice == 3:
        ob.check_balance()
    elif choice == 4:
        print("Exiting program")
        break
    else:
        print("Invalid choice! Please enter.")