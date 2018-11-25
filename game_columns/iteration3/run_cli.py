

from Jewel  import *
from Faller import *
from Grid   import *
from CliUi  import *


if __name__ == '__main__' :

    print ("Inside iteration 3 : run  ")

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



    elif mode == "TEST" :

        rows = 8
        columns = 4

        grid = Grid(rows, columns)
        cliUi = CliUi(grid)

        test_board = ["F 3 X Y Z", "F 2 S S Z", "F 1 A B Z"]

        for step in test_board:

            if cliUi.run(step) == "GAME_OVER":
                print("Game over... Exiting..")
                exit(1)


    else :
        print("Not Valid option")

