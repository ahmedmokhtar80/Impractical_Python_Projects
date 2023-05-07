"""Decrypt a route cipher by inputing matrix & key."""
ciphertext = "16 12 8 4 0 1 5 9 13 17 18 14 10 6 2 3 7 11 15 19"

# split elements into words, not letters
cipherlist = ciphertext.split()

# initialize variables
COLS = 4
ROWS = 5

key = '-1 2 -3 4'   # neg number means read UP column, vs. DOWN
translation_matrix = []
plaintext = ''

# turn key_int into list of integers:
key_int = [int(i) for i in key.split()]

# turn columns into items in list of lists:
for end, start in enumerate(range(0, COLS*ROWS, ROWS), 1):
    if key_int[end-1] > 0:
        translation_matrix.append(cipherlist[start:end * ROWS][::-1])
    else:
        translation_matrix.append(cipherlist[start:end * ROWS])

print("\nciphertext = {}".format(ciphertext))
print("\ntranslation matrix =", *translation_matrix, sep="\n")
print("\nkey length = {}".format(len(key_int)))

# loop through nested lists popping off last item to new list:
for col in reversed([*zip(*translation_matrix)]):
    plaintext += ' '.join(col) + ' '

print("\nplaintext = {}".format(plaintext))
