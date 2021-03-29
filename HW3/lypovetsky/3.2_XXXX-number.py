# Задано чотирицифрове натуральне число.
# print("Enter a number between 0000 and 9999:")
# number = int(input())
number = 1234
print(
    "My number is:",
    number,
    sep="\n",
    end="\n\n"
)

# Знайти добуток цифр цього числа.
numberToStr = str(number)
strToMap = map(int, numberToStr)
sumOfNumber = list(strToMap)
print(
    "Number → list:",
    sumOfNumber,
    sep="\n",
    end="\n\n"
)

# - Записати число в реверсному порядку.
sumOfNumber.sort(reverse=True)
print(
    "List → tsiL:",
    sumOfNumber,
    sep="\n",
    end="\n\n"
)

# - Посортувати цифри, що входять в дане число
sumOfNumber.sort()
print(
    "tsiL → List:",
    sumOfNumber,
    sep="\n",
    end="\n\n"
)
