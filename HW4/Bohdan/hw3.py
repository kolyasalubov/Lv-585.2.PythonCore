fib_list = [0, 1, 1]

user_number = int(input('Enter Fibonacci number:\n>>>'))
# user_number = int(568)


def fibonacci_list():
    i = 2
    while user_number > int(fib_list[i]):
        i += 1
        number = ((fib_list[i-2])+fib_list[i-1])
        if user_number < number:
            break
        fib_list.append(number)
    print(fib_list)


if user_number < 0:
    print('Fibonacci numbers => 0')
elif user_number == 0:
    fib_list = [0]
    print(fib_list)
else:
    fibonacci_list()
