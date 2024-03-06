import customtkinter as ctk

from utility_functions import place_window_in_center

from Frames.category import CategoryFrame
from Frames.keyboard import KeyboardFrame
from Frames.score import Score
from Frames.secret_word import SecretWordFrame
from Frames.status import StatusImageFrame
from Frames.info import InfoFrame
from Frames.top_score import TopScore


class HangMan(ctk.CTk):

    def __init__(self):
        super().__init__()

        ctk.set_appearance_mode('dark')

        self.resizable(width=False, height=False)

        self.title('HangMan')

        self.top_score_frame = TopScore(master=self, fg_color='#242424')
        self.top_score_frame.grid(row=0, column=0, pady=5, sticky='nsew')

        self.__title_label = ctk.CTkLabel(self, text='HangMan', width=458,
                                          font=ctk.CTkFont(size=30, weight='bold'),
                                          text_color='white')
        self.__title_label.grid(row=1, pady=(0, 20), sticky='nsew')

        place_window_in_center(master=self, height=598, width=458)

        self.score_frame = Score(master=self, fg_color='#242424')
        self.score_frame.grid(row=2, column=0, padx=27, pady=15, sticky='e')

        self.category_frame = CategoryFrame(master=self, fg_color='#242424')
        self.category_frame.grid(row=3, column=0, padx=15, pady=15, sticky='nsew')

        self.info_frame = InfoFrame(master=self, fg_color='#242424')
        self.info_frame.grid(row=5, column=0, sticky='nsew')

        self.status_frame = StatusImageFrame(master=self, fg_color='#242424')

        self.sc_wd_frame = SecretWordFrame(master=self, fg_color='#242424')

        self.kb_frame = KeyboardFrame(master=self, fg_color='#242424')

        self.protocol('WM_DELETE_WINDOW', self.close)

    def close(self):
        """
        Before closing the application add the name and score to the json file
        """
        self.kb_frame.add_player_score_to_file()
        self.destroy()


if __name__ == '__main__':
    game = HangMan()
    game.mainloop()
