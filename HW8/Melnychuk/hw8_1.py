import math

class Polygon:
    def __init__(self, number_of_sides):
        self.number_of_sides = number_of_sides
        self.sides = [0 for i in range(number_of_sides)]

    def inputSides(self):
        self.sides = [float(input("Enter side "+str(i+1)+" : ")) for i in range(self.number_of_sides)]

    def dispSides(self):
        for i in range(self.number_of_sides):
            print("Side",i+1,"is",self.sides[i])

class Diamond(Polygon):
    def __init__(self):
        Polygon.__init__(self, 1)
        self.alpha = 0

    def input_alpha(self):
        self.alpha = float(input("Enter angle alpha in degrees: "))
    
    def square(self):
        side_of_diamond = float(self.sides.pop(0))
        alpha = self.alpha
        area = math.pow(side_of_diamond, 2) * math.sin(math.radians(alpha))
        print(f"Square of diamond = {area:.2f}")

    
D1 = Diamond()

D1.inputSides()
D1.input_alpha()
D1.square()
