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
    'menu1': [
            '1. Вивести в стрічку філософію Пайтона', 
            '2. Знайти в заданій стрічці кількість входжень слів (better, never, is)',
            '3. Вивести весь текст у верхньому регістрі (всі великі літери)',
            '4. Замінити всі входження символу “і” на “&”',
            '5. Вихід',
        ],
    'menu2': [
            '1. better', 
            '2. never', 
            '3. is',
            '4. Назад',
        ]
    
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

# def MenuInput
#     menu = int(input('aaa'))
#     menu2 = int(input('\t1. better;\n\t2. never;\n\t3. is;\n\t4. назад;\n\t5. вихід;\n\t###:'))
# MenuInput

# menu2 = int(input('\t1. better;\n\t2. never;\n\t3. is;\n\t4. назад;\n\t5. вихід;\n\t###:'))

# menu3 = input('вибрати смивол який змінити', "вибрати символ на який змінити")



def MenuGo():
    menu = True
    if menu == "1":
        print(string)
        return menu
    elif menu == "2":
        print(menu2)
    elif menu == "3":
        print(UpperString)
        return menu
    elif menu == "4":
        print(ReplaceLetter)
        return menu
    elif menu == "5":
        pass
MenuGo()

def ChouseWords():
    better = string.count('better')+1
    never = string.count('never')+1
    countIs = string.count('is')+1

    if menu1 == 1:
        print(better)
    elif menu1 == 2:
        print(never)
    elif menu1 == 3:
        print(countIs)
    elif menu1 == 4:
        print(menu)
    elif menu1 == 5:
        pass
ChouseWords()



def ReplaceLetter():
    replaseI = string.replace("i", "&")
    if menu == 4:
        print(replaseI)
ReplaceLetter()


def UpperString():
    uperStr = string.upper()
    if menu == 3:
        print(uperStr)
UpperString()