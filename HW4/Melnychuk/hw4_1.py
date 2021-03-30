number = int(input("Enter number: "))
factorial = 1

if number < 0:
    print("Nubmer must be > 0!!!")
number = int(input("Enter number > 0: "))

while number > 1:
    factorial *= number
    number -= 1
print(f"Factorial = {factorial}")



    




