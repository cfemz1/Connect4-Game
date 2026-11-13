class Player:

    def __init__(self, symbol, board):
        self.__symbol = symbol
        self._gboard = board
        self.__colour = ""
        self.__difficulty = "medium"

    def get_player_symbol(self):
        return self.__symbol

    def set_player_colour(self, colour):
        self.__colour = colour

    def get_player_colour(self):
        return self.__colour

    def set_difficulty(self, difficulty):
        self.__difficulty = difficulty

    def get_difficulty(self):
        return self.__difficulty


class HumanPlayer(Player):

    def __init__(self, symbol, board):
        Player.__init__(self, symbol, board)

    def play(self):
        # This method defines mechanism for the human players to play.
        # TODO: Get input from the player about the column in which they wish to place their mark.
        # Check if the input is valid and then place the player's symbol in that column,
        # if the column is not full
        print("Player %s turn" %self.get_player_symbol())
        while (True):
            col = int(input("Please enter column no : "))
            if col < 0 or col >= self._gboard.get_num_cols():
                print("Column out of range. Try again.")
            elif self._gboard.is_col_full(col):
                print("Column is full. Try again.")
            else:
                self._gboard.make_move(col, self.get_player_symbol())
                break

import random
import time

class ComputerPlayer(Player):

    def __init__(self, symbol, board, buttons_2d_list = []):
        Player.__init__(self, symbol, board)
        self.buttons_2d_list = buttons_2d_list

    def play(self):
        # If the computer player is created for the GUI game, it needs to use the
        # GUI's button list (therefore, buttons_2d_list will not be empty). In that
        # case, the __play_gui() method will be called. See __play_gui() method for info
        if len(self.buttons_2d_list) > 0:
            self.__play_gui()
            return
        print("Player %s turn" %self.get_player_symbol())
        # TODO: Generate a random number for the column and then use the make_move()
        # method to place the player's symbol in that column, if the column is not full
        print("Computer is thinking...")
        time.sleep(2)
        col = self.choose_col()
        self._gboard.make_move(col, self.get_player_symbol())
        print("Computer placed disc in column %d." % col)

    def __play_gui(self):
        # This method is to be used when the computer player is created for the GUI game.
        # TODO: Generate a random number for the column and then use the buttons_2d_list
        # to invoke() a click on the appropriate button of that column
        pass
        col = self.choose_col()
        for row in range(self._gboard.get_num_rows() - 1, -1, -1):
            button = self.buttons_2d_list[row][col]
            if button["text"] == " ":
                button.invoke()
                break

    def choose_col(self):
        if self.get_difficulty() == "easy":
            return self.__random_col()
        return self.__strategic_col()

    def __random_col(self):
        available = []
        for col in range(self._gboard.get_num_cols()):
            if not self._gboard.is_col_full(col):
                available.append(col)
        return random.choice(available)

    def __strategic_col(self):
        symbol = self.get_player_symbol()
        opponent = self.__get_opponent_symbol()

        for col in range(self._gboard.get_num_cols()):
            if not self._gboard.is_col_full(col):
                row = self._gboard.make_move(col, symbol)
                win = self._gboard.check_winner()
                self.__undo_move(row, col)
                if win:
                    return col

        for col in range(self._gboard.get_num_cols()):
            if not self._gboard.is_col_full(col):
                row = self._gboard.make_move(col, opponent)
                win = self._gboard.check_winner()
                self.__undo_move(row, col)
                if win:
                    return col

        centre = self._gboard.get_num_cols() // 2
        if not self._gboard.is_col_full(centre):
            return centre

        return self.__random_col()

    def __undo_move(self, row, col):
        if row == -1:
            return
        board = self._gboard.get_board()
        board[row][col] = " "
        self._gboard.set_board(board)

    def __get_opponent_symbol(self):
        if self.get_player_symbol() == "X":
            return "O"
        return "X"
