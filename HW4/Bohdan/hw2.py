int_list = list(input('Enter numbers: \n>>>'))


def int_to_float():
    float_list = []
    for i in int_list:
        float_list.append(float(i))
    print(f'Float list:\n {float_list}')


int_to_float()
