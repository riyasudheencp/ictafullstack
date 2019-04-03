
n=int(input("Enter n"))
Rev=0
while(n>0):
   r=n%10    
   Rev=(Rev*10)+r   
   n=n//10    
print("rev=",Rev)
