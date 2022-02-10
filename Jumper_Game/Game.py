
from word import Word
from terminal import Terminal
from JumperPic import Jumper

class Game:
    '''Runs game.'''
    def __init__(self):
        ''' Attributes of Game'''
        self._rand_word = Word()
        self._terminal = Terminal()
        self._jumper = Jumper()
        self._word = " "
        self._is_playing = True
        self._num_wrong_guess = 0
        self._blanks = []
        

    def play_game(self):
        '''Calls the input, update, and output methods. Remember to 
           call random word to create new random word to play again.'''
        self._word = self._rand_word.random_word()
        self._jumper.parachute_pic(self._num_wrong_guess)
        self._jumper.man()
        self._blanks = ["_"] * len(self._word)

        while self._is_playing and self._num_wrong_guess < 4 and self.check_blanks():
            guess = self._do_inputs()
            self._do_updates(guess)
            self._do_outputs()
        self._play_again_prompt()

    def check_blanks(self):
        for item in self._blanks:
            if item == '_':
                return True
        return False

    def _do_inputs(self):
        '''Prompt user for a letter. Play again option'''
        letter_guess = " "
        while not(letter_guess.isalpha()) or len(letter_guess) != 1:
            letter_guess = self._terminal.read_text("Guess a letter from [a-z]: ")
            if not(letter_guess.isalpha()):
                self._terminal.write_text("That wasn't a letter.")
            elif len(letter_guess)!= 1:
                self._terminal.write_text("Only one letter.")
        return letter_guess

    def _do_updates(self, guess):
        '''See if letter is in word. Change "_" in word to that letter. If it
           was a wrong letter add to wrong letter guess'''
        is_right_guess = False
        for num in range(len(self._word)):
            if guess.lower() == self._word[num].lower():
                self._blanks[num] = guess.lower()
                is_right_guess = True
        if not is_right_guess:
            self._num_wrong_guess += 1


                
    def _do_outputs(self):
        '''Print out picture. Print the word/blanks '''
        for item in self._blanks:
            print(item, end=" ")
        print()

        self._jumper.parachute_pic(self._num_wrong_guess)
        self._jumper.man() 

    def _play_again_prompt(self):
        answer = self._terminal.read_text("Do you want to play again? [y.n]") 
        if answer.lower() == "y":
            self._is_playing = True
            self._num_wrong_guess = 0
            self.play_game()
        else:
            self._terminal.write_text("Thanks for playing.")
            self._is_playing = False
             



        

game = Game()
game.play_game()




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
<<<<<<< HEAD
        # print("_", end=" ")






=======
#         print("_", end=" ")
>>>>>>> 67ffae6369b407133287ca76d7be64de72d0a3e8
