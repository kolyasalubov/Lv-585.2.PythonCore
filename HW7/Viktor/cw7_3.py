def solution(number):
    if number <= 0:
        return 0
    elif number > 0:
        b = []
        for x in range(number):
            if x%3==0 or x%5==0:
                b.append(x)
    return sum(b)
    