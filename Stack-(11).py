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

