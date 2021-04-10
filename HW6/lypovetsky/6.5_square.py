# Write a program that calculates the square of ​​a rectangle, triangle and circle
# (write three functions to calculate the square, and call them in the main program depending on the user's choice).
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
    return round(3.141592653589793 * pow(r, 2), 2)


def squareSelect(x=0):
    """
    Returns one of three functions on the user's choice, which calculates the square.

        Parametrs:
            x (int): the menu number of choice

        Returns:
            rectangleSquare() or triangleSquare(), or circleSquare(): function that calculates the selected square
    """
    trigger = False
    print("What do you want to count? \nArea of rectangle (1) \nArea of a triangle (2) \nArea of a circle (3) \n")
    while trigger == False:
        x = int(input())
        if x == 1:
            trigger = True
            return rectangleSquare()
        elif x == 2:
            trigger = True
            return triangleSquare()
        elif x == 3:
            trigger = True
            return circleSquare()
        else:
            print("Wrong! \nPlease select number from 1 to 3 \n")

# print(squareSelect())
