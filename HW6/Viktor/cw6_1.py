from math import hypot

def distance(x1, y1, x2, y2):
    distance = hypot(x2-x1, y2-y1)
    return round(distance, 2)


#def distance(x1, y1, x2, y2):
#    distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
#    return round(distance, 2)
