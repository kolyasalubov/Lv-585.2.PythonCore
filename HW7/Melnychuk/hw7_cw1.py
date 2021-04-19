arr = []

def count_positives_sum_negatives(arr):
    if arr == []:
        return []
    res = []
    pos = []
    sum = 0
    for i in arr:
        if i > 0:
            pos.append(i)
        elif i < 0:
            sum += i
        n = len(pos) 
    res = [n, sum]
    return res

count_positives_sum_negatives(arr)



