from gameboard import GameBoard
from player import HumanPlayer, ComputerPlayer
from gamegui import GameGUI



def main():

    gboard = GameBoard()
    # create player 1 object
    p1 = HumanPlayer("X", gboard)
    # TODO: create player 2 object
    p2 = HumanPlayer("O", gboard)

    
    print("\nDefault grid is 6 rows x 7 columns.")
    custom = input("Would you like to choose a grid size? (y/n): ").strip().lower()
    if custom == "y":
        try:
            rows = int(input("Rows, minimum 4: "))
            cols = int(input("Columns, minimum 4: "))
            gboard = GameBoard(max(4, rows), max(4, cols))
        except ValueError:
            print("Invalid grid size. Using default 6 x 7.")
            gboard = GameBoard()

    load_choice = input("Load saved game? (y/n): ").strip().lower()
    if load_choice == "y":
        filename = input("Filename, or press Enter for connect4_save.txt: ").strip()
        if filename == "":
            filename = "connect4_save.txt"
        gboard.load_from_file(filename)

    print("\nChoose game mode:")
    print("\t1. Human vs Human")
    print("\t2. Human vs Computer")
    print("\t3. Computer vs Computer")
    mode = input("Choice: ").strip()

    if mode == "1":
        p1 = HumanPlayer("X", gboard)
        p2 = HumanPlayer("O", gboard)
    elif mode == "3":
        p1 = ComputerPlayer("X", gboard)
        p2 = ComputerPlayer("O", gboard)
    else:
        p1 = HumanPlayer("X", gboard)
        p2 = ComputerPlayer("O", gboard)

    p1.set_player_colour(choose_colour("Player X"))
    p2.set_player_colour(choose_colour("Player O", p1.get_player_colour()))

    if isinstance(p1, ComputerPlayer):
        p1.set_difficulty(choose_difficulty("Computer X"))
    if isinstance(p2, ComputerPlayer):
        p2.set_difficulty(choose_difficulty("Computer O"))


    # TODO: Place players 1 and 2 in tuple for turn based game. 
    players_lst = (p1, )
    players_lst = (p1, p2)

    winner = False

    # show empty grid at the beginning of the game
    gboard.show_board_dynamic()

    while (winner == False):
        # This is to allow players to take turns. 
        # The game begins with the player at index zero in the tuple,
        # When the player completes its turn, the next player in the tuple will be asked to play. 
        # If there is no winner, this will continue until reaching the end of the players list, 
        # and then we start again from the beggining of the list.

        for p in players_lst:
            p.play()
            # After each move, the board is shown on the screen
            gboard.show_board_dynamic()

            # TODO: Use the check_winner() method of the GameBoard class to check
            # if a player has won the game
            winner = False
            winner = gboard.check_winner()

            if winner == True:
                # Show current player's symbol as Winner, 
                # and terminate the game
                pass
                print("Player %s (%s) is the Winner!" %
                      (p.get_player_symbol(), p.get_player_colour()))
                break
            # TODO: Add an if statement to check if the board is full. If the board
            # is full, print a message and end the game
            if gboard.is_board_full():
                print("The board is full. The game is a draw.")
                winner = True
                break

        if winner == False:
            save_choice = input("Enter s to save, r to restart, or Enter to continue: ").strip().lower()
            if save_choice == "s":
                filename = input("Filename, or press Enter for connect4_save.txt: ").strip()
                if filename == "":
                    filename = "connect4_save.txt"
                gboard.save_to_file(filename)
            elif save_choice == "r":
                print("Restarting game...")
                main()
                return


def choose_colour(player_name, taken_colour=None):
    colours = ["red", "yellow", "blue", "green", "purple", "orange"]
    while True:
        print("\n%s, choose a colour:" % player_name)
        for i in range(len(colours)):
            if colours[i] != taken_colour:
                print("\t%d. %s" % (i + 1, colours[i]))
        choice = input("Enter colour number or name: ").strip().lower()
        if choice.isdigit():
            index = int(choice) - 1
            if index >= 0 and index < len(colours):
                choice = colours[index]
        if choice in colours and choice != taken_colour:
            return choice
        print("Invalid colour. Try again.")


def choose_difficulty(label):
    print("\nSelect difficulty for %s:" % label)
    print("\t1. Easy - random")
    print("\t2. Medium - strategic blocking")
    choice = input("Enter choice: ").strip()
    if choice == "1":
        return "easy"
    return "medium"


if __name__ == "__main__":
    print("Welcome to Connect4!")
    while True:
        print("Choose interface:")
        print("\t 1. Console")
        print("\t 2. GUI")
        choice = input("Enter number to choose interface or q to quit: ")
        if choice.lower() == "q":
            break
        if choice == "1":
            print("")
            main()
        elif choice == "2":
            b_gui = GameGUI()
            b_gui.initialise()
            break
