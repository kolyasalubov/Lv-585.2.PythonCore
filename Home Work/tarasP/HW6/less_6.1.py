# Task1. In the range from 1 to 10 determine 
# even numbers that are divisible by 2,
# odd numbers, which are divisible by 3,
# numbers that are not divisible by 2 and 3.


numDiv_2 = []
numDiv_3 = []
other = []

for number in range (1, 10):
    if number % 2 == 0:
        numDiv_2.append(number)
    elif number % 3 == 0:
        numDiv_3.append(number)
    else:
        other.append(number)
print(f"Numbers that are divisible by 2: {numDiv_2}")
print(f"Numbers that are divisible by 3: {numDiv_3}")
print(f"Numbers that are not divisable by 2 and 3: {other}")
