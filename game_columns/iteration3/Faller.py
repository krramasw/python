


class Faller(object) :


    def __init__(self, col, c1, c2, c3):

        self.block1 = c1
        self.block2 = c2
        self.block3 = c3

        self.falling = True
        self.frozen  = False

        self.row_location = 0
        self.col_location = col

    def move_column(self, new_col):

        if not self.frozen:
            self.location_col = new_col

    def move_row(self,new_row):

        self.row_location = new_row


if __name__ == '__main__' :

    print ("Inside Faller")

