a = input('ФИО, группа, GPA: ').split(', ')
fio, group, gpa = a

gpa = float(gpa)
parts = fio.strip().split()
fio2 = parts[0]
for part in parts[1:]:
    fio2 += ' ' + part[0] + '.'
student = (fio2, group, f"{gpa:.2f}")
print(f'{student[0]}, гр. {student[1]}, GPA {student[2]}')