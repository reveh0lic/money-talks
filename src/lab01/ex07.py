stroka=input('In:')
s=''
step=0
finish=0

p=0
for i in range (len(stroka)):
    if stroka[i].isupper():
        s+=stroka[i]
        break
for k in range(i+1,len(stroka)-1):
    if stroka[k].isdigit():
        step=k-i+1
        finish=k+1
        break

for n in range(finish,len(stroka),step):
    s+=stroka[n]
print('Out: ',s)
        


