student1={}

student1["name"]=input("\nplease enter your name").title()
student1["id"]=input("please enter your id").strip().zfill(18)
student1["address"]=input("please enter your address").capitalize()

student2={}

student2["name"]=input("\nplease enter your name").title()
student2["id"]=input("please enter your id").strip().zfill(18)
student2["address"]=input("please enter your address").capitalize()

print("student details")
print("name:",student1["name"])
print("id:",student1["id"])
print("address:",student1["address"])

print("student details")
print("name:",student2["name"])
print("id:",student2["id"])
print("address:",student2["address"])

print(student1==student2)