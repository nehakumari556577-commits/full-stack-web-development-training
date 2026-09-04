
from datetime import datetime

def create_files():    
    data=int(input("enter number of files you want to create"))

    if  data <=1 or data <= 20:
        now = datetime.now().strftime("%H_%M_%S")
        
        for i in range(1,data+1):
            with open(f"list{i}_{now}.txt", "w") as file:

                file.write("My name is Neha")

    else:
        print("invalid number")

create_files()

