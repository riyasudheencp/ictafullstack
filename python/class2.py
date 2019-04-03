class Employ:
    def __init__(self,x,y,z):
        self.ename=x
        self.ecode=y
        self.eslry=z
    def show(self):
        print("Employ name   :",self.ename)
        print("Employ code   :",self.ecode)
        print("Employ salary :",self.eslry)
e1=Employ("Dans","e31",30000)
e1.show()



