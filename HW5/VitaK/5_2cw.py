def enough(cap, on, wait):
    return on + wait-cap if on + wait > cap else (0)
