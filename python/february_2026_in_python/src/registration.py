import json
import os

file_name = "students.json"
def read_data():
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            return json.load(file)
    return []

def write_data(data):
    with open(file_name, "w") as file:
        json.dump(data, file, indent=4)

def registration_student(listdata):
    student_id = int(input("Enter ID: "))
    name = input("Enter Name: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")

    student = {
        "id": student_id,
        "name": name,
        "email": email,
        "address": address
    }
    listdata.append(student)
    write_data(listdata)
    print("Student Registered Successfully!")

   