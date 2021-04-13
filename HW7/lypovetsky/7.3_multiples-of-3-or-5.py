# https://www.codewars.com/kata/multiples-of-3-or-5
def solution(number):
    num = 0
    for i in range(3, number):
        if i % 3 == 0:
            num += i
        elif i % 5 == 0 and not i % 3 == 0:
            num += i

    return num


# print(solution(10))
