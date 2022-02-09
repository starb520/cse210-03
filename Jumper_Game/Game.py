from word import Word
from terminal import Terminal
from JumperPic import Jumper

class Game:
    '''Runs game.'''
    def __init__(self):
        ''' Attributes of Game'''
        self.rand_word = Word()
        self.word = self.rand_word.random_word()
        self.terminal = Terminal()

       

    def play_game(self):
        '''Calls the input, update, and output methods'''
        pass


    def input(self):






# word_blanks = [False for i in range(len(rand_word._word))]
# print(word_blanks)

# print(rand_word._word)

# letter_guess = " "
# while not(letter_guess.isalpha()) or len(letter_guess) != 1:
#     letter_guess = terminal.read_text("Guess a letter from [a-z]: ")
#     if not(letter_guess.isalpha()):
#         terminal.write_text("Choose a letter.")
#     elif len(letter_guess)!= 1:
#         terminal.write_text("Only one letter.")



# letter_is_in_word = False
# for letter in range(len(rand_word._word)):
#     if rand_word._word[letter] == letter_guess:
#         word_blanks[letter] = True

# print(word_blanks)
# for i in range(len(word_blanks)):
#     if word_blanks[i] == True:
#         print(rand_word._word[i], end=" ")
#     else:
        print("_", end=" ")






