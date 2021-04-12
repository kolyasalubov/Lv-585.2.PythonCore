def enough(cap, on, wait):
    if (cap >= 0) and (on >= 0) and (wait >= 0):
        if (cap-on) >= wait:
            print(f'He can fit all {wait} passengers')
            return 0
        elif (cap-on) < wait:
            print(f"He can't fit {wait-(cap-on)} of the {wait} waiting")
            return wait-(cap-on)
    else:
        return 0
