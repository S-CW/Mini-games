import random

# Guessing game
def guess(x):
    random_number = random.randint(1, x)
    guess = 0

    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry wrong number, guess too low. Try again.')
        elif guess > random_number:
            print('Sorry wrong number, guess too high. Try again.')

    print(f'You won! The number is {random_number}')


guess(10)



# Computer guessing
def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'Is {guess} too high, too low, or correct?').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'{guess} is correct! Computer win')

computer_guess(10)

