# def add(a,b):
#     print("sum=",a+b)
# def sub(a,b):
#     print("dif=",a-b)
# def mul(a,b):
#     print("mul=",a*b)
# def div(a,b):
#     return a/b
# x=int(input("enter 1 number"))
# y=int(input("enter 2 number"))
# add(x,y)
# mul(x,y)
# sub(x,y)
# print(div(x,y))
def ree(a):
    n=a
    Rev=0
    while(n>0):
        r=n%10    
        Rev=(Rev*10)+r   
        n=n//10    
    return Rev
x=int(input("enter number"))
print("reverse",ree(x))
