def remove_by_id(students):
    remove_id = int(input("Enter student ID to remove: "))
    for student in students:
        if student['id'] == remove_id:
            students.remove(student)
            print(f"Student ID {remove_id} removed successfully.\n")
            return
    print("Student not found.\n")
