"""Find all word-pair palingrams in a dictionary file."""
import load_dictionary

word_list = load_dictionary.load('2of4brif.txt')

# find word-pair palingrams
def find_palingrams():
    """Find dictionary palingrams."""
    pali_list = []
    words = set(word_list)
    for word in words:
        end = len(word)
        if end > 1:
            rev_word = word[::-1]
            for forward, backward in enumerate(range(end, 0, -1)):
                if word[forward:] == rev_word[:backward] and rev_word[backward:] in words:
                    pali_list.append((word, rev_word[backward:]))
                if word[:forward] == rev_word[backward:] and rev_word[:backward] in words:
                    pali_list.append((rev_word[:backward], word))
    return pali_list

palingrams = find_palingrams()

#sort palingrams on first word
palingrams_sorted = sorted(palingrams)

#display list of palingrams
print("\nNumber of palingrams = {}\n".format(len(palingrams_sorted)))
for first, second in palingrams_sorted:
    print("{} {}".format(first, second))
