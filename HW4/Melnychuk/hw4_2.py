var_from_user = input("Enter numbers: ")

int_list = list(map(int, var_from_user))

float_list = []

for i in int_list:
    float_list.append(float(i))
print(f"Float list: {float_list}")
