# Program :6
# Python programme to implement bubble sort

def Read():
    a=[]
    n=int(input("Enter the size of list:"))
    for i in range(n):
        x=int(input(f"Enter {i} element:"))
        a.append(x)
    print("Original List:",a)
    return a,n

def Bubble_Sort(a,n):
    for i in range(n-1):
        for j in range(n-i-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    print("The sorted list in ascending order:",a)
    
a,n=Read() 
Bubble_Sort(a,n)


# Time and Space: 0(n^2), 0(1)



            
    

