import random

NUM_DIGITS = 3
MAX_GUESS = 10

def main():
    print(
        'Лалала хуё моё\n'
        'Число из {} цифр, даётся {} попыток.'.format(NUM_DIGITS,MAX_GUESS)
    )
    numGuesses = 1
    while True:
        secretNum = getSecretNum()

        print('Число загадано!')
        while numGuesses <= MAX_GUESS:
            guess = input('Попытка № {}. Пробуй > '.format(numGuesses))
            print(getClue(guess, secretNum))
            numGuesses += 1

            if guess == secretNum:
                break
            elif numGuesses == MAX_GUESS:
                print('Подсказки кончились! Загаданное число: {}'.format(secretNum))
                break

        if playAgain():
            numGuesses = 1
            continue
        else:
            break

    print('Спасибо за игру!')

    
def getSecretNum():
    num = list('0123456789')
    random.shuffle(num)
    return ''.join(num[:NUM_DIGITS])

def playAgain():
    ans = input('Играем еще раз? (y/n) -> ')
    if ans.lower().startswith('y'):
        return True
    return False

def getClue(guess, secretNum):
    clues = {
        1: 'Почти',
        2: 'Попал',
        3: 'Всё мимо'
    }

    if guess == secretNum:
        return 'Угадал!'
    else:
        clue = ''
        for i in range(len(guess)):
            if guess[i] == secretNum[i]:
                clue += (clues[2]) + ' '
            elif guess[i] in secretNum:
                clue += (clues[1]) + ' '
        if len(clue) == 0:
            clue = clues[3]
    return clue

if __name__ == '__main__':
    main()

