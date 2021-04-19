def list_animals(animals):
    list = ''
    for i in range(0, len(animals)):
        list += str(i + 1) + '. ' + animals[i] + '\n'
    return print(list)

