"""Use brute force to crack a lock combination."""

import time, sys
from random import choices

start_time = time.time()

combo = (9, 9, 7, 6, 5)

numbers = list(range(0,10))
attempts = 0

# use randint to generate permutations with repetition
while True:
    perm = tuple(choices(numbers, k=len(combo)))
    attempts += 1
    if perm == combo:
        print('\nCracked! {} {}'.format(combo, perm))
        print('it took {} attempts to crack!'.format(attempts), file=sys.stderr)
        break

end_time = time.time()
print('\nRuntime for this program was {} seconds.'
      .format(end_time - start_time))
