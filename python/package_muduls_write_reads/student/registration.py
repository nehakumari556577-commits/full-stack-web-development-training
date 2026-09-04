import json
def registration_student():
    id = input("Enter student id: ")
    name = input("Enter name: ")
    email = input("Enter email: ")

    student = {
        "id": id,
        "name": name,
        "email": email
    }
    with open("students_details.txt", "a") as file:
        json.dump(student, file)
        file.write("\n")

    print("Student registration successfully!")
    
