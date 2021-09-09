import math


def find_freq(text):
    freq = {}
    for i in text:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    return freq

print(find_freq("чсмчсмчсм"))

def find_bigram_freq(text):
    freq = {}
    for i in range(0, len(text), 2):
        if text[i:i+2] in freq:
            freq[text[i:i+2]] += 1
        else:
            freq[text[i:i+2]] = 1
    return freq


# print(find_bigram_freq("momomemtmdghh"))


def find_entropy(text, n = 1):

    if n == 1:
        freq = find_freq(text)
    elif n == 2:
        freq = find_bigram_freq(text)
    prob = freq.values()
    entropy = sum(list(map(lambda x: -x * math.log2(x), prob)))
    entropy *= 1 / n
    return entropy


print(find_entropy("", 1))