import string


text = "hello world"

shift = 26 - 7
# 25 gives the word "hello world"
# this formula keeps it in a loop
shift %= 26



alphabet = string.ascii_lowercase

# start at the point where we shift and append
# everything that came after
shifted = alphabet[shift:] + alphabet[:shift]

# translation table, putting them bellow each other
table = str.maketrans(alphabet, shifted)

encrypted = text.translate(table)


print(encrypted)

