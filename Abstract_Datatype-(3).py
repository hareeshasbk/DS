# Program :3
# Python programme to implement Abstract data type

class Student:
    
    def getStudentDetails(self):
        self.name=input("Enter your name:")
        self.rollno=int(input("Enter your roll no:"))
        self.pms=int(input("Enter PMS marks:"))
        self.ds=int(input("Enter Data Structures of Py Marks:"))
        self.os=int(input("Enter the Operating System marks:"))
        self.maths=int(input("Enter Maths marks:"))

    def Result(self):
        self.percentage=(self.pms+self.ds+self.os+self.maths)/400*100
        print("Name:",self.name)
        print("Roll No:",self.rollno)
        print("Percentage:",self.percentage,"%")
        
s1=Student()
s1.getStudentDetails()
s1.Result()

s1.ds+=5
s1.os+=10
s1.Result()
