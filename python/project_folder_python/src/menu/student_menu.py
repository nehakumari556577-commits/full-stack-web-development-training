from src.student.student_dashboard import student_registration,search_student,update_student_record,delete_student,view_student_data
listdata=[]
def menu():
    while True:        
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Student Registration")
        print("3. Search Student")
        print("4. update student")
        print("4. delete student")
        print("5. View Student Data")
        print("6. Exit")
        user_input()

def user_input():
    option = input("Please enter your option: ")

    if option.isdigit():
        option = int(option)

    if option == 1:
        student_registration()
    
    elif option == 2:
         search_student()
    elif option == 3:
        update_student_record()

    elif option == 4:
         delete_student()

    elif option == 5:
        view_student_data()
         
    elif option == 6:
        print("exit program")
        exit()
    
    else:
         print("invalid option")
menu()
    
                  

        