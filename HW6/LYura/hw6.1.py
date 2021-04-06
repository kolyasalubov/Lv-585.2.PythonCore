n1 = int(input("Enter first number:"))
n2 = int(input("Enter second number:"))

def find_largest(n1, n2):
	"""This function return largest number"""
if n1>n2:
    print(f"Largest number is {n1}")
elif n1<n2:
    print(f"Largest number is {n2}")
else:
    print(f"Numbers are equal {n1}={n2}")
