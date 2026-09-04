datalist=[]

while True:
    print("****STUDENT MENU****")
    print("1. Registration")
    print("2. Search Student Record")
    print("3. Exit")
    

    choice = input("Please Enter Your choice: ")

    if choice == "1":
        print("\n--- Student Registration ---")
        student_id = input("Enter Your Student ID: ").strip()
        name = input("Enter Your Name: ")
        address = input("Enter Your Address: ")
        email = input("Enter Your Email: ")

        student = {
            "student_id": student_id,
            "Name": name,
            "Address": address,
            "Email": email
        }
        datalist.append(student)

        print("\n Registration Successfully!")

    elif choice == "2":
        print("\n--- Search Student ---")
        search_id = input("Enter Student ID : ").strip()

        found = False
        for student in datalist:
            if student["student_id"] == search_id:
                print("\n Student Details")
                print("ID:", student["student_id"])
                print("Name:", student["Name"])
                print("Address:", student["Address"])
                print("Email:", student["Email"])
                found = True
                break
        else:
            print("\n Student Record Not Found!")

    elif choice == "3":
        print("\n Exit Successfully Thank You!")
        break

    else:
        print("\n Invalid choice, Try Again:")
