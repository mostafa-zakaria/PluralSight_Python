import random

def get_random_word():
    words = ['Juno', 'Hypatia', 'Achilles', 'Hector', 'Mulberry', 'Telephone', 'Alexandria']
    word = words[random.randint(0, len(words) - 1 )]
    return word

def show_word(word):
    for c in word:
        print(c, end=' ')
    print('')

def get_guess():
    print ('Enter a Letter: ')
    return(input())

def process_letter(letter, secret_word, blanked_word):
    flag = False
    for i in range(0, len(secret_word)):
        if secret_word[i] == letter:
            flag = True
            blanked_word[i] = letter
    return flag

def print_strikes(num):
    for i in range(0, num):
        print ("X ", end='')
    print('') 

def play_word_game():
    strikes = 0
    max_strikes = 3
    playing = True
    
    word = get_random_word()
    blanked_word = list("_" * len(word))
    
    while playing:
        show_word(blanked_word)
        letter = get_guess()
        if not process_letter(letter, word, blanked_word):
            strikes += 1
            print_strikes(strikes)

        if strikes >= max_strikes:
            playing = False

        if not "_" in blanked_word:
            playing = False

    if(strikes < max_strikes):
        print('Winner')
    else:
        print('Loser!')
        print('The word was> ' + word)
        

print('Game Started')

play_word_game()
