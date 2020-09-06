# program to find the highest number in the series
x=0
y=1
n=int(input("enter the number of to find the highest fibbonacci series"))
i=0
if(n<=0):
    print("invalid input")
elif(n==1):
    print(1)
else:
    for i in range(n-2):
        z=x+y
        temp=x
        x=y 
        y=z
        i+=1
print(z)
