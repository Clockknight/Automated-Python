'''
INCORRECT CODE

import random
guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
toss = random.randint(0, 1) # 0 is tails, 1 is heads
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guesss = input()
    if toss == guess:
       print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
'''

#CORRECTED CODE
import random
guess = ''
while guess not in ('heads', 'tails'):
  print('Guess the coin toss! Enter heads or tails:')
  guess = input()

while True:
    toss = random.randint(0, 1) # 0 is tails, 1 is heads
    if (guess == 'heads'):
        guess = 1
    if (guess == 'tails'):
        guess = 0
    if (toss == guess):
      break
    else:
      print('Nope! Guess again!')
      while guess not in ('heads', 'tails'):
        guess = input()
        break

print('You got it!')
