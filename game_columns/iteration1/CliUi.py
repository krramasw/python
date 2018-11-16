

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

            ## Dummy or Partial implementation

            self.process_user_input(user_input)
            self.grid.intialize_faller()
            self.grid.dump()
            self.grid.descend(self)

            if self.grid.check_match() :
                self.grid.descend(self)

            if self.grid.faller.frozen :
                return "FALLER_FROZEN"

            if self.grid.is_game_over() :
                return "GAME_OVER"

            time.sleep(1)



    def process_user_input(self,user_input):

        ## Dummy or No implementation

        if user_input == "<":
            print ("")

        elif user_input == ">":
            print("")

        elif user_input[:1] == "F":

            words = user_input.split(" ")
            col_faller = words[1]
            c1 = words[2]
            c2 = words[3]
            c3 = words[4]

            faller = Faller(col_faller, c1, c2, c3)
            self.grid.faller = faller

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

        if cliUi.run(step) == "GAME_OVER" :
            print ("Game over... Exiting.." )
            exit(1)

    print (" Game Done ...")