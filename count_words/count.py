from string import punctuation, printable
import re
def count_words_one(sentence):  # first solution
    word_count = {}
    for word in map(lambda x: x.lower().strip(punctuation), sentence.split()):
        word = list(filter(lambda x: x in set(printable), word))
        word = ''.join(word)
        word_count[word] = word_count.get(word, 0) + 1

    return word_count


def count_words_two(sentence):  # second solution
    regex = r"[\w']+"
    words = map(lambda x: x.lower(), sentence.split())

    words = re.findall(regex, sentence)

    word_count = {}
    for word in map(lambda x: x.lower(), words):
        word_count[word] = word_count.get(word, 0) + 1

    return word_count