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
    a = float(input('Enter side length A\n>>>'))
    b = float(input('Enter side length B\n>>>'))
    c = float(input('Enter side length C\n>>>'))
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print(f'triangle area {s}')
    return s


def circle_area():
    """
    The function calculates the area of a circle

    :return: float
    """
    pi = 3.14159265359
    r = float(input('Enter radius\n>>>'))
    s = pi * r ** 2
    print(f'Circle area {s}')
    return s


def menu():
    """
    Start program

    """
    choice = int(input('1 - calculating the area of a rectangle,\n'
                       '2 -  calculating the area of a triangle\n'
                       '3 -  calculating the area of a circle\n'
                       'Enter menu item\n>>> '))

    if choice == 1:
        rectangle_area()
    elif choice == 2:
        triangle_area()
    elif choice == 3:
        circle_area()
    else:
        print('Menu item not found')
        menu()


menu()
