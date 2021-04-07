number_from_user = int(input("Enter number: "))

if number_from_user < 0:
    print("Need number > 0")
elif number_from_user == 1:
    fibonacci = [0, 1]
    print(fibonacci)
elif number_from_user == 0:
    fibonacci = [0]
    print(fibonacci)
else:
    fibonacci = [0, 1]

    for item in range(2, number_from_user):
        fibonacci.append(fibonacci[item-1] + fibonacci[item-2])
        if fibonacci[item] > number_from_user:
            break
    print(fibonacci)
    
