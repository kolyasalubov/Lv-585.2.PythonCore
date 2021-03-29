fibonacci1 = 1
fibonacci2 = 1
user_number = int(input("Enter a last Fibonacci number: "))

print(0, fibonacci1, fibonacci2, sep=', ', end=', ')

for i in range(2, 50):
    fibonacci1, fibonacci2 = fibonacci2, fibonacci1 + fibonacci2
    if fibonacci2 > user_number:
        break
    print(fibonacci2, end=', ')
    