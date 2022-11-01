import random

guesses_made = 0 # number of attempts to guess

name = input("What's your name?\n")
number = random.randint(1, 100)
print('Alright, {0}, I guessed a number between 1 and 100. Can you guess?'.format(name))

while guesses_made < 6: # until the user has exceeded the number of allowed attempts - 6

    guess = int(input('Enter number:'))

    guesses_made += 1 # increase the counter of the number of attempts

    if guess < number:
        print('Your number is less than what I guessed.')

    if guess > number:
        print('Your number is greater than my guess.')

    if guess == number:
        break

if guess == number:
    print('Good, {0}! You guessed my number using {1} tries!'.format(name, guesses_made))
else:
    print('Guessed wrong! I guessed the number {0}'.format(number))