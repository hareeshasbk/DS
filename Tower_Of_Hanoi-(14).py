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

