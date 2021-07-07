fib_range = 4
num = 0
num1 = 0
num2 = 1
counter = 0

while (counter<fib_range):
    print(num1)
    num = num1 + num2
    num1 = num2
    num2 = num
    counter += 1
else:
    print("This is the end for this number:", fib_range)
