def count_sheeps(sheep):
    wordfreq = 0
    for w in sheep:
        if w == True:
            wordfreq += 1
        else:
            pass
    return(wordfreq)
