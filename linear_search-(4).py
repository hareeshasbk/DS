# Program :4
# Python programme to implement linear search

A=[]

n=int(input("Enter the size of list:"))

for i in range(n):
    x=int(input(f"Enter {i} element:"))
    A.append(x)

S=int(input("Enter the element to search:"))

flag=0

for i in range(n):
    if S==A[i]:
        flag=1
        break

if flag==1:
    print(f"{S} was found at index {i}")
else:
    print("Not found:")
    
 
#  Time and Space :0(1)




