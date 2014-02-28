
def count_words(sentence):
    ''' Counting words in a sentence'''

    words = []
    word = ''

    for index, c in enumerate(sentence):

        if c != ' ':
            word += c
        elif index == 0 or sentence[index - 1] == ' ':
            continue
        else:
            words.append(word)
            word = ''

    if word != '':
        words.append(word)

    return len(words)

print count_words('This is a world cat')

