import random
# list of my five favourite fruits
favourite_fruit = ['Mango','Lychee','Grapes','Melon','Peach']
#assign the list to a variable called word_list
word_list = favourite_fruit
print(word_list)

# randomly generates words from list
word = random.choice(word_list)
print(word)

# asking user to choose a single letter
guess = input('Enter a single letter: ')
# check guess is alphabetical
if len(guess) == 1 and guess.isalpha():
   print('Good guess!')
else:
    print('Oops! That is not a valid option.')
