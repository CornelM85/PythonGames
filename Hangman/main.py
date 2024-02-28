import customtkinter as ctk

from Frames.category import CategoryFrame
from Frames.keyboard import KeyboardFrame
from Frames.score import Score
from Frames.secret_word import SecretWordFrame
from Frames.status import StatusImageFrame
from Frames.info import InfoFrame
from Frames.top_score import TopScore
import ctypes


class HangMan(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.scale_factor = ctypes.windll.shcore.GetScaleFactorForDevice(0) / 100

        ctk.set_appearance_mode('dark')

        self.resizable(width=False, height=False)

        self.title('HangMan')

        self.top_score_frame = TopScore(master=self, fg_color='#242424')
        self.top_score_frame.grid(row=0, pady=5, sticky='nsew')

        self.__title_label = ctk.CTkLabel(self, text='HangMan', width=458,
                                          font=ctk.CTkFont(size=30, weight='bold'),
                                          text_color='white')
        self.__title_label.grid(row=1, pady=(0, 20), sticky='nsew')

        self.__root_center_screen(window_height=598, window_width=458)

        self.score_frame = Score(master=self, fg_color='#242424')
        self.score_frame.grid(row=2, column=0, padx=27, pady=15, sticky='e')

        self.category_frame = CategoryFrame(master=self, fg_color='#242424')
        self.category_frame.grid(row=3, column=0, padx=15, pady=15, sticky='nsew')

        self.info_frame = InfoFrame(master=self, fg_color='#242424')
        self.info_frame.grid(row=5, column=0, sticky='nsew')

        self.status_frame = StatusImageFrame(master=self, fg_color='#242424')

        self.sc_wd_frame = SecretWordFrame(master=self, fg_color='#242424')

        self.kb_frame = KeyboardFrame(master=self, fg_color='#242424')

    def __root_center_screen(self, window_width: int, window_height: int):
        """
        Center the Application in the middle of the screen
        """
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        x_coordinate = int((screen_width - window_width) * self.scale_factor / 2)
        y_coordinate = int((screen_height - window_height) / 2)

        self.geometry('{}x{}+{}+{}'.format(window_width, window_height, x_coordinate, y_coordinate))


if __name__ == '__main__':
    game = HangMan()
    game.mainloop()
