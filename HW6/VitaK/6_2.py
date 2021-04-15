import math

def square_of_rectangle ():
    side1 = int(input('Enter first side of rectangle:'))
    side2 = int(input('Enter second side of rectangle:'))
    return f'Square of rectangle is {side1*side2}'
    
def square_of_triangle ():
    basis = int(input('Enter basis of triangle:'))
    height = int(input('Enter height of triangle:'))
    return f'Square of triangle is {0.5*basis*height}'
    

def square_of_circle ():
    radius = int(input('Enter radius of circle:'))
    return f'Square of circle is {round((math.pi*radius**2),1)}'
    

def choose_shape():
    choise = int(input('Choose geometric shape 1-rectangle,2-triangle,3-circle :'))
    if choise == 1:
        return square_of_rectangle ()
    elif choise == 2:
        return square_of_triangle()
    elif choise == 3:
        return square_of_circle()
    else: 
        return "Bad input"

print (choose_shape())