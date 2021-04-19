import math

def circle_square(radius):
    cir_square = math.pi * pow(radius, 2)
    cir_square = round(cir_square, 2)
    return print(f"Square of circle: {cir_square}")