name= input("enter student name")

marks ={}

hindi = int(input("enter your hindi marks"))
english = int(input("enter your english marks"))
maths = int(input("enter your maths marks"))
science = int(input("enter your science marks"))
computer = int(input("enter your computer marks"))

total= hindi+english+maths+science+computer

marks["hindi"]=hindi
marks["english"]=english 
marks["maths"]=maths
marks["science"]=science
marks["computer"]=computer

print("total marks",total)
print(marks)