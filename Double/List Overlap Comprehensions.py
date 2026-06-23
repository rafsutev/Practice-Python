# https://www.practicepython.org/exercise/2014/04/10/10-list-overlap-comprehensions.html

import random

a = random.sample(range(1,30), 12)
b = random.sample(range(1,30), 16)

print([x for x in a for y in b if x==y])
