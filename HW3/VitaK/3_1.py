def number_of_choise ():
    print ('''Find the number of occurrences of words (better, never, is) in a given tape 
    Print all uppercase text (all uppercase letters) 
    Replace all occurrences of the "and" character with "&" ''')
    select_number = int(input('What your choise?:'))
    zen_of_python = '''Beautiful is better than ugly.
        Explicit is better than implicit.
        Simple is better than complex.
        Complex is better than complicated.
        Flat is better than nested.
        Sparse is better than dense.
        Readability counts.
        Special cases aren't special enough to break the rules.
        Although practicality beats purity.
        Errors should never pass silently.
        Unless explicitly silenced.
        In the face of ambiguity, refuse the temptation to guess.
        There should be one-- and preferably only one --obvious way to do it.
        Although that way may not be obvious at first unless you're Dutch.
        Now is better than never.
        Although never is often better than *right* now.
        If the implementation is hard to explain, it\'s a bad idea.
        If the implementation is easy to explain, it may be a good idea.
        Namespaces are one honking great idea -- let\'s do more of those!'''
    if select_number == 1:
        print (f"Number of words \"better\" in Zen of Python is", zen_of_python.count("better"))
        print (f"Number of words \"never\" in Zen of Python is", zen_of_python.count("never"))
        print (f"Number of words \"is\" in Zen of Python is", zen_of_python.count("is"))
        number_of_choise()
    elif select_number == 2:
        print (zen_of_python.upper())
        number_of_choise()
    elif select_number == 3:
        print (zen_of_python.replace('i','&'))
        number_of_choise()
    else :
        print ('bad input')
        number_of_choise()
number_of_choise()




