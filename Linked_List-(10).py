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

