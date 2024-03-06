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
        """
        Switches the category and resets the score
        """
        text = event.widget.master.cget('text')
        self.ms.score_frame.reset_score()
        self.ls = []
        self.category = text

        if self.ms.info_frame.winfo_exists():

            self.ms.info_frame.destroy()
            self.ms.status_frame.grid(row=6, column=0, pady=10, sticky='nsew')
            self.ms.kb_frame.grid(row=7, column=0, padx=27, pady=15, sticky='nsew')
            self.ms.top_score_frame.edit_name_button.grid(row=0, column=2)
            self.ms.top_score_frame.set_player_name()

        self.refresh_sc_wd_frame()

    def refresh_sc_wd_frame(self):
        """
        Updates the status image and the secret word frame
        """
        self.ms.status_frame.update_image()

        if not self.ms.sc_wd_frame.winfo_exists():

            self.ms.sc_wd_frame.grid(row=4, column=0, padx=self.__pad_x(), pady=15, sticky='nsew')

        else:

            self.ms.sc_wd_frame.destroy()
            self.ms.sc_wd_frame = SecretWordFrame(master=self.ms, fg_color='#242424')
            self.ms.sc_wd_frame.grid(row=4, column=0, padx=self.__pad_x(), pady=15, sticky='nsew')

        self.__list_update()

    def __pad_x(self):
        """
        Centers the text from the secret word frame
        :return: int
        """
        x = (458 - len(self.ms.sc_wd_frame.text) * 30) / 2
        return x

    def __list_update(self):
        """
        Updates the list of words used in the secret word frame
        """
        self.ls.append(self.ms.sc_wd_frame.text.lower())

    def get_next_category(self):
        """
        Gets the next category list for play
        :return: str
        """
        index = self.words_category.index(self.category)
        self.words_category.pop(index)

        if self.words_category:

            self.category = self.words_category[0]
            return self.category


