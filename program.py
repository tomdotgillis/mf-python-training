import random

print('--------------------------------')
print('        GUESS THE NUMBER')
print('--------------------------------')
print()

the_number = random.randint(0, 100)
guess = -1
while guess != the_number:
    guess_text = input('Guess the Number')
    guess = int(guess_text)
    if guess < the_number:
        print('oooh too low')
    elif guess > the_number:
        print('oooh too high')
    else:
        print('You Win!!')