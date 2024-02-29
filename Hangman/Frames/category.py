import customtkinter as ctk
from .secret_word import SecretWordFrame


class CategoryFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.ms = master

        self.category = ''

        self.ls = []

        self.words_category = ['Animals', 'House', 'Ocean', 'Space', 'Sports', 'Cities']

        for i in range(6):
            self.btn = ctk.CTkButton(master=self, text=self.words_category[i], width=40,
                                     font=ctk.CTkFont(size=15, weight='bold'), cursor='hand2', hover_color='#242424',
                                     fg_color='#874B2D', height=10)
            self.btn.bind('<Button-1>', self.__on_click)
            self.btn.grid(row=0, column=i, padx=5)

    def __on_click(self, event):
        text = event.widget.master.cget('text')
        self.ms.score_frame.reset_score()
        self.ls = []
        self.category = text

        if self.ms.info_frame.winfo_exists():

            self.ms.info_frame.destroy()
            self.ms.status_frame.grid(row=6, column=0, pady=10, sticky='nsew')
            self.ms.kb_frame.grid(row=7, column=0, padx=27, pady=15, sticky='nsew')
            self.__set_player_name()

        self.refresh_sc_wd_frame()

    def refresh_sc_wd_frame(self):
        self.ms.status_frame.update_image()

        if not self.ms.sc_wd_frame.winfo_exists():

            self.ms.sc_wd_frame.grid(row=4, column=0, padx=self.__pad_x(), pady=15, sticky='nsew')

        else:

            self.ms.sc_wd_frame.destroy()
            self.ms.sc_wd_frame = SecretWordFrame(master=self.ms, fg_color='#242424')
            self.ms.sc_wd_frame.grid(row=4, column=0, padx=self.__pad_x(), pady=15, sticky='nsew')

        self.__list_update()

    def __pad_x(self):
        x = (458 - len(self.ms.sc_wd_frame.text) * 30) / 2
        return x

    def __list_update(self):
        self.ls.append(self.ms.sc_wd_frame.text.lower())

    def get_next_category(self):
        index = self.words_category.index(self.category)
        self.words_category.pop(index)

        if self.words_category:

            self.category = self.words_category[0]
            return self.category

    def __set_player_name(self):
        input_dialog = ctk.CTkInputDialog(title='Player Name', text='Enter name:')

        self.__window_center_root(input_dialog, 300, 150)

        name = input_dialog.get_input()

        if name is None or not name.isalnum():

            self.ms.top_score_frame.player_label.configure(text='Guest')

        else:

            self.ms.top_score_frame.player_label.configure(text=name)

    def __window_center_root(self, window_name, width: int, height: int):
        """
        Center the window in the middle of the Application window
        """
        multiplication_scale: int

        root_height = self.ms.winfo_height()
        root_width = self.ms.winfo_width()

        root_x = self.ms.winfo_x()
        root_y = self.ms.winfo_y()

        if self.ms.scale_factor == 1:

            multiplication_scale = 2

        else:

            multiplication_scale = 4

        x = int((root_width - width) / (self.ms.scale_factor * multiplication_scale))
        y = int((root_height - height) / 2)

        window_name.geometry('{}x{}+{}+{}'.format(width, height, x + root_x, y + root_y))
