import random

import customtkinter as ctk
from CTkMessagebox import CTkMessagebox


class Score(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.score = ctk.StringVar(value='Score: 0')
        self.attempt = ctk.StringVar(value='Try: 0')
        self.remaining_tries = ctk.StringVar(value='Remaining tries: 5')

        self.score_label = ctk.CTkLabel(self, textvariable=self.score, font=ctk.CTkFont(size=15), height=10)
        self.score_label.grid(row=0, column=0, sticky='w')

        self.attempt_label = ctk.CTkLabel(self, textvariable=self.attempt, font=ctk.CTkFont(size=15), height=10)
        self.attempt_label.grid(row=1, column=0, sticky='w')

        self.rm_tr_label = ctk.CTkLabel(self, textvariable=self.remaining_tries, font=ctk.CTkFont(size=15), height=10)
        self.rm_tr_label.grid(row=2, column=0, sticky='w')

    def set_score(self):
        if self.get_remaining_tries() != 0:
            result = int(self.score.get().removeprefix('Score: '))
            result += 10
            self.score.set('Score: ' + str(result))

    def set_attempt(self):
        if self.get_remaining_tries() != 0:
            result = int(self.attempt.get().removeprefix('Try: '))
            result += 1
            self.attempt.set('Try: ' + str(result))

    def set_remaining_tries(self):
        if self.get_remaining_tries() != 0:
            result = int(self.remaining_tries.get().removeprefix('Remaining tries: '))
            result -= 1
            self.remaining_tries.set('Remaining tries: ' + str(result))

    def get_remaining_tries(self):
        result = int(self.remaining_tries.get().removeprefix('Remaining tries: '))
        return result

    def reset_score(self):
        self.score.set(value='Score: 0')
        self.attempt.set(value='Try: 0')
        self.remaining_tries.set(value='Remaining tries: 5')


class CategoryFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.ms = master

        self.set_category = ''

        self.words_category = ['Animal', 'House', 'Space', 'Ocean']

        for i in range(4):
            self.btn = ctk.CTkButton(master=self, text=self.words_category[i], width=40, font=ctk.CTkFont(size=15),
                                     cursor='hand2')
            self.btn.bind('<Button-1>', self.on_click)
            self.btn.grid(row=0, column=i, padx=5)

    def on_click(self, event):
        text = event.widget.master.cget('text')
        self.ms.score_frame.reset_score()
        self.set_category = text
        if text in ('Animal', 'House'):
            self.refresh_sc_wd_frame()

    def refresh_sc_wd_frame(self):
        self.ms.sc_wd_frame.destroy()
        self.ms.sc_wd_frame = SecretWordFrame(master=self.ms, fg_color='#242424')
        self.ms.sc_wd_frame.grid(row=3, column=0, padx=self.pad_x(), pady=20, sticky='nsew')

    def pad_x(self):
        x = (458 - len(self.ms.sc_wd_frame.text) * 30) / 2
        return x


class SecretWordFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.cat = master.category_frame

        self.text = self.set_text()

        self.box = list(range(len(self.text)))
        for i in range(len(self.text)):
            self.box[i] = ctk.CTkLabel(master=self, text='*', width=30, font=ctk.CTkFont(size=20, underline=True))
            self.box[i].grid(row=0, column=i)

    def set_text(self):
        result = self.animal_category()
        if self.cat.set_category == 'Animal':
            result = self.animal_category()

        elif self.cat.set_category == 'House':
            result = self.house_category()

        print(result)
        return result

    def animal_category(self):
        random_list = ['elephant', 'zebra', 'monkey', 'horse', 'shark',
                       'hippopotamus', 'giraffe', 'crocodile', 'lion']

        return random.choice(random_list).upper()

    def house_category(self):
        random_list = ['chair', 'table']

        return random.choice(random_list).upper()

    # def default(self):
    #     default = 'Pick a category'
    #     return default


class KeyboardFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.ms = master

        self.sc_frame = master.score_frame

        self.keyboard_text = 'abcdefghijklmnopqrstuvwxyz'.upper()

        for i in range(len(self.keyboard_text)):
            self.btn = ctk.CTkButton(master=self, width=31, text=self.keyboard_text[i], font=ctk.CTkFont(size=15),
                                     cursor='hand2')
            self.btn.bind('<Button-1>', self.on_click)
            if i <= 12:
                self.btn.grid(row=4, column=i)
            else:
                self.btn.grid(row=5, column=i - 13)

    def on_click(self, event):
        char = event.widget.master.cget('text')
        print(char)
        if char in self.ms.sc_wd_frame.text:
            for i in range(len(self.ms.sc_wd_frame.text)):
                if self.ms.sc_wd_frame.text[i] == char:
                    self.ms.sc_wd_frame.box[i].configure(text=char)
                    self.sc_frame.set_score()

        else:
            self.sc_frame.set_attempt()
            self.sc_frame.set_remaining_tries()

        self.status()

    def status(self):
        count = 0
        for i in range(len(self.ms.sc_wd_frame.text)):

            if self.ms.sc_wd_frame.box[i].cget('text') != '*':
                count += 1

        if count == len(self.ms.sc_wd_frame.text) and self.sc_frame.get_remaining_tries() > 0:
            CTkMessagebox(master=self.master, message='Evrika!')


        elif self.sc_frame.get_remaining_tries() == 0:
            CTkMessagebox(master=self.master, message='You lose!')


class HangMan(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.resizable(width=False, height=False)

        self.configure(fg_color='#242424')

        self.title('HangMan')

        # self.grid_rowconfigure(index=1, minsize=10)

        self.__title_label = ctk.CTkLabel(self, text='HangMan',
                                          font=ctk.CTkFont(size=30, weight='bold'),
                                          text_color='white')

        self.__title_label.grid(padx=150, pady=(40, 20))

        self.__root_center_screen(window_height=598, window_width=458)

        self.score_frame = Score(master=self, fg_color='#242424')
        self.score_frame.grid(row=1, column=0, padx=27, pady=20, sticky='e')

        self.category_frame = CategoryFrame(master=self, fg_color='#242424')
        self.category_frame.grid(row=2, column=0, padx=26, pady=20, sticky='nsew')

        self.sc_wd_frame = SecretWordFrame(master=self, fg_color='#242424')
        self.sc_wd_frame.grid(row=3, column=0, padx=self.category_frame.pad_x(), pady=20, sticky='nsew')

        self.kb_frame = KeyboardFrame(master=self, fg_color='#242424')
        self.kb_frame.grid(row=4, column=0, padx=26, pady=20, sticky='nsew')


    def __root_center_screen(self, window_width: int, window_height: int):
        """
        Center the Application in the middle of the screen
        """
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x_coordinate = int(screen_width / 2 - window_width / 2)
        y_coordinate = int(screen_height / 2 - window_height / 2)

        self.geometry('{}x{}+{}+{}'.format(window_width, window_height, x_coordinate, y_coordinate))


if __name__ == '__main__':
    game = HangMan()
    game.mainloop()
