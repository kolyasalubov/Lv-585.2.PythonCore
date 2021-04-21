def age():
    """
    Funcion age
    The funcion displays the message
    whether the age is even or odd.
    """
    
    try:
        user_age = int(input("Enter your age: "))
        if user_age <= 0:
            raise TypeError
        elif user_age % 2 == 0:
            print("Your age is even number")
        else:
            print("Your age is odd number")
    except TypeError:
        print("Not a positive number")
    except:
        print("You entered incorrect data.")


age()
