
Authod : Krishnan & H

Iteration 1 Implementation summary


        In this iteration, we have defined Classes/Objects, create simple and dummy interfaces with static values in some places.
        The idea is to define the skeleton and make it work for hardcodeed values.

                - Jewel.py
                            have data structure to represent Jewel color and text

                - Faller.py

                            have data structure to represent Faller components ( c1, c2, c3 ) and state of Faller (frozen and falling)
                            have methods move_column and move_row
                                    move_row() is called up on when Faller is falling in the given row
                                    move_column() is called up on when User moves the Faller to different row using < or > command


                - Grid.py
                            have data structure to represent Board and state of the board any time
                            have following methods

                                is_game_over()
                                intialize_faller()
                                descend()
                                check_match()
                                is_move_valid()
                                move_faller()
                                update_faller()

                - CliUi.py

                            Is the CLI based interface for this game.



                - run_cli.py

                            Main program for the game. This will

                                 initialize Game by creating new Grid object
                                 create some sample move
                                 call CliUi to manage




