# import calendar
# year=int(input("please enter your year"))
# month=int(input("please enter your month"))

# print(calendar.month(year,month))

import datetime

today = datetime.today()

print("1. Last 1 week")
print("2. Last 6 months")
print("3. Last 1 year")

option = int(input("Enter option: "))

if option == 1:
    print(today - datetime(days=7))

elif option == 2:
    print(today - datetime(days=180))

elif option == 3:
    print(today - datetime(days=365))

else:
    print("Wrong option")






