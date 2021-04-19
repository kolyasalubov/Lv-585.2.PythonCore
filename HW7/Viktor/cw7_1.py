def count_positives_sum_negatives(arr):
    if arr == []:
        return []
    count_positives = 0
    sum_negatives = 0
    for x in arr:
        if x > 0:
            count_positives += 1
        elif x < 0:
            sum_negatives += x
    return [count_positives, sum_negatives]
