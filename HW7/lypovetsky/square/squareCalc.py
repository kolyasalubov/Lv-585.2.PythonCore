import math

def rectangleSquare(a=0, b=0):
    """
    Returns the square of ​​the rectangle.

        Parametrs:
            a (int): length of the rectangle
            b (int): width of the rectangle

        Returns:
            a (int) * b (int): the square of ​​the rectangle
    """
    a = int(input("Enter the length of the rectangle \n"))
    b = int(input("Enter the width of the rectangle \n"))
    return a * b


def triangleSquare(a=0, h=0):
    """
    Returns the square of ​​the triangle.

        Parametrs:
            a (int): base of the triangle
            h (int): height of the triangle

        Returns:
            1/2 * a (int) * h (int): the square of ​​the triangle
    """
    a = int(input("Enter the base of the triangle \n"))
    h = int(input("Enter the height of the triangle \n"))
    return 1/2 * a * h


def circleSquare(r=0):
    """
    Returns the radius of the circle.

        Parametrs:
            r (int): radius of the circle

        Returns:
            Pi * pow(r (int), 2): the radius of the circle up to two decimal places
    """
    r = int(input("Enter the radius of the circle \n"))
    return round(math.pi * math.pow(r, 2), 2)
