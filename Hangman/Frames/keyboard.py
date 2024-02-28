import json
import customtkinter as ctk
from CTkMessagebox import CTkMessagebox


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

        self.status()

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

            message = CTkMessagebox(master=self.ms, title='Exit or Continue', icon='question',
                                    message='You have no remaining tries!\nStart a new game?',
                                    width=430, option_1='Yes', option_2='No', cancel_button='No')
            response = message.get()

            self.add_player_score_to_file()

            if response == 'No':

                self.ms.destroy()

            else:

                self.ms.score_frame.reset_score()
                self.ms.category_frame.ls = []
                self.status()
                return self.ms.category_frame.refresh_sc_wd_frame()

        self.after(1000, lambda: self.status())

    def add_player_score_to_file(self):
        json_file = 'high_scorers.json'
        name = self.ms.top_score_frame.player_label.cget('text')
        score = self.ms.score_frame.get_score()
        with open(json_file, 'r+') as write_file:
            score_dict = json.load(write_file)
            score_dict[name] = score
            write_file.seek(0)
            write_file.truncate()
            json.dump(score_dict, write_file, indent=4)


