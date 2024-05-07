# Program :1
# python program to illustrate various operations on primitive datatypes:

# operations on integer
 
int1=100
int2=10
print(int1+int2)
print(int1-int2)
print(int1*int2)
print(int1/int2)


# Operations on float

float1=5.2
float2=4.5
print(float1+float2)
print(float1-float2)
print(float1*float2)
print(float1/float2)

# operations on string

string1="Hello, "
string2="How are you?"
print(string1+string2)

# operations on boolean

eligible=True
age=16

if age>18:
    eligible=True

print(eligible)







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
    
    
    
    
    

# Program :3
# Python programme to implement Abstract data type

class Student:
    
    def getStudentDetails(self):
        self.name=input("Enter your name:")
        self.rollno=int(input("Enter your roll no:"))
        self.pms=int(input("Enter PMS marks:"))
        self.ds=int(input("Enter Data Structures of Py Marks:"))
        self.os=int(input("Enter the Operating System marks:"))
        self.maths=int(input("Enter Maths marks:"))

    def Result(self):
        self.percentage=(self.pms+self.ds+self.os+self.maths)/400*100
        print("Name:",self.name)
        print("Roll No:",self.rollno)
        print("Percentage:",self.percentage,"%")
        
s1=Student()
s1.getStudentDetails()
s1.Result()

s1.ds+=5
s1.os+=10
s1.Result()




    
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




# Program :9
# Python program to implement fibonacci series:

def fib(n):
    if n<=1:
        return n
    else:
        return (fib(n-1)+fib(n-2))

n=int(input("Enter the number of fibonacci terms:"))
print("Fibonacci sequence")

for i in range (n):
    print(fib(i))

# Time and Space complexity: 2^N    0(N)





# Program :10
# Python program to implement linked list 
# with insert, delete, search and display operations



class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
class LinkedList:
    def __init__(self):
        self.head=None
        
    def insertAtBeginning(self, x):
        newnode=Node(x)
        newnode.next=self.head
        self.head=newnode
        
    def deleteFirstNode(self):
        temp = self.head
        if temp:
            self.head=temp.next
            temp.next=None
            print("Deleted node value = ",str(temp.data))
        else:
            print("List is empty")
        
    def searchNode(self):
        flag=0
        x=int(input("Enter which node you want to search ="))
        temp=self.head
        
        if(temp):
            while(temp):
                if x==temp.data:
                    flag=1
                    break
                temp=temp.next
            
            if (flag==1):
                print("element found in list")
            else:
                print("list is empty")
    
    def displayList(self):
        temp=self.head
        if(temp):
            print("linkedlist ------->", end=" ")
            while (temp):
                print(str(temp.data) + " ",end="")
                temp=temp.next
        else:
            print("List is empty...")

    def selectionOption(self, ch):
        if ch==1:
            x=int(input("Enter value for Newnode="))
            LL.insertAtBeginning(x)
        elif ch==2:
            LL.deleteFirstNode()
        
        elif ch==3:
            LL.searchNode()
        
        elif ch==4:
            LL.displayList()

if __name__=="__main__":
    LL=LinkedList()
    ch=0
    while ch<=4:
        print("\n\n")
        print("-----------menu---------")
        print("1     insert     ")
        print("2     delete firstnode  ")
        print("3     search    ")
        print("4     display firstnode   ")
        
        ch=int(input("enter your choice= "))
        LL.selectionOption(ch)
        LL.displayList()
        
        
    

# Program :11
# Python program to implement Stack

def Create_Stack():
    STACK=[]
    return STACK

def push(STACK,item):
    STACK.append(item)
    print("Pushed item=",item)

def pop(STACK):
    if(len(STACK)==0):
        print("Stack is empty")
    else:
        print(STACK.pop())

def Select_Option(ch):
    if ch==1:
        x=int(input("Enter the value for push="))
        push(STACK,x)
    else:
        x=pop(STACK)
        print("poped element from stack:",x)

STACK=Create_Stack()
ch=0

while ch<3:
    print("_______STACK_______")
    print(" 1. Push  ")
    print(" 2. Pop  ")
    print(" 3. Exit  ")
    print('-----------------')
    ch=int(input("Enter your choice:"))
    Select_Option(ch)
    print(STACK)

# Time complexity: 0(1)  
# Space complexity: 0(1)





# Program :12
# Python program to implement Bracket matching using stack

def Bracket_Balanced(expr):
    STACK=[]

    for char in expr:
        if char in ['(','{','[']:
            STACK.append(char)
        else:
            if not STACK:
                return False
            current_char=STACK.pop()
            if current_char=='(':
                if char!=')':
                    return False
                
            if current_char=='{':
                if char!="}":
                    return False
            
            if current_char=="[":
                if char!="]":
                    return False
        
    if STACK:
        return False
    return True

