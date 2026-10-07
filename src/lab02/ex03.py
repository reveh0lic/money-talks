a = input("Список: ")

a = a.replace("[", "").replace("]", "")
a = a.replace("(", "").replace(")", "")

a = list(map(int, a.split(",")))

print(a)