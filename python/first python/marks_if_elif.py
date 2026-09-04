hindi = int(input("Enter Hindi marks: "))
english = int(input("Enter English marks: "))
maths = int(input("Enter Maths marks: "))
science = int(input("Enter Science marks: "))


total = hindi + english + maths + science
percentage = (total / 400)*100

print("Total Marks:", total)
print("Percentage:", percentage)

if percentage >= 60:
    print("First Division")
elif percentage >= 45:
    print("Second Division")
elif percentage >= 33:
    print("Third Division")
else:
    print("Fail")




