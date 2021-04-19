# https://www.codewars.com/kata/count-of-positives-slash-sum-of-negatives
def count_positives_sum_negatives(arr):
    positive = 0
    negatives = 0

    if arr == []:
        return []
    else:
        for i in arr:
            if i > 0:
                print(f"if i > 0: {i}")
                positive += 1
            else:
                print(f"if i < 0: {i}")
                negatives += i
        return list(map(int, (str(positive), str(negatives))))


print(count_positives_sum_negatives(
    []))
