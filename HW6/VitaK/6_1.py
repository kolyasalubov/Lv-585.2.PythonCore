def largest_number():
    '''
    This function compares 2 entered numbers and 
    determines a larger number or equality of numbers 

    '''
    number1 = int(input('Enter first number:'))
    number2 = int(input('Enter second number:'))
    
    if number1 == number2:
        return f'The numbers are equal '
    elif number1 > number2:
        return f'The largest number is {number1}'
    else :
        return f'The largest number is {number2}'
    

print (largest_number ())     
