# Program :2
# Python programme to implement non primitive data type

import array as arr
a=arr.array('i',[])

n=int(input("Enter the size of array:"))

for i in range(n):
    x=int(input(f"Enter the {i} element of array:"))
    a.append(x)

print("Original array:",a)

for i in range(n):
    print(a[i])

