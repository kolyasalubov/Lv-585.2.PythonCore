# https://www.codewars.com/kata/will-there-be-enough-space/train/python
def enough(cap, on, wait):
    if cap - on < wait:
        return wait - (cap - on)
    else:
        return 0
