def count(user_string):
    dict_from_string = {}.fromkeys(user_string, 0)
    for item in user_string:
        if item in dict_from_string:
            dict_from_string[item] += 1
    return print(dict_from_string)

user_string = str(input("Please enter string for counting\n"))
count(user_string)