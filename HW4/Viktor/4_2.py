user_list = list(range(int(input("Enter a number of elements in the list: "))))
elements_index = 0

print(user_list)
print(type(user_list[elements_index]))

for elements_index in range(len(user_list)):
    if isinstance(user_list[elements_index], int):
        user_list[elements_index] = float(user_list[elements_index])
    elements_index += 1

input("To change data type in the list press Enter.")
print(user_list)
print(type(user_list[elements_index-1]))
