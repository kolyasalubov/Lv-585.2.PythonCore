import less_8_1
#num = input("1: Rectangle;\n2: Triangle;\n3: Circle;\nVuberit punkt: ")

num = 0
num = input("1: Rectangle;\n2: Triangle;\n3: Circle;\nVuberit punkt: ")
def Menu(): 
    #num = input("1: Rectangle;\n2: Triangle;\n3: Circle;\nVuberit punkt: ")
    if num == 1:
        a = input("storona A: ")
        b = input("storona B: ")
        less_8_1.Rectangle(a,b)
    elif num == 2:
        h = input("vusota H: ")
        a = input("storona A: ")
        less_8_1.Triangle(h,a)
    elif num == 3:
        r = input("radius R: ")
        less_8_1.Circle(r)

Menu()