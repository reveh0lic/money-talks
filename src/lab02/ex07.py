a=input('ФИО, группа, GPA: ').split(', ')
fio, group, gpa = a
gpa= float(gpa)

student = (fio.strip().capitalize(),group,f"{gpa:.2f}")
print(student)

