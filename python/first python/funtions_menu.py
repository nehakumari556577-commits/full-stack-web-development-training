
x=int(input("please enter first number:"))
y=int(input("please enter second number:"))

def multiply(x,y):
    print(x*y)

def division(x,y):
    print(x/y)

def menu():   
    print("1. multiply")
    print("2. division")

    option=int(input("please enter any option: "))
    return option

def dashboard():
        number=menu()
        if number==1:
            multiply(x,y)

        elif number==2:
            division(x,y)
        else:
            print("invalid option")

dashboard()

    
