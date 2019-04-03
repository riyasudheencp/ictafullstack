a=raw_input("enter the string")

n=0
p=0
k=0
r=0
for i in a:
	if i in "aioueAIOUE":
		n=n+1
	elif i in "bcdfghjklmnpqrstvwxyz":
		p=p+1
	elif i in "":
		k=k+1
	elif i in "?":
		r=r+1
print("the vowel is",n)
print("the constant is",p)
print("the sentence is",k+1)
print("the ?",r)


