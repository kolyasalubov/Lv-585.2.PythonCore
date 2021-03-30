# Task2. Create a list that contains elements of integer type, then use the loop to change the type of these elements to a floating type.

# (Hint: use the built-in float() function).
list = [1, 2, 3]
i = len(list)
while i >= 1:
    float(list[i - 1])
    print(float(list[i - 1]))
    i -= 1
