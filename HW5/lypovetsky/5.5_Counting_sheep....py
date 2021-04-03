# https://www.codewars.com/kata/counting-sheep-dot-dot-dot/train/python
def count_sheeps(sheep):
    count = 0
    for i in sheep:
        if i == True:
            count += i

    return count
