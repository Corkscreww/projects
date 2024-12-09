"""Первый проект книги, которую я нашел, скачал и начал прорабатывать
потихоньку. Всё буду сохранять на гитхабе в отдельном репозитории под названием
bigbookpython
"""

import random

NUM_DIGITS = 3
MAX_GUESSES = 10


def main():
    print('''Bagels, deductive logic game.
By Evgeny Shashkov. shashkow@gmail.com
    
    I am a thinking of a {}-digit number with no repeated digits. Try to guess
    what it is. Here are some clues:
    When I say:             That means:
    Pico                    One digit is correct but in the wrong position.
    Fermi                   One digit is correct and in the right position.
    Bagels                  No digit is correct.

    For example, if the correct secret number was 248 and your guess was 843,
    the clues would be Fermi Pico.'''.format(NUM_DIGITS))

    while True:
        # Variable with secret number, that the player must guess
        secretNum = getSecretNum()
        print('I have thought up a number.\nYou have {} guesses to get it.'
              ''.format(MAX_GUESSES))

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            # Continue iterations until get right guess
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Guess #{}: '.format(numGuesses))
                guess = input('> ')

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break # Right! Exit loop
            if numGuesses > MAX_GUESSES:
                print('You ran out of guesses.')
                print('The answer was {}'.format(secretNum))

        if playAgain():
            numGuesses = 1
            continue
        else:
            print('Thanks for playing!')
            break



def getSecretNum():
    '''Returns string of NUM_DIGITS unique random digits'''
    numbers = list('0123456789')
    random.shuffle(numbers)

    # Take first NUM_DIGITS digits from numbers list for our secret number
    secretNum = ''.join(numbers[:NUM_DIGITS])
    return secretNum

def getClues(guess, secretNum):
    '''Returns string wits clues pico, farmi and bagels for recieved pair of
    guess and secretNum'''
    if guess == secretNum:
        return 'You got it!'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            # Right num in right place
            clues.append('Fremi')
        elif guess[i] in secretNum:
            # Right num not in wrong place
            clues.append('Pico')
    if len(clues) == 0:
        return 'Bagels' # No right nums
    else:
        # Sorting clues in alphabetic order to their order doesn't give clue
        clues.sort()
        # Glue together list clues in single string value
        return ' '.join(clues)

def playAgain():
    # Asking player to play again
    ans = input('Do you want to play again? (Y/N)')
    if ans.lower().startswith('y'):
        return True
    return False

# If program is not imported, but is launched, launch it
if __name__ == '__main__':
    main()

