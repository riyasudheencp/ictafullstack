def pal(n):
    m=n
    Rev=0
    while(n>0):
        r=n%10    
        Rev=(Rev*10)+r   
        n=n//10
    if(Rev==m):
        print("palindrome")
    else:
        print("not palindrome")
a=int(input("Enter n"))
pal(a)