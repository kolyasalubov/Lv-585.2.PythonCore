def compare(first_number, second_number):
    """
    Function compare 
    input parameters: first_number, second_number
    type input parameters - int
    return bigger number
    """
    if first_number > second_number:
        return print(f"Bigger number: {first_number}")
    elif second_number > first_number:
        return print(f"Bigger number: {second_number}")
    else:
        return print("Numbers are equal")

first_number = int(input("Enter first number: "))
second_number = int(input("Enter second nubmer: "))

compare(first_number, second_number)
