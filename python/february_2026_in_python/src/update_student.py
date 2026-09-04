
def update_student_record(listdata):
    search_id = int(input("Enter student id to update: "))

    for student in listdata:
        if student["id"] == search_id:
            student["name"] = input("Enter New Name: ")
            student["email"] = input("Enter New Email: ")
            student["address"] = input("Enter New Address: ")
            print("Student Record Updated Successfully!")
            return

    print("Student not found")