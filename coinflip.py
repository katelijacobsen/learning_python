# Using the if statement. We import something called random that generates a random number between 0 and 1

import random

num = random.randint(0, 1)   # Generates a random number that's either 0 or 1

if num > 0.5:
  print('Heads')
else:
  print('Tails')