# In the range from 1 to 10 determine
# 1) even numbers that are divisible by 2,
# 2) odd numbers, which are divisible by 3,
# 3) numbers that are not divisible by 2 and 3.

my_range = list(range(1, 10))
evenNums = []
oddNums = []
numsNotDivedBy2And3 = []

# 1) even numbers that are divisible by 2,
for i in my_range:
    if my_range[i-1] % 2 == 0:
        # print(f"i: {i}")
        evenNums.append(my_range[i-1])
    else:
        i += 1


# 2) odd numbers, which are divisible by 3,
for i in my_range:
    if my_range[i-1] % 3 == 0:
        # print(f"i: {i}")
        oddNums.append(my_range[i-1])
    else:
        i += 1


# 3) numbers that are not divisible by 2 and 3.
for i in my_range:
    if my_range[i-1] % 2 != 0 and my_range[i-1] % 3 != 0:
        # print(f"i: {i}")
        numsNotDivedBy2And3.append(my_range[i-1])
    else:
        i += 1

print(numsNotDivedBy2And3)
