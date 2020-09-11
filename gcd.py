# program for gcd
x=int(input("enter the 1st number"))
y=int(input("enter the second number"))
if x>y:
    large=x
    small=y
else:
    large=y
    small=x
for i in range(1,small+1):
    if(large%i==0) and(small%i==0):
        gcd=i
        
print(gcd)