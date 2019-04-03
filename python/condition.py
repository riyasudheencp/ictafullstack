# a=int(input("enter number"))
# if(a!=0):

#     if(a%2==0):
#         print("even")
#     else:
#         print("odd")
# else:
#     print("zero")
a=int(input("enter 1number"))
b=int(input("enter 2 number"))
c=int(input("enter 3 number"))
if(a>b):
    if(a>c):
        print("largest is",a)
    else:
        print("largest is",c)
elif(b>c):
    print("largest is",b)
else:
    print("largest is",c)