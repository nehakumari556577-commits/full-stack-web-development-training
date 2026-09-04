students=[]
def registration(students):
    student = {
        "name":input("please enter your student name: "),
        "id":int(input("please enter your student id:")),
        "email":input("please enter your email:"),
        "address":input("please enter your address")
    }
    students.append(student)

    print("Registration Successfully:")
