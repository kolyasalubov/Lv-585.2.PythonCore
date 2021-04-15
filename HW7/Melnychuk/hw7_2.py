import re

password = input("Enter your password: ")

lenth_of_password = len(password)

def capital_letters(password):
    cap = re.findall("[A-Z]", password)
    while cap == []:
        print("Must be capital letter in your password")
        password = input("Please enter with capital letter: ")
        cap = re.findall("[A-Z]", password)
        if cap != []:
            break    
    return password

def lowercase_letters(password):
    low = re.findall("[a-z]", password)
    if low != []:
        return password
    else:
        while low == []:
            print("Must be low letter in you password")
            password = input("Please enter with low letter: ")
            low = re.findall("[a-z]", password)
            if low != []:
                break
        return password

def numbers(password):
    num = re.findall("[0-9]", password)
    if num != []:
        return password
    else:
        while num == []:
            print("Must be number in your password")
            password = input("Please enter with number: ")
            num = re.findall("[0-9]", password)
            if num != []:
                break
        return password

def symbols(password):
    sym = re.findall("[$#@]", password)
    if sym != []:
        return password
    else:
        while sym == []:
            print("Must be symbol in your password")
            password = input("Please enter with @ or # or $: ")
            sym = re.findall("[$#@]", password)
            if sym != []:
                break
        return password

while lenth_of_password < 6 or lenth_of_password > 16:
    print("from 6 to 16")
    password = input("Enter one more: ")
    lenth_of_password = len(password)
    if lenth_of_password >= 6 and lenth_of_password <= 16:
        break

capital_letters(password)
lowercase_letters(password)
numbers(password)
symbols(password)

print("Thank you! Yor password saved!")



        
    