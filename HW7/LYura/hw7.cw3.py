def solution(number):
    li = []
    i = 1
    while i<number:
        li.append(i)
        i +=1
    loma = []
    for x in li:
        if x %3 == 0 or x %5 == 0:
            loma.append(x)
    return(sum(loma))
    