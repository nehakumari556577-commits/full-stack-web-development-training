from src import registration 
from src import search_student
from src import update_student
from src import delete_student
from src import view_student
listdata=[]
def menu():
    while True:
        print("\n===== USER MENU =====")
        print("1. Registration")
        print("2. search student")
        print("3. update student record")
        print("4. delete student")
        print("5. view student records")
        print("6. exit")
        
        option = input("Please enter your option: ")

        if option.isdigit():
            option = int(option)
            if option == 1:
                registration.registration_student(listdata)
            elif option == 2:
                search_student.search_student_data(listdata)
            elif option == 3:
                update_student.update_student_record(listdata)
            elif option == 4:
                delete_student.delete_student_record(listdata)
            elif option == 5:
                view_student.view_student_record(listdata)
            elif option == 6:
                print("Program exited")
                break
            else:
                print("Invalid option")