if __name__=="__main__":
    expr=input("Enter expression:")
    if Bracket_Balanced(expr):
        print("Balanced")
    else:
        print("Not balanced") 



# Time and Space complexity: 0(n)





# Program :13
# Python program to implement factorial of number

def Fact(n):
    if n==1:
        return 1
    else:
        return n*Fact(n-1)

a=int(input(" Enter the number:"))
print(" Factorial:",Fact(a))

# Time and Space complexity: 0(n)    0(n)




# Program :14
# Python program to implement tower of hanoi

def Tower_Of_Hanoi(n,rodA,rodB,rodC):
    if n==0:
        return
    Tower_Of_Hanoi(n-1,rodA,rodC,rodB)
    print("Move disk",n,'roadA',rodA,"rodB",rodB)
    Tower_Of_Hanoi(n-1,rodC,rodB,rodA)

n=int(input("Enter the no.  of disks:"))
Tower_Of_Hanoi(n,'P','Q','R')




# Program :15
# Python program to implement Queue

def Create_Queue():
    Queue=[]
    return Queue 

def Insert(Queue,item):
    Queue.append(item)

def Delete(Queue):
    if (len(Queue)==0):
        return "Queue is empty"
    else:
        return (Queue.pop(0))

def Select_Option(ch):
    if ch==1:
        x=int(input("Enter the item to insert:"))
        Insert(Queue,str(x))
    elif ch==2:
        print("Delete item:",Delete(Queue))

Queue=Create_Queue()

ch=0

while ch<3:
    print("1 Insert ")
    print("2 Delete")
    print("3 Exit")
    ch=int(input("Enter your choice:"))
    Select_Option(ch)
    print(Queue)





# Program :16
# Python program to implement priority queue 

class Priority_Queue(object):
    def __init__(self):
        self.queue = []

    def __str__(self):
        return ' '.join([str(i) for i in self.queue])

    def isEmpty(self):
        return len(self.queue)==0
    
    def insert(self,data):
        self.queue.append(data) 

    def delete(self):
        try:
            max_val=0
            for i in range(len(self.queue)):
                if self.queue[i]>self.queue[max_val]:
                    max_val=i
            item = self.queue[max_val]
            del self.queue[max_val]
            return item
        except IndexError:
            print()
            exit()


if __name__=='__main__':
    myQueue = Priority_Queue()
    myQueue.insert(20)
    myQueue.insert(10)
    myQueue.insert(40)
    myQueue.insert(30)
    print(myQueue)
    print("Delete from Queue =")
    while not myQueue.isEmpty():
        print(myQueue.delete())




# Program :17
# Python program to implement Binary Search Tree

class Node:
    def __init__(self,key):
        self.left= None
        self.data=key
        self.right=None
        
def insert(node,key):
        if node is None:
            return Node(key)
        
        if key< node.data:
            node.left=insert(node.left,key)
        else:
            node.right=insert(node.right,key)
        return node
    
def inorder(root):
        if root is not None:
            inorder(root.left)
            print(str(root.data)+" ")
            inorder(root.right)

def exists(node,val):
        if val == node.data:
            return True

        if val<node.data:
            if node.left == None:
                return False
            return exists(node.left,val)

        if node.right == None:
            return False
        return exists( node.right,val)

root= None

root = insert(root, 8)
root = insert(root, 3)
root = insert(root, 1)
root = insert(root, 6)
root = insert(root, 7)
root = insert(root, 10)
root = insert(root, 14)
root = insert(root, 4)

print("Inorder =")
inorder(root)


x=int(input("Enter value you want to search:"))
if (exists(root,x)):
    print("Found")
else:
    print("Not Found")



# Program :18
# Python Program to implement depth first search


graph={
  '5':['3','7'],
  '3':['2','4'],
  '7':['8'],
  '2':[],
  '4':['8'],
  '8':[]
}

visited=set()

def dfs(visited,graph,node):
  if node not in visited:
    print(node)
    visited.add(node)
    for neighbour in graph[node]:
      dfs(visited,graph,neighbour)

print("Following is the depth first search")
dfs(visited,graph,'5')




# Program :19
# Python program to implement Hashing

HashTable =[[] for _ in range(10)]

def Hashing(keyvalue):
    return keyvalue % len(HashTable)

def insert(HT, keyvalue, value):
    hash_key = Hashing(keyvalue)
    HT[hash_key].append(value)
    
def Display(HT):
    for i in range(len(HT)):
        print(i, end=" ")
        for j in HT[i]:
            print("---->", end=" ")
            print(j, end="")
    
        print()
        

insert(HashTable, 42, 'Prayag') 
insert(HashTable, 24, 'mathura') 
insert(HashTable, 35, 'Vrindavan') 
insert(HashTable, 17, 'Gokul') 
insert(HashTable, 98, 'Hubli') 
insert(HashTable, 14, 'Belagavi')
insert(HashTable, 10, 'Pune') 

Display(HashTable)

