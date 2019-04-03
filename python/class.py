class Student:
    def __init__(self,x,y):
        self.name=x
        self.rolno=y
    def print(self):
        print("name : ",self.name)
        print("rolno: ",self.rolno)
        self.age()
    def age(self):
        z=int(input("enter age"))
        print("age is ",z)
s=Student("rahul",20)
s.print()

