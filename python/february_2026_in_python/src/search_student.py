
def search_student_data(listdata):
    search_id = int(input("Enter student id to search: "))
    for student in listdata:
        if (student["id"])== search_id:
            print("\nStudent Found")
            print("ID:", student["id"])
            print("Name:", student["name"])
            print("Email:", student["email"])
            print("Address:", student["address"])
            return 
    print("Student not found")
