# Program :8
# Python program to implement insertion sort

def Read():
    a=[]
    n=int(input("Enter size of list:"))
    for i in range(n):
        x=int(input(f"Enter element {i} : "))
        a.append(x)
    print("Original list",a)
    return a,n

def Insertion_Sort(a,n):
    for i in range(n):
        key=a[i]
        j=i-1
        while j>=0 and key<a[j]:
            a[j+1]=a[j]
            j-=1
            a[j+1]=key
    return a
a,n=Read()
a=Insertion_Sort(a,n)
print("After the insertion Sort:",a)

# Time and Space: 0(n^2), 0(1)
