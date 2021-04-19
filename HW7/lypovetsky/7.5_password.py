# Write a Python program to check the validity of a password (input from users).

# Validation:
# At least 1 letter between[a-z] and 1 letter between[A-Z].
# At least 1 number between[0-9].
# At least 1 character from [$#@].
# Minimum length 6 characters.
# Maximum length 16 characters.

import re

password = input("Enter your password:\n")

if re.match("^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[$#@])(?=.{6,16}$).*", password):
    print("Nice pass! Psss, I won't tell anyone ;)")
else:
    print("Password is not valid. Check if you have:"
          """
    At least 1 letter between[a-z] and 1 letter between[A-Z].
    At least 1 number between[0-9].
    At least 1 character from [$#@].
    Minimum length 6 characters.
    Maximum length 16 characters.
          """
          )
