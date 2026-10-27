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