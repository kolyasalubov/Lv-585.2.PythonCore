from calculator import user_sum
from calculator import user_difference
from calculator import user_multiplication
from calculator import user_division


def choice_operation():
    """
    Choice user function
    :return: result function
    """
    user_choice = int(input('1 - calculate the sum of numbers,\n'
                            '2 - calculate the difference of numbers\n'
                            '3 - calculate the multiplication of numbers\n'
                            '4 - calculate division of numbers\n'
                            'Enter menu item\n>>> '))

    if user_choice == 1:
        print(user_sum(*create_user_list()))
    elif user_choice == 2:
        print(user_difference(*create_user_list()))
    elif user_choice == 3:
        print(user_multiplication(*create_user_list()))
    elif user_choice == 4:
        print(user_division(*create_user_list()))
    else:
        print('Menu item not found')
        choice_operation()


def create_user_list():
    """
    Create user number list for calculate
    :return: list[float,]
    """
    user_nums = []
    num = (input('Enter number for list, \n'
                 'to finish entering numbers enter stop \n>>>'))
    while num != 'stop':
        user_nums.append(float(num))
        num = (input('Enter number for list, \n'
                     'to finish entering numbers enter stop \n>>>'))
    return user_nums


choice_operation()
