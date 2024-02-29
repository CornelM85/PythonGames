import json
import customtkinter as ctk
from CTkMessagebox import CTkMessagebox

from Utility.static_functions import create_file


class KeyboardFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.ms = master

        self.keyboard_text = 'abcdefghijklmnopqrstuvwxyz'.upper()

        for i in range(len(self.keyboard_text)):

            self.btn = ctk.CTkButton(master=self, width=31, text=self.keyboard_text[i], font=ctk.CTkFont(size=15),
                                     cursor='hand2', fg_color='#874B2D', hover_color='#242424')
            self.btn.bind('<Button-1>', self.__on_click)

            if i <= 12:

                self.btn.grid(row=0, column=i)

            else:

                self.btn.grid(row=1, column=i - 13)

    def __on_click(self, event):
        char = event.widget.master.cget('text')

        if char in self.ms.sc_wd_frame.text:

            for i in range(len(self.ms.sc_wd_frame.text)):

                if (self.ms.sc_wd_frame.text[i] == char and
                        self.ms.sc_wd_frame.box[i].cget('text') == '*'):

                    self.ms.sc_wd_frame.box[i].configure(text=char, text_color='#3282F6')
                    self.ms.score_frame.set_score()

        else:

            self.ms.score_frame.set_attempt()
            self.ms.score_frame.set_remaining_tries()
            self.ms.status_frame.update_image()

        self.status()

    def status(self):
        count = 0
        for i in range(len(self.ms.sc_wd_frame.text)):

            if self.ms.sc_wd_frame.box[i].cget('text') != '*':
                count += 1

        if (count == len(self.ms.sc_wd_frame.text) and
                self.ms.score_frame.get_remaining_tries() > 0):

            if (len(self.ms.category_frame.words_category) == 1
                    and len(self.ms.sc_wd_frame.get_list()) - len(self.ms.category_frame.ls) == 0):

                self.ms.sc_wd_frame.restart_game()

            elif (len(self.ms.category_frame.words_category) != 1
                    and len(self.ms.sc_wd_frame.get_list()) - len(self.ms.category_frame.ls) == 0):

                self.ms.sc_wd_frame.next_category()

            else:

                self.ms.category_frame.refresh_sc_wd_frame()

        elif self.ms.score_frame.get_remaining_tries() == 0:

            message = CTkMessagebox(master=self.ms, title='Game Lost', icon='info',
                                    message='You have no remaining tries!', height=100,
                                    width=200, option_1='Ok', cancel_button='Ok')
            response = message.get()

            if response == 'Ok':

                self.add_player_score_to_file()
                self.ms.score_frame.reset_score()
                self.ms.category_frame.ls = []
                self.status()
                self.ms.category_frame.refresh_sc_wd_frame()

    def add_player_score_to_file(self):
        json_file = 'high_scorers.json'
        name = self.ms.top_score_frame.player_label.cget('text')
        score = self.ms.score_frame.get_score()
        create_file(json_file)

        if name != 'Guest':

            with open(json_file, 'r+') as file:
                score_dict = json.load(file)
                score_dict[len(score_dict)] = {name: score}
                file.seek(0)
                file.truncate()
                json.dump(score_dict, file, indent=4)


