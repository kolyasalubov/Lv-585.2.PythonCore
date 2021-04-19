# Task3. Print Fibonacci numbers up to the entered number n, 
# using cycles. 
# (Sequence of Fibonacci numbers 0, 1, 1, 2, 3, 5, 8, 13, etc.) 

n = input("input number fibonacci: ")
def Fibonacci(n):
    if n in (1, 2):
        return 1
    return Fibonacci(n - 1) + Fibonacci(n - 2)
 
 
print(Fibonacci(10))