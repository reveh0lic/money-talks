a=input('Кортеж: ')

if a=='[ ]':
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

        




