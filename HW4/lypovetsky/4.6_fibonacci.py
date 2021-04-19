# Task3. Print Fibonacci numbers up to the entered number n,
# using cycles.
# (Sequence of Fibonacci numbers 0, 1, 1, 2, 3, 5, 8, 13, etc.)

number = int(input("Enter positive number: "))

fibStart = 0
fibStep = 1
fibEnd = number

while fibEnd > fibStart:
    print(fibStart)
    fibStart += fibStep
    if fibStart > fibEnd:
        break
    print(fibStep)
    fibStep += fibStart
