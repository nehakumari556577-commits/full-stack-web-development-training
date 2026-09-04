import registration_student 
import search_student
import get_all_records
import remove
students=[]
def menu():
    while True:
        print("\n===== USER MENU =====")
        print("1. Registration")
        print("2. Get All Records")
        print("3. Search User")
        print("4. Remove by ID")
        print("5. Exit")
        
        option = input("Please enter your option: ")

        if option.isdigit():
            option = int(option)
            if option == 1:
                registration_student.registration(students)
            elif option == 2:
                get_all_records.get_all(students)
            elif option == 3:
                search_student.search(students)
            elif option == 4:
                remove.remove_by_id(students)
            elif option == 5:
                print("Program exited")
                break
            else:
                print("Invalid option")
        else:
            print("Please enter numbers only")
menu()
