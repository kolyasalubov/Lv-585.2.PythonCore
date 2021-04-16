# Task2. Write a script that checks the login that the user enters. 
# If the login is "First", then greet the users. If the login is different, send an error message. 
# (need to use loop while)

loginUser = str(input("login: "))
logined = str("First")

while loginUser == logined:
    print("Hello ", logined)
    break
else:
    print("Login is invalid")