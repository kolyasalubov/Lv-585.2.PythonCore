def count_positives_sum_negatives(arr):
    countpos = 0
    countneg = 0
    for i in arr:
        if i >0:
        countpos +=1
        if i <0:
            countneg = countneg + i
    else:
        []
    return([countpos, countneg])
