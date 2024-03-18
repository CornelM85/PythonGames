import customtkinter as ctk
from CTkMessagebox import CTkMessagebox


class BoxesFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.ms = master

        self.player_s_choice = None

        for i in range(3):
            for j in range(3):
                button = ctk.CTkButton(self, text='', corner_radius=0, height=150, width=150,
                                       font=ctk.CTkFont(size=100))
                button.grid(row=i, column=j, padx=1, pady=1)
                button.bind('<Button-1>', self.__on_click)

    def __on_click(self, event):
        # char = event.widget.master.cget('text')
        if self.player_s_choice is None:
            self.player_s_choice = self.__player_choose()

        event.widget.master.configure(text=self.player_s_choice)

    def __player_choose(self):
        message = CTkMessagebox(master=self.ms, title='Player\'s choice', icon='question',
                                message='Choose your weapon:', height=100,
                                width=200, option_1='X', option_2='O', cancel_button='X')

        choice = message.get()

        return choice
