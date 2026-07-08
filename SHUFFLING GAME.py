from random import shuffle

my_list = [' ', 'O', ' ']
guess = ''

#FLOW --> SHUFFLE, GUESS, CHECK GUESS

def shuffle_list(my_list):
    shuffle(my_list)
    return my_list


def guessed():
    global guess
    while guess not in ['0', '1', '2']:
        guess = input('Enter a number between 0 and 2 ')
    return int(guess)

def check_guess(my_list, guess):
    if my_list[guess] == 'O':
        print('Correct!')
        print(my_list)
    else:
        print('Wrong. Try again...')
        print(my_list)

shuffled = shuffle_list(my_list)
guess = guessed()
check_guess(shuffled, guess)