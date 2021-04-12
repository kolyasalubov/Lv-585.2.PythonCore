# user_input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]
# user_input = []


def count_positives_sum_negatives(arr):
    count = 0
    sum_negativ = 0
    if not arr:
        res = []
        return res
    else:
        for i in arr:
            if i > 0:
                count += 1
            elif i < 0:
                sum_negativ += i
        res = [count, sum_negativ]
    return res


# print(count_positives_sum_negatives(user_input))
