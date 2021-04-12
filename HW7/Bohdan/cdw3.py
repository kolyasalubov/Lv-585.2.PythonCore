def solution(number):
    user_sum = 0
    for i in range(0, number):
        if i % 3 == 0 or i % 5 == 0:
            user_sum += i
        elif i <= 0:
            return 0
    return user_sum


# print(solution(10))
