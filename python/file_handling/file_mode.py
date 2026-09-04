import json

file_path = "students.json"
listdata = []
def registration_student():
    student = {}
    student["id"] = input("please enter your id: ")
    student["name"] = input("please enter your name: ")
    student["address"] = input("please enter your address: ")
    return student
    

def append_student(new_student):

    with open(file_path, "r") as file:
        listdata = json.load(file)
    listdata.append(new_student)

    with open(file_path, "w") as file:
        json.dump(listdata, file, indent=4)

def read_students():

    with open(file_path, "r") as file:
        listdata = json.load(file)
        for student in listdata:
            print(student)

for i in range(2):
    student = registration_student()
    append_student(student)

read_students()
