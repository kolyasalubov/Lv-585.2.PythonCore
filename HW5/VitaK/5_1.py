numbers = [a for a in range (1,11)]

list1=[b for b in numbers if b % 2 == 0 ]
print ((list1), 'is even numbers that are divisible by 2')

list2=[c for c in numbers if c % 3 == 0 and c % 2 != 0 ]
print ((list2), 'is odd numbers, which are divisible by 3') 

list3=[d for d in numbers if d % 3 != 0 and d % 2 != 0 ]
print ((list3), 'is numbers that are not divisible by 2 and 3')
