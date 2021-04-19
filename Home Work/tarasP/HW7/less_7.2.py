# Task2. Write a program that calculates the square of ​​a rectangle, triangle and circle 
# (write three functions to calculate the square, and call them in the main program depending on the user's choice).

# Задача2. Напишите программу, которая вычисляет площу прямоугольника, треугольника и круга.
# (напишите три функции для вычисления площі и вызовите их в основной программе в зависимости от выбора пользователя). 
import math

menu_1 = 0
menu_2 = 0
menu_3 = 0

def Circle():
    """
    Function: Circle
    input parameter:
    type input parameter: (float)
    return: Area of a circle 
    """
    pi = float(3.14)
    if menu_3 == 1:
        r = float(input("input radius: "))
        sR = pi * r**2
        print("площади круга через радиус ", sR)
    elif menu_3 == 2:
        d = float(input("input diameter"))
        sD = d**2 / 4 * pi
        print("площади круга через диаметр ", sD)
    elif menu_3 == 3:
        L = float(input("input dlinu okru*noisti "))
        sL = L**2 / 4 *pi
        print("Площадь круга через длину окружности ", sL)
    else:
        pass



def Triangle():
    """
    Function: Triangle
    input parameter: (none)
    type input parameter: (float)
    return: Area of a Triangle 
    """
    if menu_2 == 1:
        def Triangle_2_1():
            kut = float(input("kut v gradusah: "))      # = 30 - в градусах
            k = math.radians(kut)                       # = переводить в радіани
            a = float(input("storona A = "))            # = сторона 9
            b = float(input("storona B = "))            # = сторона 8
            S = 0,5 * a * b * math.sin(k)
            print("Площадь треугольника через две стороны и угол между ними = ", S) # відповідь = (0, 179.99999999999997) питання полягає в тому: чому в мене на 100 більше і відповідь в такому форматі ?
        Triangle_2_1()
    elif menu_2 == 2:
        def Triangle_2_2():
            a = float(input("osnova = "))
            h = float(input("vusota = "))
            S = 0,5 * a * h
            print("Площадь треугольника через основание и высоту = ", S)
        Triangle_2_2
    elif menu_2 == 3:
        def Triangle_2_3():
            a = float(input("storona A = "))
            b = float(input("storona B = "))
            c = float(input("storona C = "))
            r = float(input("radius opisanoi okru*nosti = "))
            S = (a * b * c) / (4 * r)
            print("Площадь треугольника через описанную окружность и стороны = ", S)
        Triangle_2_3()
    elif menu_2 == 4:
        def Triangle_2_4():
            a = float(input("storona A = "))
            b = float(input("storona B = "))
            c = float(input("storona C = "))
            r = float(input("radius vpisanoi okru*nosti = "))
            S = r * (a + b + c) / 2
            print("Площадь треугольника через вписанную окружность и стороны = ", S)
        Triangle_2_4()
    elif menu_2 == 5:
        def Triangle_2_5():
            a = float(input("storona A = "))
            kut_A = float(input("kut v gradusah: "))
            kut_B = float(input("kut v gradusah: "))
            k_A = math.radians(kut_A)
            k_B = math.radians(kut_B)
            S = a**2 / 2 * (math.sin(k_A) * math.sin(k_B)) / math.sin(180 - (kut_A + kut_B))
            print("Площадь треугольника по стороне и двум прилежащим углам = ", S)
        Triangle_2_5()
    elif menu_2 == 6:
        def Triangle_2_6():
            a = float(input("storona A = "))
            b = float(input("storona B = "))
            c = float(input("storona C = "))
            p = (a + b + c) / 2 # pluperimtr
            S = math.sqrt(p) * (p - a) * (p - b) * (p - c)
            print("Формула Герона для вычисления площади треугольника", S)
        Triangle_2_6()
    else:
        pass

def Rectangle():
    """
    Function: Rectangle
    input parameter: (none)
    type input parameter: (float)
    return: Area of a Rectangle 
    """
    if menu_1 == 1:
        def Rectangle_1_1():
            a = float(input("длина = "))
            b = float(input("ширина = "))
            S = a * b
            print("Площадь прямоугольника = ", S)
        Rectangle_1_1()
    elif menu_1 == 2:
        def Rectangle_1_2():
            a = float(input("длина = "))
            b = float(input("ширина = "))
            P = (a + b) * 2
            print("Периметр прямоугольника = ", P)
        Rectangle_1_2
    else:
        pass


def menu():
    """
    Function: menu
    input parameter: (none)
    type input parameter: (integer)
    return: menu 
    """
    print("1. Прямокутник\n2.трикутник\n3.круг")
    menu_Ins_Number = int(input("###: "))
    if menu_Ins_Number == 1:
        print("1.1 Площадь прямоугольника\
        \n1.2 Периметр прямоугольника")
        global menu_1
        menu_1 = int(input("###: "))
        Rectangle()
    elif menu_Ins_Number == 2:
        print("2.1 Площадь треугольника через две стороны и угол между ними\
        \n2.2 Площадь треугольника через основание и высоту\
        \n2.3 Площадь треугольника через описанную окружность и стороны\
        \n2.4 Площадь треугольника через вписанную окружность и стороны\
        \n2.5 Площадь треугольника по стороне и двум прилежащим углам\
        \n2.6 Формула Герона для вычисления площади треугольника")
        global menu_2
        menu_2 = int(input("###: "))
        Triangle()
    elif menu_Ins_Number == 3:
        print("3.1 площади круга через радиус\
        \n3.2 площади круга через диаметр\
        \n3.3 Площадь круга через длину окружности")
        global menu_3
        menu_3 = int(input("###: "))
        Circle()
menu()
