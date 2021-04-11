import re


def enter_password():
    """
    Entering user password and length check password
    user_password = input str
    :return: str
    """
    global user_password
    user_password = input('Enter password.\n >>>')
    if len(user_password) < 6 or len(user_password) > 12:
        print(f'password must be between 6 and 12 characters ')
        enter_password()
    return user_password


def checking_big_letters(password):
    """
    checking uppercase letters
    :param password: str from enter_password
    :return: str or int
    """
    template_look = r"[A-Z]+"
    result = re.findall(template_look, password)
    if len(result) == 0:
        print('Incorrect password format.\nPassword must contain at least one big letter')
        password = 0
    return password


def checking_little_letters(password):
    """
    checking lowercase  letters
    :param password: str from enter_password
    :return: str or int
    """
    template_look = r"[a-z]+"
    result = re.findall(template_look, password)
    if len(result) == 0:
        print('Incorrect password format.\nPassword must contain at least small letter')
        password = 0
    return password


def checking_digit(password):
    """
    check digits
    :param password: str from enter_password
    :return: str or int
    """
    template_look = r"[0-9]+"
    result = re.findall(template_look, password)
    if len(result) == 0:
        print('Incorrect password format.\nPassword must contain at least one digit')
        password = 0
    return password


def checking_symbol(password):
    """
    check $, #, @
    :param password: str from enter_password
    :return: str or int
    """
    template_look = r"[$, #, @]+"
    result = re.findall(template_look, password)
    if len(result) == 0:
        print('Incorrect password format.\nPassword must contain at $, # or @')
        password = 0
    return password


def start():
    enter_password()
    if checking_big_letters(user_password) == 0:
        start()
    elif checking_little_letters(user_password) == 0:
        start()
    elif checking_digit(user_password) == 0:
        start()
    elif checking_symbol(user_password) == 0:
        start()
    return user_password


print('Password must have:\n'
      'At least 1 letter between [a-z] and 1 letter between [A-Z].\n'
      'At least 1 number between [0-9].\n'
      'At least 1 character from [$, #,@].\n'
      'Minimum length 6 characters.\n'
      'Maximum length 16characters.')

print(f'{start()} - good password')
