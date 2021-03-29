user_number = int(input("Enter number: "))
factorial = 1
count = 1

while user_number > 1:
    factorial *= user_number
    user_number -= 1
    count += 1

print(f"Factorial of {count} equals {factorial}")
