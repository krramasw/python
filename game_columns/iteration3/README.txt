
Authod : Krishnan & H

Iteration 3 Implementation summary


        In this iteration, we have implemented

                descend.py and check_match.py

                of Grid.py


        Note that we HAVE NOT implemented all the functionality needed in
            descend()
            check_match()


        In this iteration

            descend()
                In this iteration, we have implemented state adjustment of Falling of current Faller. We YET to implement another method (let us call)
                decend_for_other_columns(), when a check_match is true.  We will implement decend_for_other_columns() in iteration 4


            check_match()
                In this iteration, we have implemented only Horizontal match. We YET to implement vertical and diagonal match. We will implement the horizontal and
                diagonal match in iteration 4






How to Run ?

        cd to ./iteration1 directory

        python run_cli.py

        enter "TEST" as the mode

        now run_cli.py will simulate steps for actions ["F 3 X Y Z", "F 2 S S Z", "F 1 A B Z"]

        You will see the state of Grid getting dumped