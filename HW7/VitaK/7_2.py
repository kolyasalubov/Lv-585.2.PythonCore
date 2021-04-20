import re

password = str(input ('Enter password:'))

result=[(re.findall("[a-z]", password)), (re.findall("[A-Z]", password)),
    (re.findall("[0-9]", password)), (re.findall("[$#@]", password))]


def check_password():

    global password
    global result
    
    #print (password)
    #print(res)

    if len(password) < 6 or len(password) >16:
        return find_problem()
    for a in result:
        if a == [] :
            return find_problem()
    else :
        return "Password is validity"

def find_problem():
    
    global password
    global result
    
    print ("Your password is incorrect.")
    
    if len(password)<6:
        return "Short password. Minimum length 6 characters"
    elif len(password)>16:
        return "Long password. Maximum length 16 characters"
    elif result[0]==[]:
        return "Password must include at least 1 letter between a-z"
    elif result[1]==[]:
        return "Password must include at least 1 letter between A-Z"
    elif result[2]==[]:
        return "Password must include at least number between 0-9"
    else:
        return "Password must include at least 1 character from [$#@]"
    
    
print(check_password())