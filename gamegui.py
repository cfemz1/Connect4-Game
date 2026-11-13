import tkinter
from sys import exit
from tkinter import messagebox
from gameboard import GameBoard
from player import HumanPlayer
from player import ComputerPlayer

class GameGUI:

    def __init__(self):

        self.mw = tkinter.Tk()
        self.mw.title("Connect4")
        self.mw.configure(bg="#1a1a2e")
        self.animating = False
        self.game_over = False




    def clicked_btn(self,x, y):

        if self.animating == True or self.game_over == True:
            return

        p = self.players_lst[self.current_player_index]

        button = self.buttons_2d_list[x][y] # get the button instance from the list
        if button["text"] == " ":

            # TODO: Call (use) the make_move() method from the GameBoard class to 
            # place the player's symbol on the board and then call (use) the
            # update_button_text() method of the GameGUI class to place the symbol
            # on the GUI grid
            placed_row = self.gboard.make_move(y, p.get_player_symbol())
            if placed_row == -1:
                return
            self.update_button_text(y, p.get_player_symbol())


            # TODO: Use the check_winner() method of the GameBoard class to check
            # if a player has won the game
            winner = False
            winner = self.gboard.check_winner()

            if winner == True:
                # Show current player's symbol as Winner, and end the game
                win_messge = ("Player %s is the Winner!" % p.get_player_symbol())
                messagebox.showinfo("Winner Info ",win_messge)
                self.mw.destroy()
                exit()

            # TODO: Add an if statement to check if the board is full. If the board
            # is full, display a popup window with an info message and end the game
            if self.gboard.is_board_full():
                messagebox.showinfo("Draw Info", "The board is full. The game is a draw.")
                self.mw.destroy()
                exit()


            # Change player index to allow the next player to play. 
            self.current_player_index += 1
            if self.current_player_index >= len(self.players_lst):
                self.current_player_index = 0

            # If it is computer player's turn, make the next move
            p = self.players_lst[self.current_player_index]
            if isinstance(p, ComputerPlayer):
                self.mw.after(2000, self.__computer_turn)


    def update_button_text(self, col, element):
        # TODO: Using a for loop, find the first blank space or button (button["text"] == " ")
        # in the specified column (col) and change its value to the given element
        # Hint: You can also disable this button, so it cannot be clicked again in the future
        pass
        landing_row = -1
        board = self.gboard.get_board()
        for row in range(self.gboard.get_num_rows()):
            if board[row][col] == element and self.buttons_2d_list[row][col]["text"] == " ":
                landing_row = row
                break

        if landing_row == -1:
            return

        colour = self.__get_colour_for_symbol(element)
        self.__animate_disc(col, landing_row, element, colour)


    def __initialise_game(self, gboard, players_lst, current_player_index = 0):
        self.gboard = gboard
        # TODO: Initialise other attributes of the class (players_lst, current_player_index)
        self.players_lst = players_lst
        self.current_player_index = current_player_index


        self.winner = False
        # TODO: Initialise buttons and add to buttons list (nested for loop)
        for x in range(gboard.get_num_rows()):
            for y in range(gboard.get_num_cols()):
                button = tkinter.Button(self.mw, text=" ", width=4, height=2,
                                        bg="#16213e", fg="white",
                                        font=("Arial", 14, "bold"),
                                        command=lambda row=x, col=y: self.clicked_btn(row, col))
                button.grid(row=x, column=y, padx=2, pady=2)
                self.buttons_2d_list[x][y] = button

        restart_btn = tkinter.Button(self.mw, text="Restart",
                                     command=self.__restart_game)
        restart_btn.grid(row=gboard.get_num_rows(), column=0,
                         columnspan=2, sticky="we")

        save_btn = tkinter.Button(self.mw, text="Save",
                                  command=self.__save_game)
        save_btn.grid(row=gboard.get_num_rows(), column=2,
                      columnspan=2, sticky="we")

        load_btn = tkinter.Button(self.mw, text="Load",
                                  command=self.__load_game)
        load_btn.grid(row=gboard.get_num_rows(), column=4,
                      columnspan=max(1, gboard.get_num_cols() - 4), sticky="we")

        # If it is computer player's turn, make the first move
        current_player = self.players_lst[self.current_player_index]
        if isinstance(current_player, ComputerPlayer):
            current_player.play()



    def initialise(self):
        # Initialise the GameBoard. Later, this can be initialised with custom grid size
        # based on user input
        gboard = GameBoard()
        setup = self.__setup_screen()
        gboard = GameBoard(setup["rows"], setup["cols"])
        # Initialise buttons list for the GUI based on game board's size (rows and columns)
        self.buttons_2d_list =  []
        for i in range (gboard.get_num_rows()):
            self.row = [' '] * gboard.get_num_cols()
            self.buttons_2d_list.append(self.row)
        # Initialise players and players list
        p1 = ComputerPlayer("O", gboard, self.buttons_2d_list)
        # TODO: Create 2nd player object (p2) and add it to the players list
        p2 = HumanPlayer("X", gboard)

        if setup["mode"] == "Human vs Human":
            p1 = HumanPlayer("X", gboard)
            p2 = HumanPlayer("O", gboard)
        elif setup["mode"] == "Computer vs Computer":
            p1 = ComputerPlayer("X", gboard, self.buttons_2d_list)
            p2 = ComputerPlayer("O", gboard, self.buttons_2d_list)
        else:
            p1 = HumanPlayer("X", gboard)
            p2 = ComputerPlayer("O", gboard, self.buttons_2d_list)

        p1.set_player_colour(setup["p1_colour"])
        p2.set_player_colour(setup["p2_colour"])

        if isinstance(p1, ComputerPlayer):
            p1.set_difficulty(setup["difficulty"])
        if isinstance(p2, ComputerPlayer):
            p2.set_difficulty(setup["difficulty"])

        players_lst = (p1, )
        players_lst = (p1, p2)
        # TODO: Initialise the game using the game board and the players list
        # Hint: use the __initialise_game() method
        self.__initialise_game(gboard, players_lst)


        tkinter.mainloop()


    def __setup_screen(self):
        setup_window = tkinter.Toplevel(self.mw)
        setup_window.title("Connect4 Setup")
        setup_window.configure(bg="#1a1a2e")
        setup_window.grab_set()

        rows_var = tkinter.IntVar(value=6)
        cols_var = tkinter.IntVar(value=7)
        mode_var = tkinter.StringVar(value="Human vs Computer")
        p1_colour_var = tkinter.StringVar(value="red")
        p2_colour_var = tkinter.StringVar(value="yellow")
        difficulty_var = tkinter.StringVar(value="medium")

        tkinter.Label(setup_window, text="Rows", bg="#1a1a2e", fg="white").grid(row=0, column=0)
        tkinter.Spinbox(setup_window, from_=4, to=12, textvariable=rows_var).grid(row=0, column=1)

        tkinter.Label(setup_window, text="Columns", bg="#1a1a2e", fg="white").grid(row=1, column=0)
        tkinter.Spinbox(setup_window, from_=4, to=12, textvariable=cols_var).grid(row=1, column=1)

        tkinter.Label(setup_window, text="Mode", bg="#1a1a2e", fg="white").grid(row=2, column=0)
        tkinter.OptionMenu(setup_window, mode_var,
                           "Human vs Human", "Human vs Computer", "Computer vs Computer").grid(row=2, column=1)

        tkinter.Label(setup_window, text="Player X Colour", bg="#1a1a2e", fg="white").grid(row=3, column=0)
        tkinter.OptionMenu(setup_window, p1_colour_var,
                           "red", "yellow", "blue", "green", "purple", "orange").grid(row=3, column=1)

        tkinter.Label(setup_window, text="Player O Colour", bg="#1a1a2e", fg="white").grid(row=4, column=0)
        tkinter.OptionMenu(setup_window, p2_colour_var,
                           "yellow", "red", "blue", "green", "purple", "orange").grid(row=4, column=1)

        tkinter.Label(setup_window, text="Computer Difficulty", bg="#1a1a2e", fg="white").grid(row=5, column=0)
        tkinter.OptionMenu(setup_window, difficulty_var,
                           "easy", "medium").grid(row=5, column=1)

        result = {}

        def start():
            if p1_colour_var.get() == p2_colour_var.get():
                messagebox.showerror("Colour Error", "Players must choose different colours.")
                return
            result["rows"] = rows_var.get()
            result["cols"] = cols_var.get()
            result["mode"] = mode_var.get()
            result["p1_colour"] = p1_colour_var.get()
            result["p2_colour"] = p2_colour_var.get()
            result["difficulty"] = difficulty_var.get()
            setup_window.destroy()

        tkinter.Button(setup_window, text="Start", command=start).grid(row=6, column=0, columnspan=2, sticky="we")

        self.mw.wait_window(setup_window)
        if result == {}:
            result["rows"] = 6
            result["cols"] = 7
            result["mode"] = "Human vs Computer"
            result["p1_colour"] = "red"
            result["p2_colour"] = "yellow"
            result["difficulty"] = "medium"
        return result

    def __computer_turn(self):
        if self.animating == True or self.game_over == True:
            self.mw.after(100, self.__computer_turn)
            return
        p = self.players_lst[self.current_player_index]
        if isinstance(p, ComputerPlayer):
            col = p.choose_col()
            self.clicked_btn(0, col)

    def __get_colour_for_symbol(self, symbol):
        colours = {
            "red": "#e94560",
            "yellow": "#f5a623",
            "blue": "#3498db",
            "green": "#2ecc71",
            "purple": "#9b59b6",
            "orange": "#e67e22"
        }
        for player in self.players_lst:
            if player.get_player_symbol() == symbol:
                return colours.get(player.get_player_colour(), "#ffffff")
        return "#ffffff"

    def __animate_disc(self, col, landing_row, element, colour):
        self.animating = True
        self.__animation_step(0, col, landing_row, element, colour)

    def __animation_step(self, row, col, landing_row, element, colour):
        if row > 0:
            board = self.gboard.get_board()
            if board[row - 1][col] == " ":
                self.buttons_2d_list[row - 1][col].config(text=" ", bg="#16213e")

        if row <= landing_row:
            self.buttons_2d_list[row][col].config(text=element, bg=colour, fg="white")
            self.mw.after(70, lambda: self.__animation_step(row + 1, col, landing_row, element, colour))
        else:
            self.buttons_2d_list[landing_row][col].config(
                text=element, bg=colour, fg="white", state="disabled",
                disabledforeground="white")
            self.animating = False

    def __restart_game(self):
        self.mw.destroy()
        new_game = GameGUI()
        new_game.initialise()

    def __save_game(self):
        self.gboard.save_to_file("connect4_save.txt")
        messagebox.showinfo("Save", "Game saved to connect4_save.txt")

    def __load_game(self):
        if self.gboard.load_from_file("connect4_save.txt"):
            board = self.gboard.get_board()
            for row in range(self.gboard.get_num_rows()):
                for col in range(self.gboard.get_num_cols()):
                    val = board[row][col]
                    if val == " ":
                        self.buttons_2d_list[row][col].config(text=" ", bg="#16213e", state="normal")
                    else:
                        colour = self.__get_colour_for_symbol(val)
                        self.buttons_2d_list[row][col].config(text=val, bg=colour, fg="white", state="disabled")
            messagebox.showinfo("Load", "Game loaded from connect4_save.txt")



def main():
    b_gui = GameGUI()
    b_gui.initialise()

if __name__ == "__main__":
    main()
