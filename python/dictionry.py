b={"welcome":"swagatham",4:"four",3.5:"three"}
print b
b[3.5]="three poin five"
print b
print b.keys()
print b.values()
print b.items()
for i in b:
	print i,b[i]
print b.has_key(5)
print b.get(4)
del b[3.5]
print b
