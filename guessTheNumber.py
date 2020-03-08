#this is a guess the number game
import random
secretNumber = random.randint(1, 20)
print('I am thinking of a number between 1 and 20')

#ask the playrs to guess 6 times.
for guessTaken in range(1, 7):
    print('Take a guess.')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess it too low.')
    elif guess > secretNumber:
        print('Your guess is too hight')
    else:
        break
if guess == secretNumber:
    print('Good job! You guessed my number in ' + str(guessTaken) + ' guesses!')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))
