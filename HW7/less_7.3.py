# Task3. Write a function that calculates the number of characters included in a given string
# Задача 3. Напишите функцию, которая вычисляет количество символов, включенных в данную строку 

# lang = str(input("inpyt sring"))

def Inc_Str():
    """
    Function: Inc_Str
    input parameter: (none)
    type input parameter: (str)
    return Number of characters in string
    """
    lang = str(input("Input string: "))
    a = len(lang)
    print("Number of characters: ", a)
Inc_Str()