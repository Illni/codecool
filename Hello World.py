
import sys

class Program():
    def __init__(self):
        self.name = "World"
    def ArgCheck(self):
        if(len(sys.argv) > 1):
            self.name = sys.argv[1]
    def PrintIt(self):
        print("Hello " + str(self.name) + "!")

prog1 = Program()
prog1.ArgCheck()
prog1.PrintIt()
