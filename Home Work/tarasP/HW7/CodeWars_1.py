import math
def distance(x1, y1, x2, y2):
    dist = ((x1+y1) - (x2+y2))**0.5
    return round(dist, 2)