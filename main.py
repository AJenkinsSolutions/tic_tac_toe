def main():
    class Grid:
        #   Class Attributes
        #   All grids will have the same margin and divide
        margin = '     |     |     '
        divide = '_____|_____|_____'

        #   Instance Attributes
        def __init__(self):

            #   Class Attributes
            self.rows = {
                'a0': '  -  ', 'b0': '|  -  |', 'c0': '  -  ',

                'a1': '  -  ', 'b1': '|  -  |', 'c1': '  -  ',

                'a2': '  -  ', 'b2': '|  -  |', 'c2': '  -  '
            }
            self.winner = None

        # Instance Method
        def display_grid(self):
            """
            Displays the visual representation of the current grid
            :return: Nothing
            """
            print(self.margin)
            print(f'{self.rows["a0"]}{self.rows["b0"]}{self.rows["c0"]}')
            print(self.divide)
            print(self.margin)
            print(f'{self.rows["a1"]}{self.rows["b1"]}{self.rows["c1"]}')
            print(self.divide)
            print(self.margin)
            print(f'{self.rows["a2"]}{self.rows["b2"]}{self.rows["c2"]}')
            print(self.margin)

        def pos_available(self, pos):
            """
            If '-' is in selected position>> then position is available.
            If !'-' position is unavailable/ occupied.
            :param pos: User input. for desired pawn placement
            :return: True or False
            """
            if '-' in grid.rows[pos]:
                # print('Debug:position available ')
                return True
            else:
                # print('Debug:position occupied')
                return False

        def place_pawn(self, pos, pawn):
            """
            Takes current players chosen position and Pawn, updates Grid Boxes.
            :param pos: Player chosen position
            :param pawn: Players Pawn
            :return:
            """
            self.rows[pos] = self.rows[pos].replace('-', pawn)
            return  # display grid ?

        def calculate_win(self, pawn):
            """
            Takes player pawn attribute. Runs three functions to check for a winning combination
            :param pawn: player pawn
            :return: True or false
            """
            if self.horizontal_win(pawn):
                return True
            elif self.vertical_win(pawn):
                return True
            elif self.diagonal_win(pawn):
                return True
            else:
                # print('No winning moves')
                return False

        def horizontal_win(self, pawn):
            """
            Condition 1:Pawn in the middle row(top, middle, bottom)
            Conditon 2:Pawn in both adjacent position from previous middle
            :param pawn: current players pawn 'X' or 'O'
            :return: True or False
            """
            # top row check
            if pawn in self.rows['b0']:
                # print('in top middle true ')
                # now check outter edges
                if pawn in self.rows['a0'] and pawn in self.rows['c0']:
                    # print('out edges true ')
                    # print('horizontal win top row')
                    return True
                else:
                    # print('Debug: No horizontal win')
                    return False
            # Check row 2
            elif pawn in self.rows['b1']:
                # print('in middle middle true ')
                # now check outter edges
                if pawn in self.rows['a1'] and pawn in self.rows['c1']:
                    # print('out edges true ')
                    # print('horizontal win middle row')
                    return True
                else:
                    # print('Debug: No horizontal win')
                    return False
            # Check Bottom Row
            elif pawn in self.rows['b2']:
                # print('in bottom middle true ')
                # now check outter edges
                if pawn in self.rows['a2'] and pawn in self.rows['c2']:
                    # print('out edges true ')
                    # print('horizontal win bottom row')
                    return True
                else:
                    # print('Debug: No horizontal win')
                    return False

            else:
                # print('Debug: No horizontal win')
                return False

        def vertical_win(self, pawn):
            """
            Condition 1: Player pawn must be present within the middle box of columns (a Or b Or c)
                            Example a1, b1, c1.
            Condition 2: player pawn must be present at either vertical side of middle box
                            Example pawn at 'a1' pawns must be present at 'a0' and a2>>
            :param pawn: player pawn
            :return: True or False
            """
            # Check middle position across board
            if pawn in self.rows['a1']:
                # print('in col a  middle true ')
                if pawn in self.rows['a0'] and pawn in self.rows['a2']:
                    # print('top and bottom edges true')
                    # print('Vertical win true ')
                    return True
                else:
                    # print('No veritcal win')
                    return False
            elif pawn in self.rows['b1']:
                # print('in col b  middle true ')
                if pawn in self.rows['b0'] and pawn in self.rows['b2']:
                    # print('top and bottom edges true')
                    # print('Vertical win true ')
                    return True
                else:
                    # print('No veritcal win')
                    return False
            elif pawn in self.rows['c1']:
                # print('in col c  middle true ')
                if pawn in self.rows['c0'] and pawn in self.rows['c2']:
                    # print('top and bottom edges true')
                    # print('Vertical win true ')
                    return True
                else:
                    # print('No veritcal win')
                    return False
            else:
                # print('Debug: No Vertical win')
                return False

        def diagonal_win(self, pawn):
            """
            Condition 1: Pawn must be present in middle box for any diagonal win
            Condition 2: Pawns must be present diagonal adjacent to middle boz to win
            :param pawn: player pawn
            :return: True or False
            """
            #   pawn in center box
            if pawn in self.rows['b1']:
                # print('pawn in center box')

                #   Left to right diagonal
                if pawn in self.rows['a0'] and pawn in self.rows['c2']:
                    # print('Diagonal winner left to right')
                    return True
                elif pawn in self.rows['c0'] and pawn in self.rows['a2']:
                    # print('Diagonal winner right to left')
                    return True
                else:
                    # print('no diagonal winner')
                    return False
            else:
                # print('No diagonal Win')
                return False

    class Player:
        def __init__(self):
            self.active = None
            self.pawn = None
            self.position_selection = None
            self.winner = None

        def activate(self):
            self.active = True

        def deactivate(self):
            self.active = False

    game_on = True
    game_menu_on = True
    picks = 0

    alpha = ['a', 'b', 'c']
    numberic = ['0', '1', '2']

    # Initialize Grid
    grid = Grid()
    # Initialize Players
    player1 = Player()
    player1.pawn = 'X'
    player2 = Player()
    player2.pawn = 'O'

    # Welcome message
    print('Welcome to TIC TAC TOE')

    while game_on and picks <9:
        if picks % 2 == 0:

            print('Picks:', picks)
            print('Player 1')
            # player1.active = True
            # player2.active = False
            grid.display_grid()
            answer_good = False
            while not answer_good:
            # Get player input
                choice = input('Please select a box').lower().strip()
                print(choice)
                if len(choice) == 2:
                    if choice[0] not in alpha or choice[1] not in numberic:
                        answer_good = False
                        print('Invalid Input: only a,b,c and 0, 1, 2')
                    else:
                        answer_good = True
                elif len(choice) < 2:
                    answer_good = False
                    print('To Short: Choice must me 2 Characters long\n Using only a,b,c and 1,2,3')
                elif len (choice) > 2:
                    answer_good = False
                    print('To Long: Choice must me 2 Characters long\n Using only a,b,c and 1,2,3')


            player1.pos_selection = choice

            # Check if position available
            if grid.pos_available(pos=player1.pos_selection):
                # Place pawn
                grid.place_pawn(player1.pos_selection, player1.pawn)
                # Show updated grid
                # Move result in win ?
                if grid.calculate_win(player1.pawn):
                    # Update winner
                    player1.winner = True
                    grid.winner = 'Player 1'
                    # Update Game Status
                    game_on = False
                else:
                    picks += 1
                    # return to main loop

        else:
            print('Picks:', picks)
            print('Player 2')
            # player2.active = True
            # player1.active = False
            grid.display_grid()
            player2.position_selection = input('Please select a box').lower()
            if grid.pos_available(pos=player2.position_selection):
                grid.place_pawn(player2.position_selection, player2.pawn)
                if grid.calculate_win(player2.pawn):
                    player2.winner = True
                    grid.winner = 'Player 2'
                    game_on = False
                else:
                    picks += 1
                    # return to main loop
    #   Exit messages
    grid.display_grid()
    print('Winner', grid.winner)



if __name__ == "__main__":
    main()
