from math import *

file = open("07.txt", 'rt')
TEXT = file.read()
file.close()


def find_bigram_freq(text):
    freq = {}
    for i in range(0, len(text), 2):
        if text[i:i + 2] in freq:
            freq[text[i:i + 2]] += 1
        else:
            freq[text[i:i + 2]] = 1
    total = sum(freq.values())
    for bigram in freq:
        freq[bigram] = float(freq[bigram] / total)
    return freq


freq = find_bigram_freq(TEXT)
sorted_freq = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))
top_cypher_bi = list(sorted_freq)[:5]
top_bi = ["ст", "но", "то", "на", "ен"]

alph = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х',
        'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']




