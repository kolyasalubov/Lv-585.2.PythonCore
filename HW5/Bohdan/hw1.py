first_number = int(input('Enter first number\n>>>'))
last_number = int(input('Enter last number\n>>>'))
list_numbers = []
list_even_numbers = []
list_odd_numbers = []
list_other_numbers = []


def to_generate_list(start, stop):
    """
    To generate list number for next operations
    :param start: int , first number list
    :param stop: int, last number list
    :return: number list
    """

    for i in range(start, stop+1, 1):
        list_numbers.append(i)
    return list_numbers


def sampling_even_numbers():
    """
    a sample of even numbers that are divisible by 2
    :input: list_numbers
    :return: number list
    """
    for i in list_numbers:
        if i % 2 == 0:
            list_even_numbers.append(i)
    return list_even_numbers


def sampling_odd_numbers():
    """
    a sample of odd numbers, which are divisible by 3
    :input: list_numbers
    :return: number list
    """
    for i in list_numbers:
        if i % 3 == 0:
            list_odd_numbers.append(i)
    return list_odd_numbers


def other_numbers():
    """
       a sample of numbers that are not divisible by 2 and 3
       :input:list_numbers
       :return: number list
       """
    for i in list_numbers:
        if i % 2 != 0 and i % 3 != 0:
            list_other_numbers.append(i)
    return list_other_numbers


def go():
    to_generate_list(first_number, last_number)
    sampling_even_numbers()
    sampling_odd_numbers()
    other_numbers()
    print(f'list numbers\n{list_numbers}')
    print(f'list of even numbers that are divisible by 2\n{list_even_numbers}')
    print(f'list of odd numbers, which are divisible by 3\n{list_odd_numbers}')
    print(f'list other numbers that are not divisible by 2 and 3\n{list_other_numbers}')


if first_number > last_number:
    first_number, last_number = last_number, first_number
else:
    go()
