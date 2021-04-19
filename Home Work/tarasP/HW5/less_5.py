# Task2. Create a list that contains elements of integer type, then use the loop to change the type of these elements to a floating type. 
# (Hint: use the built-in float () function). 

# Создайте список, содержащий элементы целочисленного типа, затем с помощью цикла перебора измените тип 
# данных элементов на числа с плавающей точкой. (Подсказка: используйте встроенную функцию float().)

list_a = [3,5,12,33,45,1,]
i = 0

for a in list_a:
    list_a[i] = float(a)
    i = i + 1
print(list_a)