import os

def readfile():
    defaultlist = ["you", "are", "such", "an", "idiot"]
    if os.path.exists("source/words.txt"):
        try:
            f = open("source/words.txt", "r")
            words = f.read()
            if words != "":
                f.close()
                words = words.split("\n")
                return words
        except:
            print("File Handling Error")
    else:
        return defaultlist