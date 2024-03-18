import customtkinter as ctk


class MenuFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.__new_game_btn = ctk.CTkButton(self, text='New Game', height=10, font=ctk.CTkFont(size=15),
                                            fg_color='transparent', anchor='w')
        self.__new_game_btn.grid(row=0, column=0)

        self.__game_difficulty = ctk.CTkSegmentedButton(self, values=['Easy', 'Normal', 'God Mode'], fg_color='#242424',
                                                        selected_color='grey',
                                                        font=ctk.CTkFont(size=15), unselected_color='#242424',
                                                        selected_hover_color='grey',
                                                        unselected_hover_color='#242424')
        self.__game_difficulty.grid(row=0, column=2)