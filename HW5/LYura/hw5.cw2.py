 def enough(cap, on, wait):
    if cap - (on + wait) >1:
        return 0
    else:
        return (on + wait) - cap
