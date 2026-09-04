# import json

# file_path = "students.json"
# listdata = []

# def registration_student():
#     student = {}
#     student["id"] = input("please enter your id: ")
#     student["name"] = input("please enter your name: ")
#     student["address"] = input("please enter your address: ")
#     listdata.append(student)

# def save_students(students):
#     with open(file_path, "w") as file:
#         json.dump(students, file, indent=4)
    
# def read_students():

#     with open(file_path, "r") as file:
#         data = json.load(file)
#         for student in data:
#             print(student)

# for i in range(2):
#     registration_student()

# save_students(listdata)

# read_students()


from auth.manage_user import manage_menu
manage_menu()


from database.data import data
import msvcrt  

def input_password(prompt="Password: "):
    print(prompt, end="", flush=True)
    password = ""
    while True:
        char = msvcrt.getch()
        if char in {b'\r', b'\n'}: 
            print("")
            break
        elif char == b'\x08': 
            if len(password) > 0:
                password = password[:-1]
                print("\b \b", end="", flush=True)
        else:
            password += char.decode("utf-8")
            print("*", end="", flush=True)
    return password

class Login:    
    def __init__(self):
        self.data = data()
        self.file = "database/users.json"

    def login(self):

        print("\n\033[96m********* LOGIN **********")
        users = self.data.read(self.file)

        if users is None:       
            users = []

        while True:
            email = input("Please Enter Your Email: ")

            if "@" not in email or "." not in email:
                print("Invalid Email Format")
            else:
                break
        
        while True:
            password = input_password("Please Enter Your Password: ")

            if not password.isalnum():
                print("Password must be alphanumeric")
                continue

            if len(password) < 6:
                print("Password must be at least 6 characters")
                continue

            for u in users:
                if u["email"] == email and u["password"] == password:
                    print("\033[92mLogin Successfully")
                    return u

            print("Invalid Email or Password")
            return None
        




from auth.sign_up import Signup
from auth.login import Login
from dashboard.Admin_dashboard import AdminDashboard
from dashboard.staff_dashboard import StaffDashboard

signup_obj = Signup()
login_obj = Login()

def manage_menu():

    while True:
        print('-'*40)
        print("\n\033[93m===== RESTAURANT MANAGEMENT SYSTEM =====")
        print("1 Signup")
        print("2 Login")
        print("3 Exit")
        print('-'*40)

        choice = input("Please Enter Your Choice: ")

        if not choice.isdigit():
            print("Invalid input")
            continue

        choice = int(choice)

        if choice == 1:
            signup_obj.signup()

        elif choice == 2:

            user = login_obj.login()

            if user["role"] == "admin":
                admin = AdminDashboard(user)
                
                admin.run()
            elif user["role"] == "staff":
                staff=StaffDashboard(user)
                staff.run()
            else:
                print("Login Failed ")

        elif choice == 3:
            print("Exit Program")
            break

        else:
            print("Invalid Choice")


from database.data import data
import uuid
import msvcrt

def input_password(prompt="Password: "):
    print(prompt, end="", flush=True)
    password = ""
    while True:
        char = msvcrt.getch()
        if char in {b'\r', b'\n'}:
            print("")
            break
        elif char == b'\x08':
            if len(password) > 0:
                password = password[:-1]
                print("\b \b", end="", flush=True)
        else:
            password += char.decode("utf-8")
            print("*", end="", flush=True)
    return password

class Signup:
    def __init__(self):
        self.data = data()
        self.file = "database/users.json"

    def signup(self):

        users = self.data.read(self.file)
        if users is None:
            users = []

        print("\n******** SIGNUP ********")

        user_id = str(uuid.uuid4())

        while True:
            name = input("Please Enter Your Name: ")

            if not name.replace(" ", "").isalpha():
                print("Please enter only letters")
                continue

            for user in users:
                if user["name"].lower() == name.lower():
                    print("Name already exists")
                    return   
            break  

        while True:
            email = input("Please Enter Your Email: ")

            if "@" not in email or "." not in email:
                print("Invalid Email format")
                continue  

            for user in users:
                if user["email"] == email:
                    print("Email already registered")
                    return   

            break   

        while True:
            password = input_password("Please Enter Your Password: ")
            confirm = input_password("Confirm Your Password: ")

            if password != confirm:
                print("Passwords do not match")
                continue

            if not password.isalnum():
                print("Please enter only letters and numbers")
                continue

            if len(password) < 6:
                print("Password must be at least 6 characters")
                continue

            break

        role = "staff"

        new_user = {
            "user_id": user_id,
            "name": name,
            "email": email,
            "password": password,
            "role": role
        }

        users.append(new_user)
        self.data.write(self.file, users)

        print("Signup Successful ")


        from database.data import data

class AdminDashboard:

    def __init__(self, user):
        self.user = user
        self.menu_data = data()
        self.menu_file = "database/menu.json"

    def run(self):
        while True:
            print("\n===== ADMIN DASHBOARD =====")
            print("Welcome", self.user["name"])
            print("1 Manage Menu")
            print("2 Manage Orders")
            print("3 Reports")
            print("4 Logout")

            choice = input("Enter choice: ")
            if not choice.isdigit():
                print("Invalid Input")
                continue

            choice = int(choice)

            if choice == 1:
                self.manage_menu()
            elif choice == 2:
                print("Order Management (coming soon)")
            elif choice == 3:
                print("Reports (coming soon)")
            elif choice == 4:
                print("Logging out...")
                break
            else:
                print("Invalid Choice")

    def manage_menu(self):

        while True:
            print("\n===== MENU MANAGEMENT =====")
            print("1 Add Item")
            print("2 View Menu")
            print("3 Update Item")
            print("4 Delete Item")
            print("5 Back")

            choice = input("Enter choice: ")
            if not choice.isdigit():
                print("Invalid Input")
                continue

            choice = int(choice)

            if choice == 1:
                print("Add Item selected")

            elif choice == 2:
                print("View Menu selected")

            elif choice == 3:
                print("Update Item selected")

            elif choice == 4:
                print("Delete Item selected")

            elif choice == 5:
                break

            else:
                print("Invalid Choice")


                
from database.data import data

class StaffDashboard:

    def __init__(self, user):
        self.user = user
        self.menu_data = data()
        self.menu_file = "database/menu.json"

    def run(self):
        while True:
            print("\n===== STAFF DASHBOARD =====")
            print("Welcome", self.user["name"])
            print("1 View Menu")
            print("2 Take Order")
            print("3 View Orders")
            print("4 Logout")

            choice = input("Enter choice: ")

            if not choice.isdigit():
                print("Invalid Input")
                continue

            choice = int(choice)

            if choice == 1:
                print("View Menu selected")
            
            elif choice == 2:
                print("Take Order selected")
            
            elif choice == 3:
                print("View Orders selected")
                
            elif choice == 4:
                print("Logging out...")
                break

            else:
                print("Invalid Choice")


import json
import os

class data:

    def read(self, file):
        if not os.path.exists(file):
            return []

        with open(file, "r") as f:
            try:
                return json.load(f)
            except (json.JSONDecodeError, FileNotFoundError):
                return []

    def write(self, file, data):
        with open(file, "w") as f:
            json.dump(data, f, indent=4)
