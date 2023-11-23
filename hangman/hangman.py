from re import A
import requests, random, string

# Source of word
baseurl = 'https://www.randomlists.com/data/words.json'


# Hangman Game
# To start, run the file
# In the terminal, key in the choice of letter and press enter

def main_req(url):
    r = requests.get(url)
    return r.json()

data = main_req(baseurl)
word_data = data['data']

def get_valid_word(words):
    word = random.choice(words) #randomly chooses something from the list
    while '-' in word or ' ' in word: # Due to some words in the list contains '-' and ' '
        word = random.choice(words)

    return word.upper()

def hangman():
    word = get_valid_word(word_data)
    word_letters = set(word)    # letters in the selected word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()    # remove letters guessed by user

    lives = 6

    # Get user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # " ".join(['a', 'b', 'c']) --> 'a b cd'
        print("You have", lives, "lives left and you have used these letters: ", " ".join(used_letters))

        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1
                print('Letter guess is not in the word.')

        elif user_letter in used_letters:
            print("You have already used that character. Please try again.")

        else:
            print("Invalid character. Insert only alphabet.")

    if lives == 0:
        print("You have no more lives, you lost! The word was", word)
    else:
        print("You guessed the word", word, "!")


hangman()