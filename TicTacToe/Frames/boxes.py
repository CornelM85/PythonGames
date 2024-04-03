import random

import customtkinter as ctk
from CTkMessagebox import CTkMessagebox

from utility_functions import winner_list


class BoxesFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.ms = master

        self.player_s_choice = None

        self.computer_s_weapon = None

        self.boxes_list = []

        self.player_turns = ()

        for i in range(3):
            for j in range(3):
                self.box = ctk.CTkButton(self, text='', corner_radius=0, height=150, width=150,
                                         font=ctk.CTkFont('times', size=100), cursor='hand2')
                self.box.grid(row=i, column=j, padx=1, pady=1)
                self.box.bind('<Button-1>', self.__on_click, add='+')
                self.boxes_list.append(self.box)

    def __on_click(self, event):

        if self.player_s_choice is None:
            self.player_s_choice = self.__player_choose()
            self.set_computer_s_weapon()
            if self.random_player_start_game() == 0:
                self.player_turns = (9, 7, 5, 3, 1)
            else:
                self.computer_s_move()
                self.player_turns = (8, 6, 4, 2)
        elif len(self.empty_boxes_list()) in self.player_turns:
            event.widget.master.configure(text=self.player_s_choice, state='disabled', text_color_disabled='white')
            if self.status_check() != 'Winner':
                self.after(1000, lambda: self.computer_s_move())

    def __player_choose(self):
        message = CTkMessagebox(master=self.ms, title='Player\'s choice', message='Choose your weapon',
                                icon_size=(80, 80), icon='question', option_1='O', option_2='X',
                                font=('times', 20), justify='center')
        choice = message.get()

        return choice

    def set_computer_s_weapon(self):
        if self.player_s_choice == 'X':
            self.computer_s_weapon = 'O'
        else:
            self.computer_s_weapon = 'X'

    def computer_s_move(self):
        boxes_left = self.empty_boxes_list()
        if len(boxes_left) != 0:
            for x, y, z in winner_list():
                if (self.get_text(x) == self.get_text(y) != '') and (self.get_text(z) == ''):
                    self.boxes_list[z].configure(text=self.computer_s_weapon,
                                                 state='disabled', text_color_disabled='white')
                    break

                elif (self.get_text(x) == self.get_text(z) != '') and (self.get_text(y) == ''):
                    self.boxes_list[y].configure(text=self.computer_s_weapon,
                                                 state='disabled', text_color_disabled='white')
                    break

                elif (self.get_text(y) == self.get_text(z) != '') and (self.get_text(x) == ''):
                    self.boxes_list[x].configure(text=self.computer_s_weapon,
                                                 state='disabled', text_color_disabled='white')
                    break

            else:
                computer_box = random.choice(boxes_left)
                computer_box.configure(text=self.computer_s_weapon, state='disabled', text_color_disabled='white')

        self.is_a_draw()

        self.status_check()

    def empty_boxes_list(self):
        empty_boxes_list = []
        for box in self.boxes_list:
            if box.cget('text') == '':
                empty_boxes_list.append(box)
        return empty_boxes_list

    def status_check(self):
        for i in winner_list():
            if self.get_text(i[0]) == self.get_text(i[1]) == self.get_text(i[2]) == self.player_s_choice:
                for j in range(3):
                    self.set_text_color(i[j], 'green')
                self.__message('Congratulations! You win!')
                return 'Winner'
            elif self.get_text(i[0]) == self.get_text(i[1]) == self.get_text(i[2]) == self.computer_s_weapon:
                for j in range(3):
                    self.set_text_color(i[j], 'red')
                self.__message('You lose! Restart the game?', opt_1='Yes', opt_2='No')
                return 'Winner'

    def get_text(self, pos: int):
        return self.boxes_list[pos].cget('text')

    def set_text_color(self, pos, color):
        self.boxes_list[pos].configure(text_color_disabled=color)

    def __message(self, text, opt_1='Ok', opt_2=None):
        """
        :param text: str (message)
        :param opt_1: str ('Yes' or default 'Ok')
        :param opt_2 str ('No' or default None)
        """
        message = CTkMessagebox(master=self.ms, title='Results', message=text, icon_size=(80, 80),
                                option_1=opt_1, option_2=opt_2, font=('times', 20), justify='center')

        choice = message.get()

        if choice == 'Yes':
            self.ms.menu_frame.restart_game()
            self.empty_boxes_list()

    @staticmethod
    def random_player_start_game():
        start = [0, 1]
        x = random.choice(start)
        return x

    def is_a_draw(self):
        box_filled = 0
        for i in range(9):
            if self.get_text(i) != '':
                box_filled += 1

        if box_filled == 9:
            self.__message('It\'s a draw! Restart the game?', opt_1='Yes', opt_2='No')