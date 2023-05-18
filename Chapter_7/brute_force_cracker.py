"""Use brute force to crack a lock combination."""
import time
from random import randint

start_time = time.time()

combo = (9, 9, 7, 6, 5)

perm = []
attempts = 0

# use randint to generate permutations with repetition
for i in combo:
    while True:
        attempts += 1
        if (num := randint(0, 9)) == i:
            perm.append(num)
            break
        
if (perm := tuple(perm)) == combo:
    print('Cracked! {} {}'.format(combo, perm))
    print('it took {} attempts to crack'.format(attempts))

end_time = time.time()

print('\nRuntime for this program was {} seconds.'
      .format(end_time - start_time))
   
