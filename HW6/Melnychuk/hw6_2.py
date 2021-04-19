def rectangle_square(lenth_a, lenth_b):
    rec_square = lenth_a * lenth_b
    return print(f"Square of rectangle: {rec_square}")

def triangle_square(height, base):
    tr_square = (height * base) / 2
    return print(f"Square of triangle: {tr_square}")

def circle_square(radius):
    PI = 3.14
    cir_square = PI * radius ** 2
    return print(f"Square of circle: {cir_square}")

def choice(user_choice):
    if user_choice == 1:
        lenth_a = int(input("Enter first side of rectangle: "))
        lenth_b = int(input("Enter second side of rectangle: "))
        return rectangle_square(lenth_a, lenth_b)
    elif user_choice == 2:
        height = int(input("Enter height of triangle: "))
        base = int(input("Enter base of triangle: "))
        return triangle_square(height, base)
    elif user_choice == 3:
        radius = int(input("Enter radius of circle: ")) 
        return circle_square(radius)
    

print("""Please, choose what you need to calculate:
             1 - for rectangle square
             2 - for triangle square
             3 - for circle square""")

user_choice = int(input("Enter number: "))

choice(user_choice)

print("Thank you! Good luck!")