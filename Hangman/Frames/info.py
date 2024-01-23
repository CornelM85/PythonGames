import customtkinter as ctk
from PIL import Image


class InfoFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.image = ctk.CTkImage(Image.open('Images/click.png'), size=(60, 100))
        self.image_label = ctk.CTkLabel(self, text='', image=self.image)
        self.image_label.grid(row=0, column=0, pady=20, sticky='nsew')

        self.info_label = ctk.CTkLabel(self, text='Choose a Category \n& \nStart the Game  ', width=458,
                                       font=ctk.CTkFont(size=20, slant='italic'), text_color='white')
        self.info_label.grid(row=1, column=0, pady=15, sticky='nsew')
