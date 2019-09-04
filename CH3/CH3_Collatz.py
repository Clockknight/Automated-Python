def collatz(number):
  if number % 2 == 0:
      return number // 2
  else:
      return 3 * number + 1

print('Please input an integer for the collatz sequence.')
collatzValue = int(input())

print('Beginning sequence.')

while 1 == 1:
    print(collatzValue)
    collatzValue = collatz(collatzValue)
    if collatzValue == 1:
        break

print('The initial value has been transformed to 1. The collatz sequence is complete.')
