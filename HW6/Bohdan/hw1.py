user_number1 = float(input('Enter first number\n>>>'))
user_number2 = float(input('Enter second number\n>>>'))


def search_of_great_value(num1, num2):
    """
    The function selects and return
     a large from two numbers
    :param num1: float
    :param num2: float
    :return: float
    """
    if num1 == num2:
        print(f'First number {num1} and second number {num2} are the same')
        return num1
    if num1 > num2:
        print(f'First number {num1} is greater than the second number {num2}')
        return num1
    else:
        print(f'Second number {num2} is greater than the first number {num1}')
        return num2


print(search_of_great_value(user_number1, user_number2))
