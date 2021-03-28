'''I'm leasy :)'''
import math
num = int(input("Enter your number here:"))
print(math.factorial(int(num)))


'''Other way'''
num = input("Enter a number: ")
factorial = 1
for i in range(1, int(num)+1):
    factorial = factorial * i
print(factorial)
