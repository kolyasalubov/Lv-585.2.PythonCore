def Dobutok():
    n1 = int(input("Введите целое число: "))
    suma = 0
    while n1 > 0:
        digint = n1 % 10
        if digint != 0:
            suma += digint
        n1 = n1 // 10
    print(suma)
Dobutok()

