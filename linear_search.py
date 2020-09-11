# searching codes 
# linear search
lst=[]
i=0
n=int(input("enter the size of array or list: "))
for i in range(0,n):
    x=int(input())
    lst.append(x)
print(lst)

s=int(input("enter the element to search: "))
for i in range(len(lst)):
    if(lst[i]==s):
        print(i)
    elif(i<len(lst)):
        i+=1
else:
    print("invalid input or element doesnot exists in the list")   







