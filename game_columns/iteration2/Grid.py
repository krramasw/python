
import time

class Grid(object) :

    def __init__(self, rows, columns):

        self.rows = rows
        self.columns = columns
        self.state = [[" " for x in range(self.columns)] for y in range(self.rows)]
        self.faller=None


    def dump(self):
        print ("No of rows:", self.rows)
        print ("No of columns", self.columns)
        print ("State:")
        print (self.state)

    def is_game_over(self):

        ## Dummy or No implementation
        boolean = False
        return boolean

    def intialize_faller(self):

        r = int( self.rows)
        c = int( self.faller.col_location)

        self.state[0][c] = self.faller.block1
        self.state[1][c] = self.faller.block2
        self.state[2][c] = self.faller.block3



    def descend(self, cliUi):
        print ("Inside descend ...TBD")
        ## Dummy or No implementation



    def check_match(self):
        ## Dummy or No implementation
        print ("Inside check match ... TBD")
        return True

    def is_move_valid(self, row, col, faller):

        ## Dummy or No implementation
        return True


    def move_faller(self, row, col, faller):

        self.state[row - 1][col] = faller.block2
        self.state[row - 1][col] = faller.block2
        self.state[row - 1][col] = faller.block2


    def update_faller(self, faller):

        self.faller.frozen = True


if __name__ == '__main__' :

    print ("Inside Grid")