
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
        self._difficulty = self._terminal.read_text("Enter in a level of difficulty [1-3]: ")
        self._word = self._rand_word.random_word(int(self._difficulty))
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
        '''Prompt user for a letter. Continue to reprompt if an invalid 
           character is entered by the user.'''

        # Initialize the letter_guess variable to an invalid character so it
        # will enter the while loop and continue reprompting until user enters
        # a letter.   
        letter_guess = " "

        # While the user entry is not a letter or is more than one character
        # continue to reprompt. 
        while not(letter_guess.isalpha()) or len(letter_guess) != 1:
            letter_guess = self._terminal.read_text("Guess a letter from [a-z]: ")
            if not(letter_guess.isalpha()):
                self._terminal.write_text("That wasn't a letter.")
            elif len(letter_guess)!= 1:
                self._terminal.write_text("Only one letter.")

        # Once the user has entered a valid letter exit function and return the
        # the letter.
        return letter_guess

    def _do_updates(self, guess):
        '''Check if the letter entered by the user is in the randomly chosen 
           word. If letter is in word, put it into the blanks list in the 
           correct position. If the letter is not in the word, add one to the 
           number of wrong guesses array.'''
        
        # Initialize the bool to check for a right or wrong guess made by user.
        is_right_guess = False

        for num in range(len(self._word)):
            # Cast the user guess to a lowercase letter to compare it to the
            # letters in the random word.
            if guess.lower() == self._word[num].lower():
                self._blanks[num] = guess.lower()
                is_right_guess = True
        
        # If the letter chosen by the user is not in the word, add one to the 
        # number of wrong guesses. 
        if not is_right_guess:
            self._num_wrong_guess += 1


                
    def _do_outputs(self):
        '''Print out picture. Print the word/blanks '''

        # Print the blanks/letters for the user to reference when choosing a 
        # letter.
        for item in self._blanks:
            print(item, end=" ")
        print()

        # Print the parachute.
        self._jumper.parachute_pic(self._num_wrong_guess)

        # Print the jumper image, if user is out of guesses change the head to
        # an X.
        if self._num_wrong_guess < 4:
            self._jumper.man()
        else:
            self._jumper.x_man()

    def _play_again_prompt(self):
        '''Prompt the user if he/she wants to play again. If 'y' call the game
           loop, if 'n' change the is playing bool to False so the game ends.'''

        # Prompt user.
        answer = self._terminal.read_text("Do you want to play again? [y.n]") 

        # Cast user input to lower to cover more cases of user input.
        if answer.lower() == "y":
            self._is_playing = True
            self._num_wrong_guess = 0
            self.play_game()
        else:
            self._terminal.write_text("Thanks for playing.")
            self._is_playing = False
               





