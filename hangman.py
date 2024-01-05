import customtkinter as ctk
from CTkMessagebox import CTkMessagebox


class Score(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.score = 0
        self.attempt = ctk.StringVar(value='Try: 0')
        self.remaining_tries = ctk.StringVar(value='Remaining tries: 10')

        self.score_label = ctk.CTkLabel(self, text='Score: ' + str(self.score), font=ctk.CTkFont(size=15), height=10)
        self.score_label.grid(row=0, column=0, sticky='e')

        self.attempt_label = ctk.CTkLabel(self, textvariable=self.attempt, font=ctk.CTkFont(size=15), height=10)
        self.attempt_label.grid(row=1, column=0, sticky='e')

        self.rm_tr_label = ctk.CTkLabel(self, textvariable=self.remaining_tries, font=ctk.CTkFont(size=15), height=10)
        self.rm_tr_label.grid(row=2, column=0, sticky='e')

    def set_score(self):
        self.score += 10

    def set_attempt(self):
        result = int(self.attempt.get().removeprefix('Try: '))
        result += 1
        self.attempt.set('Try: ' + str(result))

    def set_remaining_tries(self):
        result = int(self.remaining_tries.get().removeprefix('Remaining tries: '))
        result -= 1
        self.remaining_tries.set('Remaining tries: ' + str(result))


class SecretWordFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.text = 'sadasdsdas'.upper()

        self.box = list(range(len(self.text)))

        for i in range(len(self.text)):
            self.box[i] = ctk.CTkLabel(master=self, text='*', width=30, font=ctk.CTkFont(size=20, underline=True))
            self.box[i].grid(row=0, column=i)


class KeyboardFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.frame = master.sc_wd_frame

        self.sc_frame = master.score_frame

        self.keyboard_text = 'abcdefghijklmnopqrstuvwxyz'.upper()

        for i in range(len(self.keyboard_text)):
            self.btn = ctk.CTkButton(master=self, width=31, text=self.keyboard_text[i], font=ctk.CTkFont(size=15))
            self.btn.bind('<Button-1>', self.on_click)
            if i <= 12:
                self.btn.grid(row=4, column=i)
            else:
                self.btn.grid(row=5, column=i - 13)

    def on_click(self, event):
        text = event.widget.master.cget('text')
        self.sc_frame.set_attempt()
        if text in self.frame.text:
            for i in range(len(self.frame.text)):
                if self.frame.text[i] == text:
                    self.frame.box[i].configure(text=text)

        else:
            self.sc_frame.set_remaining_tries()

        self.status()

    def status(self):
        count = 0
        for i in range(len(self.frame.text)):

            if self.frame.box[i].cget('text') != '*':
                count += 1

        if count == len(self.frame.text):
            CTkMessagebox(master=self.master, message='Evrika!')


class HangMan(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.resizable(width=False, height=False)

        self.configure(fg_color='#242424')

        self.title('HangMan')

        self.grid_rowconfigure(index=1, minsize=10)

        self.__title_label = ctk.CTkLabel(self, text='HangMan',
                                          font=ctk.CTkFont(size=30, weight='bold'),
                                          text_color='white')

        self.__title_label.grid(padx=150, pady=(40, 20))

        self.__root_center_screen(window_height=598, window_width=458)

        self.score_frame = Score(master=self)
        self.score_frame.grid(row=4, column=0, padx=20, pady=20, sticky='e')

        self.sc_wd_frame = SecretWordFrame(master=self)
        self.sc_wd_frame.grid(row=5, column=0, padx=20, pady=20, sticky='nsew')

        self.kb_frame = KeyboardFrame(master=self)
        self.kb_frame.grid(row=10, column=0, padx=20, pady=20, sticky='nsew')

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
