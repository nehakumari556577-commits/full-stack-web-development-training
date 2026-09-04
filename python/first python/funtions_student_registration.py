
import json
datalist=[]
def registration_student():
    student = {
        "name":input("please enter your student name:"),
        "id":int(input("please enter your student id:")),
        "email":input("please enter your student email:"),
        "address":input("please enter your student address:")
    }
    datalist.append(student)
    print(json.dumps(datalist,indent=4))

    print("Student registration successfully!")
    

def view_student_data():
    if not datalist:
        print("No student data found")
        return
    
    else:
        for student in datalist:
            print("\nID:", student["id"])
            print("Name:", student["name"])
            print("Email:", student["email"])
            print("Address:", student["address"])
            

def search_student():
        search_id = int(input("Enter student id to search: "))
        for student in datalist:
            if student["id"] == search_id:
                print("\nStudent Found")
                print("ID:", student["id"])
                print("Name:", student["name"])
                print("Email:", student["email"])
                print("Address:", student["address"])
                return 
        print("Student not found")
    
def dashboard():
    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Student Registration")
        print("2. View Student Data")
        print("3. Search Student")
        print("4. Exit")

        option = input(" Please enter your option: ")

        if option == "1":
            registration_student()
        elif option == "2":
            view_student_data()
        elif option == "3":
            search_student()
        elif option == "4":
            print("Program Exit")
            break
            
        else:
            print("Invalid option!")

dashboard()


