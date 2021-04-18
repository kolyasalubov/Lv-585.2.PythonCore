# https://www.codewars.com/kata/double-char/train/python
def double_char(s):
    double_s = ""
    for i in s:
        double_s += i + i
    return double_s


print(double_char("Hello World"))
