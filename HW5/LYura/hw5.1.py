even = []
odd = []
other = []

for i in range(1, 10):
    if i %2 == 0:
        even.append(i)
    elif i %3 == 0:
        odd.append(i)
    else:
        other.append(i)
print(even, odd, other)
