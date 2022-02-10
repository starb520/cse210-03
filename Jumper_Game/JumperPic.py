
class Jumper:
    '''Jumper is responsible for a string of characters that look like
    a parachute and a man'''

    def __init__(self):
        self._parachute = ["   ___   ", "  /___\  ", "  \   /  ","   \ /   " ]
        self._man       = ["    O    ", "   /|\   ", "   / \  "]
        self._ground    = " ^^^^^^^  "
        self._x_man     = ["    X    ", "   /|\   ", "   / \  "]

    def parachute_pic(self, wrong_guesses):
        '''Print a picture of a parachute. Begin with index zero, but as the user 
           increases the number of incorrect guesses print less of the parachute.'''
        
        print()
        # As the number of wrong letter guesses from user increases, print less
        # of the the parachute.
        for i in range(wrong_guesses, len(self._parachute)):
            print(self._parachute[i])
        

    def man(self):
        '''Print a picture of a stick man.'''

        for i in range(len(self._man)):
            print(self._man[i])
        print()
        print(self._ground)

    def x_man(self):
        '''Print a picture of a stick man with an 'X' for the head.'''
        for i in range(len(self._man)):
            print(self._x_man[i])
        print()
        print(self._ground)
        
    

    