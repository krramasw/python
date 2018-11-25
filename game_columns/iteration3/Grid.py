
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

        c = int( self.faller.col_location)
        #for c in range(self.columns):
        for x in range(self.rows):
            if self.state[x][c] == " ":
                for i in range(x, -1, -1):
                    if (i - 1 >= 0):
                        self.state[i][c] = self.state[i - 1][c]
                        self.state[i - 1][c] = " "
            cliUi.print_state()
            time.sleep(.45)




    def check_match(self):


        matched = False
        c = int( self.faller.col_location)
        for c in range(self.columns) :
            for x in range(self.rows):
                if self.state[x][c] != " ":
                    for i in range(x, -1, -1):
                        if (i - 1 >= 0) and ( c + 2 < self.columns) :

                            if self.state[i][c] == self.state[i][c+1] and self.state[i][c] == self.state[i][c + 2] :
                                self.state[i][c] = " "
                                self.state[i][c+1] = " "
                                self.state[i][c+2] = " "
                                matched = True



        return matched

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