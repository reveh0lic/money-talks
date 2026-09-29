fio = input('ФИО: ')
l = list(map(list, fio.split()))
inic=''
for x in l:
    inic+=x[0].upper()
print('ФИО: ',fio)
print('Инициалы: ',inic, '.',sep='')
print('Длина (символов): ', len(fio))
