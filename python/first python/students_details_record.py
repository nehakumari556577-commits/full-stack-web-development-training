datalist = []

while True:
    print("\n**** STUDENT MENU ****")
    print("1. Registration")
    print("2. Display student records")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Please Enter Your choice: ")

    if choice == "1":
        print("\n--- Student Registration ---")
        student_id = input("Enter Your Student ID: ")
        name = input("Enter Your Name: ")
        address = input("Enter Your Address: ")
        email = input("Enter Your Email: ")

        qualifications = []
        more = input("Do you want to add qualifications? (yes/no): ")

        while more.lower() == "yes":
            qname = input("Enter Qualification Name: ")
            year = input("Enter Passing Year: ")
            qualifications.append([qname, year])
            more = input("Do you want to add more qualifications? (yes/no): ")

        student = {
            "student_id": student_id,
            "Name": name,
            "Address": address,
            "Email": email,
            "qualifications": qualifications
        }
        datalist.append(student)
        print("\nRegistration Successful!")

    elif choice == "2":
        print("\n--- Student Records ---")
        if not datalist:
            print("No records found!")
        else:
            for student in datalist:
                print("\nID:", student["student_id"])
                print("Name:", student["Name"])
                print("Address:", student["Address"])
                print("Email:", student["Email"])
                print("Qualifications:")
                for q in student["qualifications"]:
                    print( q[0],q[1])

    elif choice == "3":
        print("\n--- Search Student ---")
        search_id = input("Enter Student ID: ")

        for student in datalist:
            if student["student_id"] == search_id:
                print("\n--- Student Details ---")
                print("ID:", student["student_id"])
                print("Name:", student["Name"])
                print("Address:", student["Address"])
                print("Email:", student["Email"])
                print("Qualifications:")
                for q in student["qualifications"]:
                    print(" -", q[0], "| Year:", q[1])
                break
        else:
            print("\nStudent Record Not Found!")

    elif choice == "4":
        print("\nExit Successfully! Thank You!")
        break

    else:
        print("\nInvalid choice, Try Again!")
