###
# Hangman
#
# Cody Heinks
###

import random
import sys
import string

guesses = 7
word_bank = ['A smooth sea never made a skillful sailor.', 'creativity', 'The only place where success comes before \
work is the dictionary.', 'believe', 'Today is the first day of the rest of your life.', 'inspiration', 'An eye for a \
eye', 'achieve', 'God bless you.', 'Geometry', 'public education', ]
number = random.randint(0, (len(word_bank) - 1))
guess_word = word_bank[number]
guessWord_list = list(guess_word)
print('Thinking... \nOk, got it.')
blankStr = ''
list_of_guesses = list(string.punctuation)
list_of_guesses.append(' ')
list_of_guesses2 = []

while guesses > 0:
    what_player_sees = []
    user_input = input('Guess a letter. ')
    if user_input == guess_word:
        print('Congrats, you won!')
        sys.exit(0)
    if user_input in list_of_guesses:
        print('You already guessed that. ')
    else:
        list_of_guesses.append(user_input.lower())
        list_of_guesses2.append(user_input.upper())

        for letter in range(len(guessWord_list)):
            if guessWord_list[letter] in list_of_guesses:
                what_player_sees.append(guessWord_list[letter])
            elif guessWord_list[letter] in list_of_guesses2:
                what_player_sees.append(guessWord_list[letter])
            else:
                what_player_sees.append('_ ')

        reveal = blankStr.join(what_player_sees)
        print(reveal)
        if reveal == guess_word:
            print('Congrats, you won!')
            sys.exit(0)
        if user_input.lower() not in guessWord_list:
            if user_input.upper() not in guessWord_list:
                guesses -= 1
                print('You have', guesses, 'guesses left.')
if number % 2 != 0:
    print('Sorry, you lost. My word was %s' % guess_word)
else:
    print('Sorry, you lost. My phrase was %s' % guess_word)
