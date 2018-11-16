

from Jewel  import *
from Faller import *
from Grid   import *
from CliUi  import *


if __name__ == '__main__' :

    print ("Inside iteration 1 : run  ")

    exiting = False

    mode = input()

    if mode == "EMPTY" :

        rows = int(input())
        columns = int(input())

        grid = Grid(rows, columns)
        cliUi = CliUi(grid)
        cliUi.run()

    elif mode == "CONTENT" :

        rows = int(input())
        columns = int(input())

        grid = Grid(rows, columns)
        cliUi = CliUi(grid)
        cliUi.run()

    elif mode == "RANDOM" :

        rows = 8
        columns = 4

        grid = Grid(rows, columns)
        cliUi = CliUi(grid)
        cliUi.run()

    else :
        print("Not Valid option")

