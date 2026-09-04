def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def menu():
    print("*** MENU ***")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")

    option = int(input("Please enter any option: "))
    x = int(input("Please enter first number: "))
    y = int(input("Please enter second number: "))

    if option == 1:
        print("Addition =", add(x, y))
    elif option == 2:
        print("Subtraction =", subtract(x, y))
    elif option == 3:
        print("Multiplication =", multiply(x, y))
    else:
        print("Invalid option")

menu()
