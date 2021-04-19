# Задано чотирицифрове натуральне число.
print("Enter a number between 0000 and 9999:")
number = int(input())
# number = 1934
print(
    "My number is:",
    number,
    sep="\n",
    end="\n\n"
)

# Знайти добуток цифр цього числа.
numberToStr = str(number)
strToMap = map(int, numberToStr)
intToList = list(strToMap)
sumOfNumber = 0
for i in intToList:
    sumOfNumber += i
print(
    "Number → n+u+m+b+e+r:",
    sumOfNumber,
    sep="\n",
    end="\n\n"
)

# - Записати число в реверсному порядку.
intReversed = int("".join(reversed(str(number))))
print(
    "List → tsiL:",
    intReversed,
    sep="\n",
    end="\n\n"
)

# - Посортувати цифри, що входять в дане число
intToList.sort()
print("tsiL → List:", intToList, sep="\n", end="\n\n")
