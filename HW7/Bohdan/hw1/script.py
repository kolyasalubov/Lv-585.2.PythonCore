from math import pow
from math import pi


def rectangle_area():
    """
    The function calculates the area of a rectangle

    :return:float
    """
    a = float(input('Enter side length A\n>>>'))
    b = float(input('Enter side length B\n>>>'))
    s = a * b
    print(f'Rectangle area  {s}')
    return s


def triangle_area():
    """
    The function calculates the area of a triangle

    :return: float
    """
    # Heron's formula
    # a = float(input('Enter side length A\n>>>'))
    # b = float(input('Enter side length B\n>>>'))
    # c = float(input('Enter side length C\n>>>'))
    # p = (a + b + c) / 2
    # s = pow((p * (p - a) * (p - b) * (p - c)), 0.5)

    a = float(input('Enter side length a\n>>>'))
    h = float(input('Enter side height h\n>>>'))
    s = 0.5 * a * h
    print(f'triangle area {s}')
    return s


def circle_area():
    """
    The function calculates the area of a circle

    :return: float
    """
    r = float(input('Enter radius\n>>>'))
    s = pi * pow(r, 2)
    print(f'Circle area {s}')
    return s



