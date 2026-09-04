def search(students):
    search_id = int(input("Enter student ID to search: "))
    for student in students:
        if student['id'] == search_id:
            print(f"Found: ID: {student['id']}, Name: {student['name']},Email:{student['email']}, Address: {student['address']}\n")
            return
    print("Student not found.\n")
