import customtkinter as ctk
from PIL import Image

from Frames.category import CategoryFrame
from Frames.keyboard import KeyboardFrame
from Frames.score import Score
from Frames.secret_word import SecretWordFrame
from Frames.status import StatusImageFrame


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

        self.image = ctk.CTkImage(Image.open('Images/click.png'), size=(60, 100))
        self.image_label = ctk.CTkLabel(self, text='', image=self.image)
        self.image_label.grid(row=3, column=0, pady=20, sticky='nsew')

        self.info_label = ctk.CTkLabel(self, text='Choose a Category \n& \nStart the Game  ', width=458,
                                       font=ctk.CTkFont(size=20, slant='italic'), text_color='white',
                                       fg_color='#242424')
        self.info_label.grid(row=4, column=0, pady=20, sticky='nsew')

        self.status_frame = StatusImageFrame(master=self, fg_color='#242424')

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
