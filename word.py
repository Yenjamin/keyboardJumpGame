#from random_word import RandomWords
import random
import filehandler

class word():
    def __init__(self, wordSpeed):
        if wordSpeed < 10:
            self.wordSpeed = wordSpeed
        else:
            self.wordSpeed = 10
        #self.displayword = RandomWords().get_random_word()
        self.displayword = random.choice(filehandler.readfile())
    yourWord = ""
    x = random.randint(300,700)
    y = 200