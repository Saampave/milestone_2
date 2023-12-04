import random

# create a class called hangman
class Hangman:
      def __init__(self, word_list, num_lives=5):
          # Initialise list of words
          self.word_list = word_list
          # Initialise the number of lives the player has at the start of the game
          self.num_lives = num_lives
          # Initialise a list of guesses that have already been tried
          self.list_of_guesses = []
          # Random word to be guessed picked from word_list
          self.word = random.choice(self.word_list)
          # Initialise a list of letters with _ for each letter not yet guessed
          self.word_guessed = ['_' for _ in self.word]
          # Initialise the number of unique letters in the word
          self.num_letters = len(set(self.word))
  
      def check_guess(self, guess):
          # change guess to lowercase
          guess = guess.lower()
          # check if guess is in word
          if guess in self.word:
             print(f"Good guess! '{guess}' is in the word.")
          else:
            print(f"Sorry, '{guess}' is not in the word")
       
      def ask_for_input(self):
          while True:
                guess = input('Enter a single letter: ')
                # statement that runs if guess is not a single alphabetical character
                if len(guess) != 1 or not guess.isalpha():
                   print('Invalid letter. Please, enter a single alphabetical character.')
                   # checks if the guess is already in the list_of_guesses
                elif guess in self.list_of_guesses:
                     print('You already tried that letter!')
                else: 
                # call check_guess
                    self.check_guess(guess)
                # append guess to list_of_guesses
                    self.list_of_guesses.append(guess)
                break

words = ['Mango','Lychee','Grapes','Melon','Peach']          
hangman_game = Hangman(words)
hangman_game.ask_for_input()