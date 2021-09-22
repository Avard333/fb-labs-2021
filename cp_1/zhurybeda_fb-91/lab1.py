import math


def find_freq(text):
    freq = {}
    for i in text:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    total = sum(freq.values())
    for letter in freq:
        freq[letter] = float(freq[letter]/total)
    return freq


print(find_freq("авпвапвапыфилшжщж"))


def find_bigram_freq(text, intersect):
    freq = {}
    if intersect:
        for i in range(0, len(text), 2):
            if text[i:i+2] in freq:
                freq[text[i:i+2]] += 1
            else:
                freq[text[i:i+2]] = 1
        total = sum(freq.values())
        for bigram in freq:
            freq[bigram] = float(freq[bigram]/total)
    else:
        for i in range(0, len(text)):
            if text[i:i+2] in freq:
                freq[text[i:i+2]] += 1
            else:
                freq[text[i:i+2]] = 1
        total = sum(freq.values())
        for bigram in freq:
            freq[bigram] = float(freq[bigram]/total)
    return freq


print(find_bigram_freq("mo momemtmdghhр", True))
print(find_bigram_freq("mo momemtmdghhр", False))


def find_entropy(text, n=1):

    if n == 1:
        freq = find_freq(text)
    elif n == 2:
        freq = find_bigram_freq(text)
    prob = freq.values()
    entropy = sum(list(map(lambda x: -x * math.log2(x), prob)))
    entropy *= 1 / n
    return entropy


def find_redundant(h, alph):
    return 1 - (h/math.log2(alph))


# print(find_entropy("sdfdshmaksjhkjvsvksjrbvbjkdf", 1))

