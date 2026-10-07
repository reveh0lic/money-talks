
mat = eval(input("Список: "))

result = []

for row in mat:
    if not isinstance(row, (list, tuple)):
        raise TypeError

    for item in row:
        result.append(item)

print(result)
