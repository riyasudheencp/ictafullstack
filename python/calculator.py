def add(a,b):
	return a+b
		
def sub(a,b):
	return a-b
	
def mul(a,b):
	return a*b
def div(a,b):
	if b==0:
		print("enter a num not zero")
	else:
		return a/b



a=input("enter the first number")
b=input("enter the second number")
print"1.addition"
print"2 division"
print"3 multiplication"
print"4 substraction"
i=int(input("enter choice"))

if i==1:
	print add(a,b)
elif i==2:
	print div(a,b)
elif i==3:
	print mul(a,b)
elif i==4:
	print sub(a,b)
else:
	print "invalid"

