"""Decode a null cipher based on number of letters after punctuation marks."""

import string, sys

punctuation = string.punctuation

def main():
    """Loat text, solve null cipher."""
    # load & process message:
    filename = input("\nEnter filename for message to translate: ")
    loaded_message = load_text(filename)
    print("\nORIGINAL MESSAGE =")
    print(f"{loaded_message}", "\n")
    print(f"\nList of punctuation marks to check {punctuation}")

    message = ''.join(loaded_message.split())

    null_words = get_null_words(message, 3)
    null_chipher = solve_null_cipher(null_words)

    print()
    print(null_chipher)

    
def load_text(file):
    """Load a text file as a string."""
    try:
        with open(file) as f:
            return f.read().strip()
    except IOError as e:
        print(f'{e}.', f'Error opening {file}. Terminating program.', file=sys.stderr, sep='\n')
        sys.exit(1)


def get_null_words(message, count):
    """get a null words based on number letters after punctuation mark."""
    null_cipher = []
    for i, letter in enumerate(message):
        if letter in punctuation:
            _index = message.find(letter, i)
            null_cipher.append(message[_index+1:_index+count+1])
    return null_cipher

def solve_null_cipher(null_words):
    """Solve a null cipher based on number letters after punctuation mark."""
    null_cipher = ""
    for word in null_words:
        if word == '':
            continue
        no_punctuation = True
    
        for letter in word:
            if letter in punctuation:
                no_punctuation = False
            
        if no_punctuation:
            null_cipher += word[-1:]
    return null_cipher
    

if __name__ == '__main__':
    main()

