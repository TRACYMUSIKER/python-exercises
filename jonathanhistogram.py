def split(sentence):
    padded_sentence = sentence ''
    words = []
    curr_word = ''

    for char in padded_sentence:

import splitter

from splitter import split 
sentence = 'to be or not to be'
words = splitter.split(sentence)
word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print word_count

def histogram(things):
    thing_count = {}
    for thing in thing_count:
        if thing in thing_count:
            thing_count[thing] += 1
        else:
            thing_count[thing] = 1
        
missing some stuff!!!!
word_sum.oy
from splitter import split
from hisotgram import histogram

def letter_histogram(sentence):
    letter_count = hisotgram(sentence)
    return letter_count


def word_hisotgram(sentence):
    words = split(sentence)
    word_count = histogram(words)
    return word_count


in another file (test.py)
from word_sum import word_histogram
print word_histogram('to be or not to be')
