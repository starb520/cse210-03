import random

class Word:
    '''Has access to a random list of words. Has a function to choose a word
     from the random list of words.'''

    def __init__(self):

        # This is a list of words. Could import a dictionary to supply the
        # list of words. 
        self._word_list = ["cat", "dog", "red", "rain"]

    def random_word(self):
        '''Generate a random word from a list of words.'''
        return random.choice(self._word_list)
        

        # Not sure if self._word needs to be returned since the method has access
        # to it's attributes.
        # return self._word


