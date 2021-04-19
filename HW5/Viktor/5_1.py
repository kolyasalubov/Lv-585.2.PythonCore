a = []
b = []
c = []

for x in range(1, 11):
    if x%2==0:
        a.append(x)
    if x%3==0:
        b.append(x)
    if x%3!=0 and x%2!=0:
        c.append(x)
        
print(f"numbers divisible by 2:\n{a}")
print(f"numbers divisible by 3:\n{b}")
print(f"numbers are not divisible by 2 and 3:\n{c}")
