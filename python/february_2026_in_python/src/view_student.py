
def view_student_record(listdata):

    if not listdata:
        print("No Records Found!")
        return
    for student in listdata:
        print("ID:", student["id"])
        print("Name:", student["name"])
        print("Email:", student["email"])
        print("Address:", student["address"])
