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
    a = []

    for row in mat:
        if not isinstance(row, (list, tuple)):
            raise TypeError

        a.extend(row)

    return a


a = input("Список: ")

a = a.replace("[", "").replace("]", "")
a = a.replace("(", "").replace(")", "")

a = list(map(int, a.split(",")))

print(a)

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
a=input('ФИО, группа, GPA: ').split(', ')
fio, group, gpa = a
gpa= float(gpa)

student = (fio.strip().capitalize(),group,f"{gpa:.2f}")
print(student)
```
## Задача 8
```
a = input('ФИО, группа, GPA: ').split(', ')
fio, group, gpa = a

gpa = float(gpa)
parts = fio.strip().split()
fio2 = parts[0]
for part in parts[1:]:
    fio2 += ' ' + part[0] + '.'
student = (fio2, group, f"{gpa:.2f}")
print(f'{student[0]}, гр. {student[1]}, GPA {student[2]}')
```






