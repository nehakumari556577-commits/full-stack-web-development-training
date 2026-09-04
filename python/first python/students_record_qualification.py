import json
datalist = []
while True:
    print("\n**** STUDENT MENU ****")
    print("1. Registration")
    print("2. Display student records")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Please Enter Your choice: ")

    if not choice.isdigit():
        print("Please enter a valid number")


    choice = int(choice)

    if choice == 1:
        student = {
            "name": input("Please enter student name: "),
            "id": input("Please enter student id: "),
            "address": input("Please enter student address: "),
            "email": input("Please enter student email: "),
            "qualification": []  
        }
        while True:
            more = input("Do you want to add qualification? (yes/no): ").lower()
            if more == "yes":
                q_name = input("Enter qualification name: ")
                year = input("Enter passing year: ")
                student["qualification"].append({"name": q_name, "year": year})
            elif more == "no":
                break
            else:
                print("Please type yes or no")

        datalist.append(student)
        print(json.dumps(datalist,indent=4))
        
        print("Student registration successfully!")

    elif choice == 2:
        if not datalist:
            print("No records found")
        else:
            for student in datalist:
                print("\nName:", student["name"])
                print("ID:", student["id"])
                print("Address:", student["address"])
                print("Email:", student["email"])
                print("Qualifications:")
                if not student["qualification"]:
                    print(" - None")
                else:
                    for q in student["qualification"]:
                        print(" -", q["name"], "(", q["year"], ")")

    elif choice == 3:
        search_id = input("Enter student ID to search: ")
        found = False
        for student in datalist:
            if student["id"] == search_id:
                print("\nStudent Found!")
                print("Name:", student["name"])
                print("Email:", student["email"])
                print("Qualifications:")
                if not student["qualification"]:
                    print(" - None")
                else:
                    for q in student["qualification"]:
                        print(" -", q["name"], "(", q["year"], ")")
                found = True
                break
        if not found:
            print("Student not found")
    elif choice == 4:
        print("Exiting program...")
        break

    else:
        print("invalid choice")
