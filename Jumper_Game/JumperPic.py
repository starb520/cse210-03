class Jumper:
    '''Jumper is responsible for a string of characters that look like
    a parachute and a man'''

    def __init__(self):
        self._parachute = ["   ___   ", "  /___\  ", "  \   /  ","   \ /   " ]
        self._man       = ["    O    ", "   /|\   ", "   / \  "]

    def parachute_pic(self):
        print()
        x = 0
        for i in range(x, len(self._parachute)):
            print(self._parachute[i])

    def man(self):
        for i in range(len(self._man)):
            print(self._man)

    