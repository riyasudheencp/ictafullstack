def lar(a,b,c):
    if(a>b):
        if(a>c):
            print("largest is",a)
        else:
            print("largest is",c)
    elif(b>c):
        print("largest is",b)
    else:
        print("largest is",c)
x=int(input("enter 1number"))
y=int(input("enter 2 number"))
z=int(input("enter 3 number"))
lar(x,y,z)