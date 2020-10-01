from string import ascii_lowercase
from words import randomWord


def getAttempt():
    while True:
        num_attempts = input(
            'How many incorrect attempts do you want? [1-20] ')
        try:
            num_attempts = int(num_attempts)
            if 1 <= num_attempts <= 20:
                return num_attempts
            else:
                print('{0} is not between 1 and 20'.format(num_attempts))
        except ValueError:
            print('{0} is not an integer between 1 and 20'.format(
                num_attempts))

def get_minWord():
    while True:
        minWord = input(
            'What minimum word length do you want? [4-16] ')
        try:
            minWord = int(minWord)
            if 4 <= minWord <= 16:
                return minWord
            else:
                print('{0} is not between 4 and 16'.format(minWord))
        except ValueError:
            print('{0} is not an integer between 4 and 16'.format(
                minWord))

def displayWord(word, idxs):
    if len(word) != len(idxs):
        raise ValueError('Word length and indices length are not the same')
    displayed_word = ''.join(
        [letter if idxs[i] else '*' for i, letter in enumerate(word)])
    return displayed_word.strip()

def nextLetter(remaining_letters):
    if len(remaining_letters) == 0:
        raise ValueError('There are no remaining letters')
    while True:
        next_letter = input('Choose the next letter: ').lower()
        if len(next_letter) != 1:
            print('{0} is not a single character'.format(next_letter))
        elif next_letter not in ascii_lowercase:
            print('{0} is not a letter'.format(next_letter))
        elif next_letter not in remaining_letters:
            print('{0} has been guessed before'.format(next_letter))
        else:
            remaining_letters.remove(next_letter)
            return next_letter

"""Play a game of hangman.
Returns if the player wants to retry."""

def hangman():
    name = input('What is your name? ')
    print('Welcome to Hangman!!', name)
    print('Starting a game of Hangman...')
    attempts_remaining = getAttempt()
    minWord = get_minWord()


    print('Selecting a word...')
    word = randomWord(minWord)
    print()


    idxs = [letter not in ascii_lowercase for letter in word]
    remaining_letters = set(ascii_lowercase)
    wrong_letters = []
    word_solved = False

# Main game loop
    while attempts_remaining >= 1 and not word_solved:
        print('Word: {0}'.format(displayWord(word, idxs)))
        print('Attempts Remaining: {0}'.format(attempts_remaining))
        print('Previous Guesses: {0}'.format(' '.join(wrong_letters)))


        next_letter = nextLetter(remaining_letters)

        if next_letter in word:
            print('{0} is in the word!'.format(next_letter))
            for i in range(len(word)):
                if word[i] == next_letter:
                    idxs[i] = True
        else:
            print('{0} is NOT in the word!'.format(next_letter))
            attempts_remaining -= 1
            wrong_letters.append(next_letter)

        if False not in idxs:
            word_solved = True
        print()

#Game OVER!!!
    print('The word is {0}'.format(word))
    if word_solved:
        print('Congratulations! You won!', name)
    else:
        print('Try again next time!', name)

    try_again = input('Would you like to try again? [Y/N] ')
    return try_again.lower() == 'y'

if __name__ == '__main__':
    while hangman():
        print()
