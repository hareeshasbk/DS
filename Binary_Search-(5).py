# Program :5
# Python program to implement binary search

def Read():   
    list=[]
    n=int(input("Enter the size of list:"))

    for i in range(n):
        x=int(input(f"Enter {i} element: "))
        list.append(x)
        
    list.sort()
    print("Given list:\n",list)
    return list

def Binary_Search(list,key):

    low=0
    high=len(list)-1
    Found=False
    
    while low<=high and not Found:
        mid=(low+high)//2
        if key==list[mid]:
            Found=True
        elif key>list[mid]:
            low=mid+1
        else:
            high=mid-1
    if Found:
        print("Found")
    else:
        print("Not Found " )


list=Read()

# Binary_Search(list,3)

# or
Binary_Search(list,int(input("Enter the element to find:")))






