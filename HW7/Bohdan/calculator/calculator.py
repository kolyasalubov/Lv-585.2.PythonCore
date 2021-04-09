def user_sum(*args):
    """
    calculate the sum of numbers
    :param args: list[float,] nums
    :return: float number
    """
    su = 0
    for i in args:
        su += i
    return su


def user_difference(n, *args):
    """
    calculate the difference of numbers
    :param n: first number list
    :param args: last number list
    :return: float number
    """
    diff = n
    for i in args:
        diff -= i
    return diff


def user_multiplication(*args):
    """
    calculate the multiplication of numbers
    :param args: list[float,] nums
    :return: float number
    """
    multi = 1
    for i in args:
        multi *= i
    return multi


def user_division(n, *args):
    """
    calculate the division of numbers
    :param n: first number list
    :param args: list[float,] nums
    :return: float number
    """
    div = n
    for i in args:
        div /= i
    return div
