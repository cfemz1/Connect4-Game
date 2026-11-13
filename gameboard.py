import json


class GameBoard:

    def __init__(self, num_rows=6, num_cols=7):
        self.__space = ' '
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__board =  []

        for i in range(self.__num_rows):
            row = [self.__space] * self.__num_cols
            self.__board.append(row)


    def get_num_rows(self):
        return self.__num_rows

    def get_num_cols(self):
        return self.__num_cols


    def is_board_full(self):
        # TODO: Return True if every space on the board has been taken. Otherwise return False.
        # Hint: You can reuse the code from the tic-tac-toe game and improve accordingly
        return False if self.__has_empty_space() else True

    def is_space_free (self, row, col):
        # TODO: Return True if the space in place row, col is free (equal to self.__space) in the board.
        # Otherwise return False.
        # Hint: You can reuse the code from the tic-tac-toe game and improve accordingly
        if row < 0 or row >= self.__num_rows:
            return False
        if col < 0 or col >= self.__num_cols:
            return False
        return True if self.__board[row][col] == self.__space else False

    def make_move(self, col, element):
        # TODO: Using a for loop, find the first blank space in the specified column (col),
        # from the botttom, and change its value to the given element
        if col < 0 or col >= self.__num_cols:
            return -1

        for row in range(self.__num_rows - 1, -1, -1):
            if self.__board[row][col] == self.__space:
                self.__board[row][col] = element
                return row

        return -1

    def show_board_dynamic(self):
        # TODO: Using a nested for loop, print the board in the console
        # Hint: You can reuse the code from show_board_dynamic() method of tic-tac-toe game
        # and improve accordingly.
        self.__print_horizontal_line()
        for row in range(self.__num_rows):
            print("|", end="")
            for col in range(self.__num_cols):
                print(" %s " % self.__board[row][col], end="|")
            print("")
            self.__print_horizontal_line()

        print(" ", end="")
        for col in range(self.__num_cols):
            print(" %d  " % col, end="")
        print("")

    def __print_horizontal_line(self):
        print("+", end="")
        for i in range(self.__num_cols):
            end = "+"
            print("---", end=end)
        print("")


    def check_winner(self):
        # Return True if a player has 4 pieces in a row horizontally or vertically or diagonally
        return self.__check_winner_hz() or self.__check_winner_vt() \
            or self.__check_winner_diag1() or self.__check_winner_diag2()
            # Uncomment the next line of code only when you have implemented  
            # the __check_winner_diag1() and self.__check_winner_diag2() methods for 50-59% marking criteria
            #or self.__check_winner_diag1() or self.__check_winner_diag2()



    def __check_winner_hz(self):
        # TODO: Return True if a player has 4 identical pieces (symbols) in a row horizontally
        # Hint: You can reuse the code from the tic-tac-toe game and improve accordingly
        for row in range(self.__num_rows):
            for col in range(self.__num_cols - 3):
                cell = self.__board[row][col]
                if cell != self.__space:
                    if cell == self.__board[row][col + 1] and cell == self.__board[row][col + 2] and cell == self.__board[row][col + 3]:
                        return True
        return False


    def __check_winner_vt(self):
        # TODO: Return True if a player has 4 identical pieces (symbols) in a row vertically
        # Hint: You can reuse the code from the tic-tac-toe game and improve accordingly
        for col in range(self.__num_cols):
            for row in range(self.__num_rows - 3):
                cell = self.__board[row][col]
                if cell != self.__space:
                    if cell == self.__board[row + 1][col] and cell == self.__board[row + 2][col] and cell == self.__board[row + 3][col]:
                        return True
        return False


    def __check_winner_diag1(self):
        # TODO: Return True if a player has 4 identical pieces (symbols) in a row
        # diagonally from left to right. 
        for row in range(self.__num_rows - 3):
            for col in range(self.__num_cols - 3):
                cell = self.__board[row][col]
                if cell != self.__space:
                    if cell == self.__board[row + 1][col + 1] and cell == self.__board[row + 2][col + 2] and cell == self.__board[row + 3][col + 3]:
                        return True
        return False

    def __check_winner_diag2(self):
        # TODO: Return True if a player has 4 identical pieces (symbols) in a row
        # diagonally from right to left. 
        for row in range(self.__num_rows - 3):
            for col in range(3, self.__num_cols):
                cell = self.__board[row][col]
                if cell != self.__space:
                    if cell == self.__board[row + 1][col - 1] and cell == self.__board[row + 2][col - 2] and cell == self.__board[row + 3][col - 3]:
                        return True
        return False

    def __has_empty_space(self):
        for row in range(self.__num_rows):
            for col in range(self.__num_cols):
                if self.__board[row][col] == self.__space:
                    return True
        return False

    def is_col_full(self, col):
        if col < 0 or col >= self.__num_cols:
            return True
        return self.__board[0][col] != self.__space

    def get_board(self):
        board_copy = []
        for row in self.__board:
            board_copy.append(row[:])
        return board_copy

    def set_board(self, board):
        self.__num_rows = len(board)
        if self.__num_rows > 0:
            self.__num_cols = len(board[0])
        else:
            self.__num_cols = 7
        self.__board = []
        for row in board:
            self.__board.append(row[:])

    def save_to_file(self, filename="connect4_save.txt"):
        data = {
            "num_rows": self.__num_rows,
            "num_cols": self.__num_cols,
            "board": self.__board
        }
        with open(filename, "w") as f:
            json.dump(data, f)
        print("Game saved to '%s'." % filename)

    def load_from_file(self, filename="connect4_save.txt"):
        try:
            with open(filename, "r") as f:
                data = json.load(f)
            self.__num_rows = data["num_rows"]
            self.__num_cols = data["num_cols"]
            self.__board = data["board"]
            print("Game loaded from '%s'." % filename)
            return True
        except FileNotFoundError:
            print("Save file '%s' was not found." % filename)
            return False
        except (KeyError, json.JSONDecodeError):
            print("Save file '%s' is not valid." % filename)
            return False
