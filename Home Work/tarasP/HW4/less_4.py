# Task1. Write a script that will calculate the factorial of the entered number  without using recursion.

n = int(input("input number: "))
f = 0
if n > 0: f = 1
for i in range(2, n + 1):
    f *= i
print("factorial  = ", f)