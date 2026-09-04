def get_all(students):
    if not students:
        print("No records found.\n")
        return
    print("All Students:")
    for student in students:
        print(f"ID: {student['id']}, Name: {student['name']}, Address: {student['address']}")
    print(student)
