def days_of_the_week():
    """
    Funcion days_of_the_week
    The function shows the day 
    of the week from 1 to 7
    """
    i = input("Enter your number from 1 to 7: ")
    my_dict = {1:"Monday", 
               2:"Tuesday", 
               3:"Wednesday", 
               4:"Thursday", 
               5:"Friday", 
               6:"Saturday", 
               7:"Sunday"}
    try:
        print(my_dict[int(i)])
#        lambda my_dict: my_dict[int(i)]
    except KeyError as k:
        print(str(k) + " not from 1 to 7" )
    except ValueError:
        print("You entered incorrect data.")


days_of_the_week()
