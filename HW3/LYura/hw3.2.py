my_integer = 2916

# 1-st task
integers_list = [int(i) for i in str(my_integer)]
# print(integers_list)


def Multiplylist(my_list):
    x = 1
    for i in my_list:
        x = x * i
    return x


print("Myltiply task:", Multiplylist(integers_list))

# 2-nd task

integer_to_string = str(my_integer)
revert_string = integer_to_string[::-1]
print("Reverting task:", int(revert_string))

# 3-rd task
sorted_string = (sorted(integer_to_string))
join_mystring = "".join(sorted_string)
print("Sorting task:", int(join_mystring))
