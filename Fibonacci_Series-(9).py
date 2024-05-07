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





