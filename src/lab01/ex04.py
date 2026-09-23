minutes=int(input('Минуты: '))
hours = str(minutes//60)
ost=minutes%60
mins=f"{ost:02d}"
print(hours, ":", mins, sep="")