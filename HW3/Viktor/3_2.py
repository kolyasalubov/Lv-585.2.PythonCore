user_number = input("Enter number from 1000 to 9999: ")
print(f"Multiplication of all digits in the number: \
{int(user_number[0])*int(user_number[1])*int(user_number[2])*int(user_number[3])}")
print(f"Reverse order of digits: {''.join(reversed(user_number))}")
print(f"Digits sorted by increase: {''.join(sorted(user_number))}")
