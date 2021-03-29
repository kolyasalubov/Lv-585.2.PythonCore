enter_number = int(input('Enter number:'))
number1 = 0
number2 = 1
if enter_number == 0: 
    print (0)
else :
    print(number1, number2, end=' ')
    for number in range (enter_number):
        number = number1 + number2
        number1 = number2
        number2= number
        if number > enter_number:
            break
        print (number, end=' ')
