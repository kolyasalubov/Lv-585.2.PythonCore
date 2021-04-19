def solution(number):
    num = 0
    for a in range(3, number):
        if a % 3 == 0:
            num += a
        elif a % 5 == 0 and not a % 3 == 0:
            num += a

    return num