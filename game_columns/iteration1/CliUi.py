

from Jewel  import *
from Faller import *
from Grid   import *

class CliUi(object) :

    def __init__(self,grid):
        self.grid = grid


    def print_state(self):
        ## Dummy or No implementation
        print(" ")

    def run(self, user_input=None):

        while True:
            ## Dummy or No implementation
            self.process_user_input(user_input)
            self.grid.intialize_faller()
            self.grid.descend(self)
            if self.grid.check_match() :
                self.grid.descend(self)


    def process_user_input(self,user_input):

        ## Dummy or No implementation

        if user_input == "<":
            print ("")

        elif user_input == ">":
            print("")

        elif user_input[:1] == "F":
            print("")

        else:
            print("No such command exist")



if __name__ == '__main__' :

    print ("Inside cli")

    rows = 8
    columns = 4

    test_board = ["F 3 X Y Z", "F 2 S S Z", "F 1 A B Z"]

    grid = Grid(rows, columns)
    cliUi = CliUi(grid)

    for step in test_board  :
        cliUi.run(step)
