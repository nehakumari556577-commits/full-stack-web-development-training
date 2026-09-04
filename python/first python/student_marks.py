hindi=int(input("please enter your hindi marks"))
english=int(input("pease enter your english marks"))
maths=int(input("pease enter your maths marks"))
science=int(input("pease enter your science marks"))

total=hindi+english+maths+science

percentage =(total/400)*100

print("total marks:",total)
print("percentage:",percentage)

if percentage>=60:
    print("pass")
else:
    print("failled")