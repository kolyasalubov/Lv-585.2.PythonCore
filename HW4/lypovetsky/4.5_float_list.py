# Task2. Create a list that contains elements of integer type, then use the loop to change the type of these elements to a floating type.

# (Hint: use the built-in float() function).
list1 = [1, 2, 3]
i = len(list1)
while i >= 1:
    print(float(list1[i - 1]))
    i -= 1
