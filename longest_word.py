
def longest_word(text):
    phrases = text.split()
    space = ""
    for phrase in phrases:
        if len(phrase) > len(space):
            space = phrase
    return space

"""
words = 'the quick brown fox jumped over the lazy dog'.split()

long_word = max(words, key=len)
print(long_word)
"""