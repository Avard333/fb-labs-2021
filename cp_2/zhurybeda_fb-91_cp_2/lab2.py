alph = ['а', 'б', 'в', 'г', 'д', 'е', 'ж','з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ','ы', 'ь', 'э', 'ю', 'я']

key_list = ["мы", "вам", "грам", "возле", "анархический"]

file = open("clean_text.txt", 'r')
TEXT = file.read()
file.close()

dict_alph = {}
for i in range(0, len(alph)):
    dict_alph[i] = alph[i]

def from_text_to_keys(text):
    text_list = []
    for letter in text:
        for let in dict_alph:
            if letter == dict_alph[let]:
                text_list.append(let)
    return text_list


def from_keys_to_text(keys_list):
    text = ""
    for i in keys_list:
        for let in dict_alph:
            if i == let:
                text += dict_alph[let]
    return text


def encode(text, key):
    text_keys_list = from_text_to_keys(text)
    keys_pos = from_text_to_keys(key)
    j = 0
    for i in range(len(text_keys_list)):
        text_keys_list[i] += keys_pos[j]
        j += 1
        if j == len(key):
            j = 0
    return from_keys_to_text(text_keys_list)








