login_from_user = input("Your login: ")

while login_from_user != "First":
    print("Error! Invalid login")
    login_from_user = input("Enter valid login: ")

if login_from_user == "First":
    print(f"Welcome, {login_from_user}")

