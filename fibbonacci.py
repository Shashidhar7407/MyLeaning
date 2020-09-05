
x=0
y=1
n=int(input("enter the number of fibonacci series required"))
i=0
if(n<=0):
    print("invalid input")
elif(n==1):
    print(1)
else:
        print(x)
        print(y)
        for i in range(n-2):
            z=x+y
            print(z)
            temp=x
            x=y
            y=z
            i+=1


