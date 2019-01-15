import random

print('--------------------------------')
print('        GUESS THE NUMBER')
print('--------------------------------')
print()

the_number = random.randint(0, 100)
guess = -1
name = input('Player, What is your name? ')

print('Hello '+ name)
while guess != the_number:
    guess_text = input('Guess the Number ')
    guess = int(guess_text)
    if guess < the_number:
        print('sorry {}, your guess of {} was too LOW'.format(name, guess))
    elif guess > the_number:
        print('sorry {}, your guess of {} was too HIGH'.format(name, guess))
    else:
        print('Excellent work {}, your guess of {} was CORRECT'.format(name, guess))

replay_text = input('Would you like to play again? type [1] for YES, [2] for NO ')
replay = int(replay_text)
if replay == 1:
        guess_text = input('Guess the Number ')
        guess = int(guess_text)
        while guess != the_number:
            guess_text = input('Guess the Number ')
            guess = int(guess_text)
            if guess < the_number:
                print('sorry {}, your guess of {} was too LOW'.format(name, guess))
            elif guess > the_number:
                print('sorry {}, your guess of {} was too HIGH'.format(name, guess))
            else:
                print('Excellent work {}, your guess of {} was CORRECT'.format(name, guess))