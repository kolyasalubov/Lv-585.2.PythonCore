# Task1. Write a script that will calculate the factorial of the entered number  without using recursion.
number = int(input("Enter a positive number\n"))
factorial = 1

while number > 1:
    factorial *= number
    number -= 1

print(f"factorial: {factorial:,}")
