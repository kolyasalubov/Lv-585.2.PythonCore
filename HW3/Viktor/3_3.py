first_user_var = input("Enter first variable: ")
second_user_var = input("Enter second variable: ")
print(f"First variable: {first_user_var}\nSecond variable: {second_user_var}")
first_user_var, second_user_var = second_user_var, first_user_var
input("Press enter to change content in variables")
print(f"First variable: {first_user_var}\nSecond variable: {second_user_var}")
