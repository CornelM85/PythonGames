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

        self.words_category = ['Animals', 'House', 'Space', 'Ocean', 'Sports', 'Cities']

        for i in range(6):
            self.btn = ctk.CTkButton(master=self, text=self.words_category[i], width=40, font=ctk.CTkFont(size=15),
                                     cursor='hand2')
            self.btn.bind('<Button-1>', self.on_click)
            self.btn.grid(row=0, column=i, padx=5)

    def on_click(self, event):
        text = event.widget.master.cget('text')
        self.ms.score_frame.reset_score()
        self.set_category = text
        if self.ms.info_label.winfo_exists():
            self.ms.info_label.destroy()
            self.ms.kb_frame.grid(row=5, column=0, padx=26, pady=20, sticky='nsew')
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

        if self.cat.set_category == 'Animals':
            random_list = ['elephant', 'zebra', 'monkey', 'horse', 'donkey', 'lizard',
                           'hippopotamus', 'giraffe', 'crocodile', 'lion', 'wolf']

        elif self.cat.set_category == 'House':
            random_list = ['chair', 'table', 'plate', 'wardrobe', 'convenience', 'kitchen',
                           'bathroom', 'sofa', 'carpet', 'refrigerator', 'shower']

        elif self.cat.set_category == 'Ocean':
            random_list = ['whale', 'walrus', 'penguin', 'dolphin', 'coral', 'shark',
                           'turtle', 'shrimp', 'tide', 'waves', 'seagulls']

        elif self.cat.set_category == 'Space':
            random_list = ['pluto', 'mars', 'jupiter', 'neptune', 'saturn', 'venus',
                           'milkyway', 'galaxy', 'stars', 'astronaut', 'satellite']

        elif self.cat.set_category == 'Sports':
            random_list = ['football', 'basketball', 'curling', 'swimming', 'handball', 'tennis',
                           'gymnastics', 'fencing', 'rugby', 'cycling', 'snooker']

        elif self.cat.set_category == 'Cities':
            random_list = ['barcelona', 'berlin', 'washington', 'amsterdam', 'paris', 'brussels',
                           'moscow', 'tokyo', 'beijing', 'stockholm', 'taiwan']

        else:
            random_list = [' ']

        result = random.choice(random_list).upper()

        return result


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

        self.status()

    def on_click(self, event):
        char = event.widget.master.cget('text')

        if char in self.ms.sc_wd_frame.text:
            for i in range(len(self.ms.sc_wd_frame.text)):
                if self.ms.sc_wd_frame.text[i] == char:
                    self.ms.sc_wd_frame.box[i].configure(text=char)
                    self.sc_frame.set_score()

        else:
            self.sc_frame.set_attempt()
            self.sc_frame.set_remaining_tries()

    def status(self):
        count = 0
        for i in range(len(self.ms.sc_wd_frame.text)):

            if self.ms.sc_wd_frame.box[i].cget('text') != '*':
                count += 1

        if count == len(self.ms.sc_wd_frame.text) and self.sc_frame.get_remaining_tries() > 0:
            self.ms.category_frame.refresh_sc_wd_frame()

        elif self.sc_frame.get_remaining_tries() == 0:
            message = CTkMessagebox(master=self.master, title='Exit or Continue', icon='question',
                                    message='You lose! Exit the application or try again?', option_1='Yes',
                                    option_2='No')
            response = message.get()
            if response == 'No':
                self.ms.destroy()
            else:
                self.sc_frame.reset_score()
                self.status()
                return self.ms.category_frame.refresh_sc_wd_frame()

        self.after(1000, lambda: self.status())


class HangMan(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.resizable(width=False, height=False)

        self.configure(fg_color='#242424')

        self.title('HangMan')

        self.__title_label = ctk.CTkLabel(self, text='HangMan', width=458,
                                          font=ctk.CTkFont(size=30, weight='bold'),
                                          text_color='white')

        self.__title_label.grid(pady=(40, 20), sticky='nsew')

        self.__root_center_screen(window_height=598, window_width=458)

        self.score_frame = Score(master=self, fg_color='#242424')
        self.score_frame.grid(row=1, column=0, padx=27, pady=20, sticky='e')

        self.category_frame = CategoryFrame(master=self, fg_color='#242424')
        self.category_frame.grid(row=2, column=0, padx=26, pady=20, sticky='nsew')

        self.info_label = ctk.CTkLabel(self, text='Choose a Category \n&  \nStart the Game  ', width=458,
                                       font=ctk.CTkFont(size=20, slant='italic'), text_color='white',
                                       fg_color='#242424')
        self.info_label.grid(row=3, column=0, pady=20, sticky='nsew')

        self.sc_wd_frame = SecretWordFrame(master=self, fg_color='#242424')

        self.kb_frame = KeyboardFrame(master=self, fg_color='#242424')

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
