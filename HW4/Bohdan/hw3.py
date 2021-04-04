fib_list = [0, 1, 1]
user_number = int(input('Enter Fibonacci number:\n>>>'))


def fibonacci_list():
    """
    This function generate Fibonacci numbers up to user number
    Input : int
    Output: list of Fibonacci numbers
    """
    i = 2
    while user_number > int(fib_list[i]):
        i += 1
        number = ((fib_list[i-2])+fib_list[i-1])
        if user_number < number:
            break
        fib_list.append(number)
    print(f'\nFibonacci numbers up to {user_number} :\n {fib_list}')


if user_number < 0:
    print('Fibonacci numbers => 0')
elif user_number == 0:
    fib_list = [0]
    print(f'\nFibonacci numbers up to {user_number} :\n {fib_list}')
else:
    fibonacci_list()

