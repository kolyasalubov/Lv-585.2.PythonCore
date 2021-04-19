import math
import rectangle
import triangle
import circle

def choice(user_choice):
    if user_choice == 1:
        lenth_a = int(input("Enter first side of rectangle: "))
        lenth_b = int(input("Enter second side of rectangle: "))
        rectangle.rectangle_square(lenth_a, lenth_b) 
    elif user_choice == 2:
        height = int(input("Enter height of triangle: "))
        base = int(input("Enter base of triangle: "))
        triangle.triangle_square(height, base)
    elif user_choice == 3:
        radius = int(input("Enter radius of circle: "))
        circle.circle_square(radius)
    

print("""Please, choose what you need to calculate:
             1 - for rectangle square
             2 - for triangle square
             3 - for circle square""")

user_choice = int(input("Enter number: "))

choice(user_choice)

print("Thank you! Good luck!")