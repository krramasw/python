

from Jewel  import *
from Faller import *
from Grid   import *

class CliUi(object) :

    def __init__(self,grid):
        self.grid = grid


    def print_state(self):

        print ("\a")
        for x in range(self.grid.rows):
            print("|", end="", flush=True)
            for y in range(self.grid.columns):
                print(" %s " % self.grid.state[x][y], end="", flush=True)
            print("|", flush=True)

        print(" ", end="", flush=True)
        print("-" * 3 * self.grid.columns, end="", flush=True)
        print(" ")

    def run(self, user_input=None):

        run_in_loop = False

        if user_input == None:
            user_input = input()
            run_in_loop = True

        while True:

            if user_input == None:
                user_input = input()

            self.process_user_input(user_input)
            self.grid.intialize_faller()
            self.grid.descend(self)
            #self.print_state()  Now self.grid.descend() will take care of printing..
            if self.grid.check_match():
                self.grid.descend(self)

            if self.grid.faller.frozen:
                return "FALLER_FROZEN"

            if self.grid.is_game_over():
                return "GAME_OVER"

            if run_in_loop == False:
                return

            time.sleep(.15)



    def process_user_input(self,user_input):


        if user_input == "<":
            self.grid.move_location(self.grid.faller.location_col - 1, self.grid.faller)

        elif user_input == ">":
            self.grid.move_location(self.grid.faller.location_col + 1, self.grid.faller)

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