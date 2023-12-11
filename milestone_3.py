import random

word_list = ['Mango','Lychee','Grapes','Melon','Peach']
# randomly generates words from list
random_word = random.choice(word_list)
# asking user to choose a single letter
choose_a_letter = input('Enter a single letter: ')

def check_guess(choose_a_letter):
    # change guess to lowercase
    choose_a_letter = choose_a_letter.lower()
    # check if guess is in word
    if choose_a_letter in random_word:
       print(f"Good guess! '{choose_a_letter}' is in the '{random_word}'.")
    else:
         print(f"Sorry, '{choose_a_letter}' is not in the '{random_word}'. Try again")
         
def ask_for_input():
    while True:
     # ask user to chose a letter
           choose_a_letter = input('Enter a single letter: ')
     # check if guess is a single letter
           if len(choose_a_letter) == 1 and choose_a_letter.isalpha():
              break
           else:
                print('Invalid letter. Please, enter a single alphabetical character.')

check_guess(choose_a_letter)
ask_for_input()