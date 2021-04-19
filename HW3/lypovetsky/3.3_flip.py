# Поміняти між собою значення двох змінних, не використовуючи третьої змінної.
a = 1
b = 2
print(
    "a = ",
    a,
    sep=""
)
print(
    "b = ",
    b,
    sep="",
    end="\n\n"
)

print("=== flip ===", end="\n\n")

a, b = b, a

print(
    "a = ",
    a,
    sep=""
)
print(
    "b = ",
    b,
    sep=""
)
