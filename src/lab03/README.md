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
