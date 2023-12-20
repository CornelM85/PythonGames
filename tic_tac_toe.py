import random

import customtkinter as ctk
from CTkMessagebox import CTkMessagebox


class TicTacToe(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.__player = None
        self.__computer = None

        self.__winner_list = [(0, 4, 8), (6, 7, 8), (1, 4, 7), (2, 5, 8), (2, 4, 6), (0, 1, 2), (0, 3, 6), (3, 4, 5)]

        self.resizable(width=False, height=False)

        self.configure(fg_color='#242424')

        self.title('Tic-tac-toe')
        self.__title_label = ctk.CTkLabel(self, text='Tic tac toe', font=ctk.CTkFont(size=30, weight='bold'),
                                          text_color='white')

        self.__new_game_btn = ctk.CTkButton(self, text='New Game', height=10, font=ctk.CTkFont(size=15),
                                            fg_color='transparent', anchor='w', hover=False, command=lambda: self.__reset_boxes())
        self.__game_difficulty = ctk.CTkSegmentedButton(self, values=['Easy', 'Normal', 'God Mode'], fg_color='#242424', selected_color='grey',
                                                        font=ctk.CTkFont(size=15), unselected_color='#242424', selected_hover_color='grey',
                                                        unselected_hover_color='#242424')
        self.__b1 = ctk.CTkButton(self, text='', corner_radius=0, height=150, width=150, font=ctk.CTkFont(size=100),
                                  command=lambda: self.__on_click(self.__b1))
        self.__b2 = ctk.CTkButton(self, text='', corner_radius=0, height=150, width=150, font=ctk.CTkFont(size=100),
                                  command=lambda: self.__on_click(self.__b2))
        self.__b3 = ctk.CTkButton(self, text='', corner_radius=0, height=150, width=150, font=ctk.CTkFont(size=100),
                                  command=lambda: self.__on_click(self.__b3))
        self.__b4 = ctk.CTkButton(self, text='', corner_radius=0, height=150, width=150, font=ctk.CTkFont(size=100),
                                  command=lambda: self.__on_click(self.__b4))
        self.__b5 = ctk.CTkButton(self, text='', corner_radius=0, height=150, width=150, font=ctk.CTkFont(size=100),
                                  command=lambda: self.__on_click(self.__b5))
        self.__b6 = ctk.CTkButton(self, text='', corner_radius=0, height=150, width=150, font=ctk.CTkFont(size=100),
                                  command=lambda: self.__on_click(self.__b6))
        self.__b7 = ctk.CTkButton(self, text='', corner_radius=0, height=150, width=150, font=ctk.CTkFont(size=100),
                                  command=lambda: self.__on_click(self.__b7))
        self.__b8 = ctk.CTkButton(self, text='', corner_radius=0, height=150, width=150, font=ctk.CTkFont(size=100),
                                  command=lambda: self.__on_click(self.__b8))
        self.__b9 = ctk.CTkButton(self, text='', corner_radius=0, height=150, width=150, font=ctk.CTkFont(size=100),
                                  command=lambda: self.__on_click(self.__b9))

        self.__title_label.grid(columnspan=3, row=0, pady=(40, 20))
        self.__new_game_btn.grid(row=1, column=0, pady=10)
        self.__game_difficulty.grid(row=1, columnspan=(2+3), pady=10)
        self.__b1.grid(row=2, column=0, padx=(2, 1), pady=1)
        self.__b2.grid(row=2, column=1, padx=1, pady=1)
        self.__b3.grid(row=2, column=2, padx=1, pady=1)
        self.__b4.grid(row=3, column=0, padx=(2, 1), pady=1)
        self.__b5.grid(row=3, column=1, padx=1, pady=1)
        self.__b6.grid(row=3, column=2, padx=1, pady=1)
        self.__b7.grid(row=4, column=0, padx=(2, 1), pady=1)
        self.__b8.grid(row=4, column=1, padx=1, pady=1)
        self.__b9.grid(row=4, column=2, padx=1, pady=1)

        self.__game_difficulty.set(value='Easy')

        self.__boxes = [self.__b1, self.__b2, self.__b3, self.__b4, self.__b5, self.__b6, self.__b7, self.__b8, self.__b9]

        self.__new_game_btn.bind('<Enter>', command=self.__on_enter, add='+')

        self.__new_game_btn.bind('<Leave>', command=self.__on_leave, add='+')

        self.__root_center_screen(window_height=598, window_width=458)

    def __root_center_screen(self, window_width: int, window_height: int):
        """
        Center the Application in the middle of the screen
        """
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x_coordinate = int(screen_width / 2 - window_width / 2)
        y_coordinate = int(screen_height / 2 - window_height / 2)

        self.geometry('{}x{}+{}+{}'.format(window_width, window_height, x_coordinate, y_coordinate))

    def __toplevel_center_root(self, window_name, width: int, height: int):
        """
        Center the window in the middle of the Application window
        """
        root_height = self.winfo_height()
        root_width = self.winfo_width()

        root_x = self.winfo_x()
        root_y = self.winfo_y()

        x = int(root_width / 2 - width / 2)
        y = int(root_height / 2 - height / 2)

        window_name.geometry('{}x{}+{}+{}'.format(width, height, x + root_x, y + root_y))

    def __player_window(self):
        """
        Window for choosing what the player option is: "X" or "0"
        """
        p_window = ctk.CTkToplevel(self, fg_color='#242424')

        p_window.resizable(width=False, height=False)

        p_window.title('Player')

        p_label = ctk.CTkLabel(p_window, text='Choose your weapon!', font=ctk.CTkFont(size=15, weight='bold'),
                               text_color='white')
        x_btn = ctk.CTkButton(p_window, text='X', width=50, height=50, font=ctk.CTkFont(size=30),
                              command=lambda: self.__player_weapon(x_btn))
        o_btn = ctk.CTkButton(p_window, text='0', width=50, height=50, font=ctk.CTkFont(size=30),
                              command=lambda: self.__player_weapon(o_btn))
        p_quit = ctk.CTkButton(p_window, text='Exit', width=50, font=ctk.CTkFont(size=15), command=p_window.destroy)

        p_label.grid(row=0, columnspan=4, padx=21, pady=(10, 4))
        x_btn.grid(row=1, column=1)
        o_btn.grid(row=1, column=2)
        p_quit.grid(row=2, columnspan=4, pady=20)

        self.__toplevel_center_root(p_window, width=200, height=170)

        p_window.wm_transient(self)

    def __player_weapon(self, btn):
        """
        Setting the player option and defining the computer option
        """
        self.__player = btn.cget('text')
        if self.__player is not None:
            CTkMessagebox(title='Info', message=f'You choose "{self.__player}" to be your weapon!',
                          width=10, height=10, font=(15, 15))

            self.__computer = '0' if self.__player == 'X' else 'X'

    def __game_mode(self):

        if self.__game_difficulty.get() == 'Easy':
            model_list = [(0, 1, 2), (0, 3, 6), (6, 7, 8), (2, 5, 8)]

        elif self.__game_difficulty.get() == 'Normal':
            model_list = [(0, 4, 8), (6, 7, 8), (1, 4, 7), (2, 5, 8), (2, 4, 6), (0, 1, 2)]

        else:
            model_list = self.__winner_list

        return model_list

    def __on_click(self, btn):
        """
        Action to perform if the player click a box
        """
        if self.__player is None:
            self.__player_window()
            self.__game_difficulty.configure(state='disabled')
        else:
            btn.configure(text=self.__player, state='disabled', text_color_disabled='white')
            self.__inter_moves(state='disabled')
            if self.__winner_check() is False:
                self.after(1000, lambda: self.__after_click())

    def __inter_moves(self, state=('normal' or 'disabled')):
        """
        Enabling and disabling the boxes of the Application
        """
        for box in self.__empty_boxes():
            box.configure(state=state)

    def __winner_check(self):
        """
        Checking if there is a winner
        """
        is_winner = False
        boxes_left = self.__empty_boxes()
        if len(boxes_left) <= 6:

            for x, y, z in self.__winner_list:

                if self.__boxes[x].cget('text') == self.__boxes[y].cget('text') == self.__boxes[z].cget(
                        'text') == self.__player:
                    self.__boxes[x].configure(text_color_disabled='yellow')
                    self.__boxes[y].configure(text_color_disabled='yellow')
                    self.__boxes[z].configure(text_color_disabled='yellow')
                    self.__message_box('You win!')

                    for btn in boxes_left:
                        btn.configure(state='disabled')
                    is_winner = True

                elif self.__boxes[x].cget('text') == self.__boxes[y].cget('text') == self.__boxes[z].cget(
                        'text') == self.__computer:
                    self.__boxes[x].configure(text_color_disabled='yellow')
                    self.__boxes[y].configure(text_color_disabled='yellow')
                    self.__boxes[z].configure(text_color_disabled='yellow')
                    self.__message_box('You lose!')

                    for btn in boxes_left:
                        btn.configure(state='disabled')
                    is_winner = True

        return is_winner

    def __after_click(self):
        """
        Action to perform after the box is clicked by the player
        """
        boxes_left = self.__empty_boxes()

        if self.__player is not None:

            if len(boxes_left) != 0:
                self.__inter_moves('normal')

                for x, y, z in self.__game_mode():

                    if (self.__boxes[x].cget('text') == self.__boxes[y].cget('text') == self.__computer) and (
                            self.__boxes[z].cget('text') == ''):
                        self.__boxes[z].configure(text=self.__computer, state='disabled', text_color_disabled='white')
                        break

                    elif (self.__boxes[x].cget('text') == self.__boxes[z].cget('text') == self.__computer) and (
                            self.__boxes[y].cget('text') == ''):
                        self.__boxes[y].configure(text=self.__computer, state='disabled', text_color_disabled='white')
                        break

                    elif (self.__boxes[y].cget('text') == self.__boxes[z].cget('text') == self.__computer) and (
                            self.__boxes[x].cget('text') == ''):
                        self.__boxes[x].configure(text=self.__computer, state='disabled', text_color_disabled='white')
                        break

                    elif (self.__boxes[x].cget('text') == self.__boxes[y].cget('text') == self.__player) and (
                            self.__boxes[z].cget('text') == ''):
                        self.__boxes[z].configure(text=self.__computer, state='disabled', text_color_disabled='white')
                        break

                    elif (self.__boxes[x].cget('text') == self.__boxes[z].cget('text') == self.__player) and (
                            self.__boxes[y].cget('text') == ''):
                        self.__boxes[y].configure(text=self.__computer, state='disabled', text_color_disabled='white')
                        break

                    elif (self.__boxes[y].cget('text') == self.__boxes[z].cget('text') == self.__player) and (
                            self.__boxes[x].cget('text') == ''):
                        self.__boxes[x].configure(text=self.__computer, state='disabled', text_color_disabled='white')
                        break

                    else:
                        continue

                else:
                    btn = random.choice(boxes_left)
                    btn.configure(text=self.__computer, state='disabled', text_color_disabled='white')

            else:
                self.__message_box('It\'s a draw!')

        self.__winner_check()

    def __empty_boxes(self):
        """
        Search for the boxes that are empty
        """
        boxes_left = []

        for box in self.__boxes:

            if box.cget('text') == '':
                boxes_left.append(box)

        return boxes_left

    def __message_box(self, text):
        """
        Message to appear in case of game over
        """
        restart_window = ctk.CTkToplevel(self, fg_color='#242424')

        restart_window.resizable(width=False, height=False)

        restart_window.title('New game')

        messagebox_label = ctk.CTkLabel(restart_window, text=text, font=ctk.CTkFont(size=25))

        restart_label = ctk.CTkLabel(restart_window, text='Do you want to play again?',
                                     font=ctk.CTkFont(size=15, weight='bold'), text_color='white')
        yes_btn = ctk.CTkButton(restart_window, text='Yes', width=80, font=ctk.CTkFont(size=20),
                                command=lambda: [restart_window.destroy(), self.__reset_boxes()])

        no_btn = ctk.CTkButton(restart_window, text='No', width=80, font=ctk.CTkFont(size=20),
                               command=restart_window.destroy)

        messagebox_label.grid(row=0, columnspan=4, pady=10)
        restart_label.grid(row=1, columnspan=4, padx=21, pady=(0, 4))
        yes_btn.grid(row=2, column=1)
        no_btn.grid(row=2, column=2)

        self.__toplevel_center_root(restart_window, width=240, height=150)

        restart_window.wm_transient(self)

    def __reset_boxes(self):
        """
        Reset the game
        """
        for box in self.__boxes:
            box.configure(text='', state='normal')
        self.__player = None
        self.__game_difficulty.configure(state='normal')

    def __on_enter(self, event):
        self.__new_game_btn.configure(text_color='grey')

    def __on_leave(self, event):
        self.__new_game_btn.configure(text_color='white')


if __name__ == '__main__':
    game = TicTacToe()
    game.mainloop()
