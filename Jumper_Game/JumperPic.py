class Jumper:
    '''Jumper is responsible for a string of characters that look like
    a parachute and a man'''

    def __init__(self):
        self._parachute = ["   ___   ", "  /___\  ", "  \   /  ","   \ /   " ]
        self._man       = ["    O    ", "   /|\   ", "   / \  "]
        self._ground    = " ^^^^^^^  "
        
    def parachute_pic(self, wrong_guesses):
        print()
       
        for i in range(wrong_guesses, len(self._parachute)):
            print(self._parachute[i])
        

    def man(self):
        for i in range(len(self._man)):
            print(self._man[i])
        print(self._ground)
        
    

    