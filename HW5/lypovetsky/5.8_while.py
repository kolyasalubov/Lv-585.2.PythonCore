# Write a script that checks the login that the user enters.
# If the login is "First", then greet the users. If the login is different, send an error message.
# (need to use loop while)

login = input("Enter a login:\n")

while login == "First":
    print(f"Hello, {login}!")
    break

while login != "First":
    print(f"Error. Please, try again")
    break
