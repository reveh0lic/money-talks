### ЛР 2
## Задача 1
```
a=input('Список: ')

if a=='[]':
    raise ValueError('Пустой список') 

a=a.strip('[]').split(', ')
a2=[]
for i in a:
    if i.count(".")==1:
        a2.append(float(i))
    elif i.count(".")==0:
        a2.append(int(i))

a3=[]
while a2:
    minimum=a2[0]
    for i in a2: 
        if i<minimum:
            minimum=i
    a3.append(minimum)
    a2.remove(minimum)

answer = a3[0],a3[-1]
print(answer)
```
![Скриншот](https://github.com/reveh0lic/money-talks/blob/main/images/lab02_images/ex01.png)
## Задача 2
```
a=input('Список: ')

if a=='[]':
    print('[]')
    exit()

a=a.strip('[]').split(', ')
a2=[]
for i in a:
    if i.count(".")==1:
        a2.append(float(i))
    elif i.count(".")==0:
        a2.append(int(i))
a2=list(set(a2))
a3=[]
while a2:
    minimum=a2[0]
    for i in a2: 
        if i<minimum:
            minimum=i
    a3.append(minimum)
    a2.remove(minimum)

print(a3)
```
## Задача 3
```
def flatten(mat: list[list | tuple]) -> list:
    result = []
    for row in mat:
        if not isinstance(row, (list, tuple)):
            raise TypeError
        for item in row:
            result.append(item)
    return result
```
## Задача 4
```
def transpose(mat):
    if not mat:
        return []

    n=len(mat[0])

    for row in mat:
        if len(row)!=n:
            raise ValueError

    a2=[]
    for j in range(n):
        a3=[]
        for i in range(len(mat)):
            a3.append(mat[i][j])
        a2.append(a3)

    return a2
```
## Задача 5
```
def row_sums(mat):
    if not mat:
        return []

    n=len(mat[0])

    for row in mat:
        if len(row)!=n:
            raise ValueError

    a2=[]
    for row in mat:
        a2.append(sum(row))

    return a2
```
## Задача 6
```
def col_sums(mat):
    if not mat:
        return []

    n=len(mat[0])

    for row in mat:
        if len(row)!=n:
            raise ValueError

    a2=[]
    for j in range(n):
        a3=0
        for i in range(len(mat)):
            a3+=mat[i][j]
        a2.append(a3)

    return a2
```
## Задача 7
```
def format_record(rec):
    if not isinstance(rec, tuple):
        raise TypeError("Запись должна быть кортежем")
    if len(rec) != 3:
        raise ValueError("Запись должна содержать ФИО, группу и GPA")

    fio, group, gpa = rec

    if not isinstance(fio, str) or not isinstance(group, str):
        raise TypeError("ФИО и группа должны быть строками")
    if not isinstance(gpa, (int, float)):
        raise TypeError("GPA должен быть числом")
    if not 0.0 <= gpa <= 5.0:
        raise ValueError("GPA должен быть от 0 до 5")

    fio_parts = fio.split()
    if len(fio_parts) not in (2, 3):
        raise ValueError("ФИО должно состоять из двух или трёх слов")

    group = group.strip()
    if not group:
        raise ValueError("Группа не должна быть пустой")

    surname = fio_parts[0].capitalize()
    initials = "".join(f"{name[0].upper()}." for name in fio_parts[1:])

    return f"{surname} {initials}, гр. {group}, GPA {gpa:.2f}"
```






