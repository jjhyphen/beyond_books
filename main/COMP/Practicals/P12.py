x=int(input("Enter the "))
n=int(input("Enter the precision?"))
i=1
pow=1
Sum=0
fact=1
while i<=n:
    pow*=x
    fact*=i
    Sum+=pow/fact
    i+=1
print("Sum =",1+Sum)    