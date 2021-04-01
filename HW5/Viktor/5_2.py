user_login = input("Enter your login: ")

while user_login != "First":
    print("User not found, try again!")
    user_login = input("Enter your login: ")

print(f"Hello, {user_login}")