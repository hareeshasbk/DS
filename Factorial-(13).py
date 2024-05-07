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
