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
        self.x = random.randint(300,700)
        i = len(self.displayword)
        if len(self.displayword) <= 4:
            while 4 - i != 0:
                self.wordSpeed += 0.1
                i += 1
        else:
            while i - 4 != 0:
                self.wordSpeed -= 0.1
                i -= 1
    yourWord = ""
    x = random.randint(300,700)
    y = 200