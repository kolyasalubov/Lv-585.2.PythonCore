
class Polygon:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def square_polygon(self):
        s = self.a * self.b
        return s


class Rectangle(Polygon):
    pass


m1 = Rectangle(20, 20).square_polygon()

print(m1)
