def count_positives_sum_negatives(arr):
    positives = [a for a in arr if a > 0]
    negatives = [b for b in arr if b < 0]
    list3 = [len(positives), sum (negatives)]
    return [] if arr == [] else list3 
    