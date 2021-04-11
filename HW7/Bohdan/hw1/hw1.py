from script import rectangle_area
from script import triangle_area
from script import circle_area


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
