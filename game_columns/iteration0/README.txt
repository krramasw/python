
Author : Krishnan 


Project Description


Design and Implementation approach

    We are following iterative approach to design and implementation. Following are the goals of each iteration.
    We will start defining object/modules and dummy interfaces and keep adding feature in each iteration.


    iteration 0

            - Analysis
            - Propose high level classes
            - High level Objects/Relationships diagram
            - High level plan for each iteration 1

            Deliverables :

                One page Classes/Objects and initial methods diagram


    iteration 1

              The goal of this iteration 1 is to realize the end to end classes and
              interaction among themselves with static/hard-coded methods returning values

              Deliverables :

                    - Define classes and data structures for Grid, Faller and Jewel
                    - Define CliUi and methods that get the input and control the Grid

                    - Dummy implementation for key methods in the classes
                    - Make end to end work for one static test


    iteration 2

            The goal of this iteration 2 is to show the initial setup for one Faller object defined.
            the print_grid() function will actually display the Grid in Cli.

            Falling of Faller/components in the given Grid will be in iteration 3

            Deliverables :

                - Continue replacing hard-coded values with actual implementation
                - Accept input in CliUi
                - Come up with actual UI (cursor based) to display the state
                - Show the initial state of the board for following
                         test_board = ["F 3 X Y Z"]

                - Test programs



    iteration 3

            The goal of this iteration 3 is to implement the descent() method that actually make the Faller/components
            fall in the Grid.

            Deliverables :

                - Implement descent() method in Grid.py
                - Show the progress for one test case of sequence
                         test_board = ["F 3 X Y Z", "F 2 S S Z", "F 1 A B Z"]

                - Test programs


    iteration 4


            The goal of this iteration 4 is to implement move_faller() method and make them move work while Faller/components
            fall in the Grid.

            Deliverables :

                - Implement move_faller() method in Grid.py
                - Show the progress for one test case of sequence and simulate move operation
                         test_board = ["F 3 X Y Z", "F 2 S S Z", "F 1 A B Z"]

                - Test programs

    iteration 5

            Final implementation for Cli based Columns game. Implement rest of the functionalities that includes
            Faller disappear after matching Horizontally, vertically and diagonally.

            Deliverables

                - Faller matches and disappears
                - Control components like < and > works..

                - Test programs

    iteration 6

            Initial pygame based implementation
            - Test programs

    iteration 7

            Final pygame based implementation and document update
            Test programs





