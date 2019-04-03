n=int(input("Enter year"))
if(n%4==0):
    print("leapyear")
elif(n%400==0):
    print("leapyear")
else:
    print("not leapyear")