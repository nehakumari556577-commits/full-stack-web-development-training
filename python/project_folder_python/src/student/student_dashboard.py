import json
students=[]
def student_registration():
    student = {
            "id":int(input("please enter your student id:")),
            "name":input("please enter your student name: "),
            "email":input("please enter your email:"),
            "address":input("please enter your address:")
        }
    students.append(student)
    print(json.dumps(students,indent=4))

    print("Registration Successfully:")

def search_student():
        search_id = int(input("Enter student id to search: "))
        for student in students:
            if student["id"] == search_id:
                print("\nStudent Found")
                print("ID:", student["id"])
                print("Name:", student["name"])
                print("Email:", student["email"])
                print("Address:", student["address"])
                return 
        print("Student not found")

def update_student_record():
 
    search_id = int(input("Enter student id to update: "))

    for student in students:
        if student["id"] == search_id:
            student["name"] = input("Enter New Name: ")
            student["email"] = input("Enter New Email: ")
            student["address"] = input("Enter New Address: ")
            print("Student Record Updated Successfully!")
            return

    print("Student not found")

def delete_student():
    remove_id = int(input("Enter student ID to remove: "))
    for student in students:
        if student['id'] == remove_id:
            students.remove(student)
            print(f"Student ID {remove_id} removed successfully.\n")
            return
    print("Student not found.\n")

def view_student_data():
    if not students:
        print("No student data found")
        return
    
    else:
        for student in students:
            print("\nID:", student["id"])
            print("Name:", student["name"])
            print("Email:", student["email"])
            print("Address:", student["address"])

