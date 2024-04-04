import customtkinter as ctk

from .boxes import BoxesFrame


class MenuFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.ms = master

        self.__new_game_btn = ctk.CTkButton(self, text='New Game', height=10, font=ctk.CTkFont('times', size=20),
                                            fg_color='transparent', anchor='w', cursor='hand2', hover=False,
                                            command=self.restart_game)
        self.__new_game_btn.grid(row=0, column=0)
        self.__on_hover()

    def restart_game(self):
        """
        Restart the game function
        """
        self.ms.boxes_frame.destroy()
        self.ms.boxes_frame = BoxesFrame(master=self.ms, fg_color='#242424')
        self.ms.boxes_frame.grid(row=2, column=0, padx=2)

    def __on_enter(self, event):
        """
        Changing the text button color on hover_on
        """
        self.__new_game_btn.configure(text_color='grey')

    def __on_leave(self, event):
        """
        Changing the text button color on hover_out
        """
        self.__new_game_btn.configure(text_color='white')

    def __on_hover(self):
        """
        Combining the hover_on and hover_out functions in one
        """
        self.__new_game_btn.bind('<Enter>', self.__on_enter, add='+')
        self.__new_game_btn.bind('<Leave>', self.__on_leave, add='+')

