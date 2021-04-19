numbers_div_2 = []
numbers_div_3 = []
other_numbers = []

for number in range (1, 10):
    if number % 2 == 0:
        numbers_div_2.append(number)
    elif number % 3 == 0:
        numbers_div_3.append(number)
    else:
        other_numbers.append(number)

print(f"Numbers that are divisible by 2: {numbers_div_2}")
print(f"Numbers that are divisible by 3: {numbers_div_3}")
print(f"Numbers that are not divisable by 2 and 3: {other_numbers}")