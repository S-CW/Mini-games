import random

# Guessing game
# By default, player will have 3 tries to guess the number right, you can change it by changing the variable TRIES
# By default, the max number range is set to 10, you can change it by changing SET_NUM variable

# To play guessing as player, uncomment line 34
# To play with computer, uncomment line 69
# To start game, run the python file.

# Variables
TRIES = 3
SET_NUM = 10

# Guess the random number
def guess(max_num, tries):
    random_number = random.randint(1, max_num)
    guess = 0
    
    while guess != random_number:
        print(f'You have {tries}❤️  left')
        guess = int(input(f'Guess a number between 1 and {max_num}: '))

        if guess < random_number:
            print('Sorry wrong number, guess too low. Try again.')
        elif guess > random_number:
            print('Sorry wrong number, guess too high. Try again.')

        tries -= 1
        if tries == 0:
            return print('You lose! You get nothing!')
        
    print(f'You won! The number is {random_number} 🎉')


# guess(SET_NUM, TRIES)



# Computer guessing
def computer_guess(max_num, tries):
    print(f'Please input h for high, l for low, c for correct as feedback.')

    low = 1
    high = max_num
    feedback = ''
    while tries > 0:
        print(f'Computer have {tries}❤️  left')

        if low <= high:
            guess = random.randint(low, high)
        elif low > high:
            # when low > high, invalid answer is chosen
            return print('No further number can be guessed, game will be terminated. Are you by any chance cheating? 😜')

        feedback = input(f'Is {guess} too high, too low, or correct? ').lower()

        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        elif feedback == 'c':
            return print(f'{guess} is correct!🤖 win')
        tries -= 1

    print(f'🤖 failed to guess your number, You win!')

# computer_guess(SET_NUM, TRIES)

