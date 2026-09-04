students = [

    {
        "Name": input("\nPlease Enter Your Name: "),
        "ID": input("Please Enter Your ID: "),
        "Email": input("Please Enter Your Email: "),
    
    "Qulification":{
      "cource name":input("please enter your cource name"),
      "passing year":input("please enter your passing year")
    },
    },
    
    {
        "Name": input("\nPlease Enter Your Name: "),
        "ID": input("Please Enter Your ID: "),
        "Email": input("Please Enter Your Email: "),
    
      "Qulification":{
      "cource name":input("please enter your cource name"),
      "passing year":input("please enter your passing year")
    },
    },

    {
        "Name": input("\nPlease Enter Your Name: "),
        "ID": input("Please Enter Your ID: "),
        "Email": input("Please Enter Your Email: "),
    
     "Qulification":{
      "cource name":input("please enter your cource name"),
      "passing year":input("please enter your passing year")
    }
    }, 
]

print("\n----- STUDENTS DATA -----\n")

print("\nName:", students[0]["Name"])
print("ID:", students[0]["ID"])
print("Email:", students[0]["Email"])
print("Course Name:", students[0]["Qulification"]["cource name"])
print("Passing Year:", students[0]["Qulification"]["passing year"])

print("\nName:", students[1]["Name"])
print("ID:", students[1]["ID"])
print("Email:", students[1]["Email"])
print("Course Name:", students[1]["Qulification"]["cource name"])
print("Passing Year:", students[1]["Qulification"]["passing year"])

print("\nName:", students[2]["Name"])
print("ID:", students[2]["ID"])
print("Email:", students[2]["Email"])
print("Course Name:", students[2]["Qulification"]["cource name"])
print("Passing Year:", students[2]["Qulification"]["passing year"])

print(students)