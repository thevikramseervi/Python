from random import *
number = randint(1, 10)
for i in range(1, 6):
    guess = int(input('Take a guess: '))
    if guess < number:
        print('Your guess is too low')
    elif guess > number:
        print('Your guess is too high')
    else:
        break
if guess == number:
    print('You guessed in', i, 'attempts.')
else:
    print('Better luck next time.')