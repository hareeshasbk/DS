# Program :7
# Python programme to implement selection sort

def Read():
    a=[]
    n=int(input("Enter size of list:"))
    for i in range(n):
        x=int(input(f"Enter element {i} : "))
        a.append(x)
    return a,n

def Selection_Sort(a,n):
    for i in range(n):
        min=i
        for j in range(i+1,n):
            if a[j]< a[min]:
                min= j
        a[min],a[i]=a[i],a[min]
    return a

a,n=Read()
a = Selection_Sort(a,n)
print("Sorted array is:", a)


    

    

    