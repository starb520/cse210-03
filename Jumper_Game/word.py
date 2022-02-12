
import random


class Word:
    '''Has access to a random list of words. Has a function to choose a word
     from the random list of words.'''

    def __init__(self):

        # These are the three lists of words with different difficulties
        self._word_list_easy = ["cat", "dog", "red", "pot"]
        self._word_list_med = ["rain", "wear", "moon"]
        self._word_list_hard = ["wonder", "plenty", "teacher", "ebony"]

    def random_word(self, difficulty):
        '''Generate a random word from a list of words.'''
        if difficulty == 1:
            return random.choice(self._word_list_easy)
        elif difficulty == 2:
            return random.choice(self._word_list_med)
        elif difficulty == 3:
            return random.choice(self._word_list_hard)
        # Return the randomly chosen word according to the difficulty selected.
        
        



