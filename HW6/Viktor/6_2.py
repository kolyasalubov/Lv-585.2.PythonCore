def rectangle_area(a, b):
    return a * b

def triangle_area(a, h):
    return (a*h)/2

def circle_area(r):
    return 3.14*r**2

def area():
    print("Choose the figure which you know to the area of")
    x = int(input("Rectangle press: 1 \nTriangle press: 2 \nCircle press: 3\n"))
    if x == 1:
        a = float(input("Length a = "))
        b = float(input("Length b = "))
        print("Area of rectangle =", rectangle_area(a, b))
    elif x == 2:
        a = float(input("Length a = "))
        h = float(input("Length h = "))
        print("Area of triangle =", triangle_area(a, h))
    elif x == 3:
        r = float(input("Length r = "))
        print("Area of circle =", circle_area(r))
    return "Good job)"

print(area())
