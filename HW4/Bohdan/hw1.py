number = int(input('Enter number\n>>>'))

factorial = 1

for i in range(number):
    i += 1
    factorial *= i
    # print(i, factorial)

print(factorial)
