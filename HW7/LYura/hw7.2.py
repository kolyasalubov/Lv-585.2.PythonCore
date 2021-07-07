import re
password = input("Enter string to test: ")
def check(password):
    if re.fullmatch(r'[A-Za-z0-9@#$%^&+=]{6,16}', password):
        print("Password saved")
    else:
        print("Please change your password")
    
check(password)
