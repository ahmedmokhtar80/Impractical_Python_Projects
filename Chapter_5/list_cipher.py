"""Hide a null cipher within a vocabulary list."""
from random import randint
import re
import load_dictionary

# write a short message and use no punctuation or numbers!
input_message = "Panel at east end of chapel slides"

message = re.findall(r'[a-z]', input_message.lower())
message = ''.join(message)
print(message, '\n')

# open dictionary file
word_list = load_dictionary.load('2of4brif.txt')

# build vocabulary word list with hidden message
vocab_list = []
for letter in message:
    size = randint(6, 10)
    for word in word_list:
        if len(word) == size and word[2].lower() == letter.lower()\
        and word not in vocab_list:
            vocab_list.append(word)
            break

if len(vocab_list) < len(message):
    print("Word List is too small. Try larger dictionary or shorter message!")
else:        
    print("Vocabulary words for Unit 1: \n", *vocab_list, sep="\n")        
