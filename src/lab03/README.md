# **ЛР 3**
### Задача A1
```
def normalize(text, *, casefold: bool = True, yo2e: bool = True):
    if yo2e:
        text=text.replace('Ё','Е').replace('ё','е')

    if casefold:
        text=text.casefold()
    else:
        text=text.lower()
    return ' '.join(text.split())
```
![Скриншот](https://github.com/reveh0lic/money-talks/blob/main/images/lab03_images/lab03A1.png)
### Задача A2
```
def tokenize(text):
    result = []
    word = ""

    for i, char in enumerate(text):
        if char.isalnum() or char == "_":
            word += char
        elif (
            char == "-"
            and word
            and i + 1 < len(text)
            and (text[i + 1].isalnum() or text[i + 1] == "_")
        ):
            word += char
        else:
            if word:
                result.append(word)
                word = ""
    if word:
        result.append(word)

    return result
```
![Скриншот](https://github.com/reveh0lic/money-talks/blob/main/images/lab03_images/lab03A2.png)
### Задачи A3 + A4
```
def count_freq(tokens):
    freq={}
    for token in tokens:
        freq[token]=freq.get(token,0)+1
    return freq
-----------------------------------------------
def top_n(freq: dict[str, int], n: int = 5) :
    if n < 0:
        raise ValueError
    return sorted(freq.items(), key=lambda x:(-x[1],x[0]))[:n]
```
![Скриншот](https://github.com/reveh0lic/money-talks/blob/main/images/lab03_images/lab03A3.png)
### Задача B
```
import sys

from lib.text import normalize, tokenize, count_freq, top_n

txt = sys.stdin.read()

text = normalize(txt)
words = tokenize(text)
freq = count_freq(words)
top = top_n(freq, n=5)

print(f"Всего слов: {len(words)}")
print(f"Уникальных слов: {len(freq)}")
print("Топ-5:")

for word, count in top:
    print(f"{word}:{count}")
```
![Скриншот](https://github.com/reveh0lic/money-talks/blob/main/images/lab03_images/LAB03B.png)
