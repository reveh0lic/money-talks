import sys
from pathlib import Path
m = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(m))

from ex01 import normalize,tokenize,count_freq,top_n

txt=sys.stdin.read()

text=normalize(txt)
count=tokenize(text)
uslov=count_freq(count)
top=top_n(uslov,n=5)

print(f'Всего слов:{len(count)}')
print(f'Уникальных слов:{len(uslov)}')
print('Топ-5:')

for word, chislo in top:
    print(f'{word}:{chislo}') 
