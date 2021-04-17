def list_animals(animals):
    list = ''
    for i in range(len(animals)):
        list += str(i + 1) + '. ' + animals[i] + '\n'
    return list

#

def list_animals(animals):
    list1=[str(i + 1) + '. ' + animals[i] + '\n' for i in range(len(animals))]
    return ''.join(list1)
