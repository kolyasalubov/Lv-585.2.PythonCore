x = 1928

# multiplication
x_str = str(x)
dobutok = int(x_str[0]) * int(x_str[1]) * int(x_str[2]) * int(x_str[3])
print(f"{x_str[0]} * {x_str[1]} * {x_str[2]} * {x_str[3]} = {dobutok}")

# reverse
print(x_str[::-1])

# sorted
x_list = list(map(int, x_str))
print(sorted(x_list))