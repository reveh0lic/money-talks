# money-talks
## Задача 1
```
name=input("Имя: ")
age=int(input("Возраст:"))
print(f'Привет, {name}! Через год тебе будет {age+1}')
```
![Скриншот](https://github.com/reveh0lic/money-talks/blob/main/images/lab01_images/ex01.png?raw=true)
## Задача 2
```
a = float(input("a: ").replace(",", "."))
b = float(input("b: ").replace(",", "."))
print(f"sum: {a+b:.2f}",f"avg: {(a+b)/2:.2f}", sep='; ')
```
![Скриншот](https://github.com/reveh0lic/money-talks/blob/main/images/lab01_images/ex02.png?raw=true)
## Задача 3
```
price=int(input('Цена:'))
discount=int(input('Скидка:'))
vat=int(input("Вещественные:"))
base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount

print(f'База после скидки: {base:.2f}')
print(f"НДС: {vat_amount:.2f}")
print(f'Итого к оплате: {total:.2f}')
```
![Скриншот](https://github.com/reveh0lic/money-talks/blob/main/images/lab01_images/ex03.png?raw=true)
## Задача 4
```
minutes=int(input('Минуты: '))
hours = str(minutes//60)
ost=minutes%60
mins=f"{ost:02d}"
print(hours, ":", mins, sep="")
```
![Скриншот](https://github.com/reveh0lic/money-talks/blob/main/images/lab01_images/ex04.png?raw=true)
## Задача 5
```
fio = input('ФИО: ')
l = list(map(list, fio.split()))
inic=''
for x in l:
    inic+=x[0].upper()
print('ФИО: ',fio)
print('Инициалы: ',inic, '.',sep='')
print('Длина (символов): ', len(fio))
```
![Скриншот](https://github.com/reveh0lic/money-talks/blob/main/images/lab01_images/ex05.png?raw=true)
## Задача 6
```
n=int(input("in_1:"))

och=0
for i in range(2,n+2):
    members=input(f'in_{i}:')
    a,b,c,d = members.split()
    c=int(c)
    if d=="True":
        och+=1

print("out:",och,n-och)
```
![Скриншот](https://github.com/reveh0lic/money-talks/blob/main/images/lab01_images/ex06.png?raw=true)
## Задача 7
```
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
```
![Скриншот](https://github.com/reveh0lic/money-talks/blob/main/images/lab01_images/ex07.png?raw=true)
