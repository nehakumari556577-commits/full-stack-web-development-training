# class Student:
#     def __init__(self):
#         self.__marks=0

#     def set_marks(self,marks):
#         if 0<=marks<=100:
#             self.__marks=marks
#         else:
#             print("invalid marks")

#     def get_marks(self):
#        return self.__marks

# ob=Student()
# ob.set_marks(10)
# print("marks:",ob.get_marks())

class Patient:
    def __init__(self,name,disease):
        self.name=name
        self.__disease =disease
    
    def get_disease(self):
        return self.__disease
    
    def set_disease(self,new_disease):
        self.__disease = new_disease
        print("Disease update successfully")
    
    def show_details(self):
        print("Name:", self.name)
        print("Disease:", self.__disease)

p1=Patient("saloni","flu")
print(p1.get_disease())

p1.set_disease("Cold")

p1.show_details()

