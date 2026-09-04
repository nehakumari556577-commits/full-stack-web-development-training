name = input("enter your name")

hindi = int(input("enter your hindi marks"))
english = int(input("enter your english marks"))
maths = int(input("enter your maths marks"))
science = int(input("enter your science marks"))
computer = int(input("enter your computer marks"))

total = hindi+english+maths+science+computer
percentage=total/500*100

print("student name:",name)
print("total marks:",total)
print("percentage:",percentage)