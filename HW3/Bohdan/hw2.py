number = int(input('Enter a four-digit natural number.\n>>>'))
# number = 1235
fix = list(str(number))


def multiplication():
    result = 1
    for i in range(int(len(fix))):
        result *= int(fix[i])
    print('multiplication:', result)


def reverse():
    n_list = list(fix)
    n_list.reverse()
    n2 = "".join(n_list)
    print('reverse number:', n2)


def sort():
    n_list = list(fix)
    n_list.sort()
    n2 = "".join(n_list)
    print('sort number:', n2)


if len(fix) != 4:
    print('Error: the number must be four digits')
else:
    multiplication()
    reverse()
    sort()
