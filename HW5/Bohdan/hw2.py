user_name = "First"
user_login = input("Enter your login:\n>>> ")

while user_login != user_name:
    user_login = input("Invalid login. Please try again\n>>>")

print(f"Hello, {user_login.title()}")
