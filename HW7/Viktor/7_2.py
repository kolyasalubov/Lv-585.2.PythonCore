import re


def check_number(x):
    pattern = re.compile("[0-9]")
    y = pattern.findall(x)
    return y!=[]

def check_lowercase(x):
    pattern = re.compile("[a-z]")
    y = pattern.findall(x)
    return y!=[]

def check_upcase(x):
    pattern = re.compile("[A-Z]")
    y = pattern.findall(x)
    return y!=[]

def check_spez(x):
    pattern = re.compile("[#$@]")
    y = pattern.findall(x)
    return y!=[]

def check_space(x):
    pattern = re.compile("[ ]")
    y = pattern.findall(x)
    return y==[]

def user_psword():
    print("""Enter your password, it must contain a special character:
             a letter [a-z] and a letter [A-Z]
             1 number between [0-9]
             1 character from [$#@]
             Minimum length 6 characters.
             Maximum length 16 characters.
         """)
    while True:
        global x
        x = input()
        if 6<=len(x)<=16 and \
        check_number(x)*check_lowercase(x)*check_upcase(x)*check_spez(x)*check_space(x)==True:
            return "Well done!"
        else:
            print("Password is not correct, try again:")

print(user_psword())
