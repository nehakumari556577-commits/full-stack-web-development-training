studentdata = []

number = int(input("please enter number of student to registation: "))

if number < 1 or number > 5:
    print("please enter a valid number between 1 and 5 only")

else:
    for i in range(number):
        print(f"\nEnter details of student {i+1}")

        student = {}
        student["id"] = input("please enter your id: ")
        student["name"] = input("please enter your name: ")
        student["address"] = input("please enter your address: ")
        
        studentdata.append(student)
        print(studentdata)
