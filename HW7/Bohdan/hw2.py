import re


def enter_password():
    global user_password
    user_password = input('Enter password.\n >>>')
    if len(user_password) < 6 or len(user_password) > 12:
        print(f'password must be between 6 and 12 characters ')
        enter_password()
    return user_password


def checking_big_letters(password):
    template_look = r"[A-Z]+"
    result = re.findall(template_look, password)
    if len(result) == 0:
        print('Incorrect password format.\nPassword must contain at least one big letter')
        password = 0
    return password


def checking_little_letters(password):
    template_look = r"[a-z]+"
    result = re.findall(template_look, password)
    if len(result) == 0:
        print('Incorrect password format.\nPassword must contain at least small letter')
        password = 0
    return password


def checking_digit(password):
    template_look = r"[0-9]+"
    result = re.findall(template_look, password)
    if len(result) == 0:
        print('Incorrect password format.\nPassword must contain at least one digit')
        password = 0
    return password


def checking_symbol(password):
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


print(f'{start()} - good password')
