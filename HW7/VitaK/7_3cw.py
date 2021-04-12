def solution(number):
    list1= [b for b in range (1,number) if b % 3 == 0 or b % 5 == 0]
    return sum(list1)
