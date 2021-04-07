# Task1. Write a function that returns the largest number of two numbers 
# (use DocStrings documentation strings in the function).

numA = float(input("input numA: "))
numB = float(input("input numB: "))

def Lar_Num():
    """
    Function: MyFunc
    input parameter: (none)
    type input parameter: (float)
    return largest number
    """
    if numA < numB:
        print("numB is large: ", numB)
    elif numA>numB:
        print("numA is large: ", numA)
    
Lar_Num()