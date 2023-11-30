import random

word_list = ['Mango','Lychee','Grapes','Melon','Peach']
# randomly generates words from list
word = random.choice(word_list)
# asking user to choose a single letter
guess = input('Enter a single letter: ')

def check_guess(guess):
    # change guess to lowercase
    guess = guess.lower()
    # check if guess is in word
    if guess in word:
       print(f"Good guess! '{guess}' is in the '{word}'.")
    else:
         print(f"Sorry, '{guess}' is not in the '{word}'. Try again")
         
def ask_for_input():
    while True:
     # ask user to chose a letter
           guess = input('Enter a single letter: ')
     # check if guess is a single letter
           if len(guess) == 1 and guess.isalpha():
              break
           else:
                print('Invalid letter. Please, enter a single alphabetical character.')

check_guess(guess)
ask_for_input()