#1. Записати в стрічку філософію Пайтона 
#- Знайти в заданій стрічці кількість входжень слів (better, never, is)
#- Вивести весь текст у верхньому регістрі (всі великі літери)
#- Замінити всі входження символу “і” на “&

#2. Задано чотирицифрове натуральне число. 
#- Знайти добуток цифр цього числа.
#- Записати число в реверсному порядку.
#- Посортувати цифри, що входять в дане число

#3. Поміняти між собою значення двох змінних, не використовуючи третьої змінної.
#Замінити всі входження символу “і” на “&


menu_congig = {
    "menu1": {
            '1':'1.Вивести в стрічку філософію Пайтона', 
            '2':'\n2.Знайти в заданій стрічці кількість входжень слів (better, never, is)',
            '3':'\n3.Вивести весь текст у верхньому регістрі (всі великі літери)',
            '4':'\n4.Замінити всі входження символу “і” на “&”',
            '5':'\n5.Вихід',
    },
    "menu2": {
            '1':'1. better', 
            '2':'2. never', 
            '3':'3. is',
            '4':'4. Назад',
    }
    
}



string = ("Zen of Python: \n"
"Beautiful is better than ugly. \n"
"Explicit is better than implicit. \n"
"Simple is better than complex. \n"
"Complex is better than complicated. \n"
"Flat is better than nested. \n"
"Sparse is better than dense. \n"
"Readability counts. \n"
"Special cases aren't special enough to break the rules. \n"
"Although practicality beats purity. \n"
"Errors should never pass silently. \n"
"Unless explicitly silenced. \n"
"In the face of ambiguity, refuse the temptation to guess. \n"
"There should be one-- and preferably only one --obvious way to do it. \n"
"Although that way may not be obvious at first unless you're Dutch. \n"
"Now is better than never. \n"
"Although never is often better than *right* now. \n"
"If the implementation is hard to explain, it's a bad idea. \n"
"If the implementation is easy to explain, it may be a good idea. \n"
"Namespaces are one honking great idea -- let's do more of those!")



def ChouseWords():
    print(menu_congig['menu2'])
    menu2 = int(input("input number ### "))
    better = string.count('better')+1
    never = string.count('never')+1
    countIs = string.count('is')+1

    if menu2 == 1:
        print(better)
    elif menu2 == 2:
        print(never)
    elif menu2 == 3:
        print(countIs)
    elif menu2 == 4:
        MenuInput()
    elif menu2 == 5:
        pass
    

def UpperString():
    uperStr = string.upper()
    print(uperStr)

def ReplaceLetter():
    replaseI = string.replace("i", "&")     #Зробити меню для вибору символу який замінити, і символ який замінити
    print(replaseI)

def MenuInput():
    print(menu_congig['menu1'])
    menu = int(input("input number ### "))
    if menu == 1:
        print(string)
    elif menu == 2:    
        ChouseWords()
    elif menu == 3:
        UpperString()
    elif menu == 4:
        ReplaceLetter()
    else:
        pass

MenuInput()











