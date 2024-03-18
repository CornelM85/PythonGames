import customtkinter as ctk

from Frames.boxes import BoxesFrame
from Frames.menu import MenuFrame
from utility_functions import place_window_in_center


class TicTacToe(ctk.CTk):
    def __init__(self):
        super().__init__()

        ctk.set_appearance_mode('dark')

        self.resizable(width=False, height=False)

        self.title('Tic-tac-toe')
        self.__title_label = ctk.CTkLabel(self, text='Tic tac toe', font=ctk.CTkFont(size=30, weight='bold'),
                                          text_color='white', width=458)
        self.__title_label.grid(row=0, column=0, pady=20)

        self.menu_frame = MenuFrame(master=self, fg_color='#242424')
        self.menu_frame.grid(row=1, column=0, pady=20, sticky='w')

        self.boxes_frame = BoxesFrame(master=self, fg_color='#242424')
        self.boxes_frame.grid(row=2, column=0, padx=2)

        place_window_in_center(self, height=602, width=459)


if __name__ == '__main__':
    game = TicTacToe()
    game.mainloop()