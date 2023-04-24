"""Map letters from string into dictionary & print bar chart of frequency."""
import string, sys

class Etaoin:
    def __init__(self, text):
        self.text = text
        self.keys = ''
        self.dict_letters = {}
        
        self.text_to_keys()
        self.keys_to_dict()
        self.count_letters()
    
    def text_to_keys(self):
        dict_trans = self.text.maketrans(dict.fromkeys(string.punctuation + ' '))
        self.keys = self.text.translate(dict_trans).lower()

    def keys_to_dict(self):
        self.dict_letters = dict.fromkeys(sorted(self.keys))

    def count_letters(self):
        for k in self.dict_letters:
            self.dict_letters.update({k: [k] * self.keys.count(k)})

    def __str__(self):
        d = [str(pairs) for pairs in self.dict_letters.items()]
        return '\n'.join(d)

text = 'Like the castle in its corner in a medieval game, \
I forsee terrible trouble and i stay here just the same.'

etaoin_text = Etaoin(text)
print("\nYou may need to stretch console window if text wrapping occurs.\n")
print("text = ", end='')
print(f"{text}\n", file=sys.stderr)
print(etaoin_text)

