
def delete_student_record(listdata):
    search_id = int(input("Enter student id to delete: "))

    for student in listdata:
        if student["id"] == search_id:
            listdata.remove(student)
            print("Student Deleted Successfully!")
            return
    print("Student not found")