import add_subtract
import multiply_divide
def main():
    while True:    
        print("1. add")
        print("2. subtract")
        print("3. multiply")
        print("4. divide")

        option=input("please enter your option")
        first = int(input("Please enter first number: "))
        second = int(input("Please enter second number: "))

        if option.isdigit():
            option=int(option)

            if option==1:
                add_subtract.add_number(first,second)
                              
            elif option==2:
                add_subtract.subtract_number(first,second)
            
            elif option==3:
                multiply_divide.multiply_number(first,second)
                

            elif option==4:
                 multiply_divide.divide_number(first,second)

                 break
        
            else:
                print("invalid option")
                

main()

            
    