# Write a function that returns the largest number of two numbers
# (use DocStrings documentation strings in the function)
def largestNum(a, b):
    """
    Returns the largest of two numbers.

        Parametrs:
            a (int): A decimal integer
            b (int): Another decimal integer

        Returns:
            a (int) or b (int): the largest of two numbers
    """
    if a > b:
        return a
    else:
        return b

# print(largestNum(5, 51))
# print(largestNum.__doc__)
