# Напишіть скрипт, який обчислює площу прямокутника a*b, площу трикутника 0.5*h*a, площу кола pi*r**2 і цей скрипт використати в іншому модулі, в якому ми запитуємо користувача площу якої фігури він хоче обчислити.

# (для виконання завдання необхідно імпортувати  модуль math, а з нього функцію pow() та значення змінної пі, модуль1, який містить три функції для знаходження площ, модуль2, в якому імпортований модуль1 і виконується основна логіка програми).
from square import squareCalc

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
            return squareCalc.rectangleSquare()
        elif x == 2:
            trigger = True
            return squareCalc.triangleSquare()
        elif x == 3:
            trigger = True
            return squareCalc.circleSquare()
        else:
            print("Wrong! \nPlease select number from 1 to 3 \n")

# print(squareSelect())
