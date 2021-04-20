def number_of_characters():

    check_string = list(input ('Enter symbols:'))
    
    result = {}
    
    for symbols in check_string:
        if symbols not in result.keys():
            result[symbols] = 1
        else:
            result[symbols] +=1
    
    return result


print (number_of_characters())

