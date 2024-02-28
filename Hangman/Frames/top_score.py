import os.path
import json
import customtkinter as ctk


class TopScore(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.ms = master

        self.player_label = ctk.CTkLabel(self, text='Guest', width=200, font=ctk.CTkFont(size=15),
                                         text_color='#3282F6', anchor='w')
        self.player_label.grid(row=0, column=0, padx=(30, 0))

        self.top_score_button = ctk.CTkButton(self, text='Top Scorers', font=ctk.CTkFont(size=12), text_color='white',
                                              width=200, fg_color='#242424', cursor='hand2', anchor='e',
                                              hover_color='#242424', command=self.__on_click)
        self.top_score_button.bind('<Enter>', self.on_enter, add='+')
        self.top_score_button.bind('<Leave>', self.on_leave, add='+')
        self.top_score_button.grid(row=0, column=1)

    def on_enter(self, event):
        self.top_score_button.configure(text_color='#874B2D')

    def on_leave(self, event):
        self.top_score_button.configure(text_color='white')

    def __on_click(self):
        window = ctk.CTkToplevel(self.ms, fg_color='#242424')

        window.resizable(width=False, height=False)

        self.sort_descending_scores()

        with open('high_scorers.json', 'r') as read_file:
            body = json.load(read_file)
            i = 1
            for name, score in body.items():
                ctk.CTkLabel(window, width=70, text=f'{str(i)}. Player name:',
                             font=ctk.CTkFont(size=15)).grid(row=0, column=0, padx=(10, 12), sticky='e')
                ctk.CTkLabel(window, text=name, text_color='#3282F6',
                             font=ctk.CTkFont(size=20)).grid(row=0, column=1)
                ctk.CTkLabel(window, width=60, text='Score:',
                             font=ctk.CTkFont(size=15)).grid(row=0, column=2, padx=(20, 0), sticky='e')
                ctk.CTkLabel(window, text=score, text_color='#3282F6',
                             font=ctk.CTkFont(size=20)).grid(row=0, column=3)

        self.__window_center_root(window, 280, 200)

        window.wm_transient(self.ms)

    @staticmethod
    def sort_descending_scores():
        score_dict: dict = {}
        json_file = 'high_scorers.json'
        if os.path.exists(json_file):
            with open(json_file, 'r') as read_file:
                x = json.load(read_file)
                y = x.values()
                values_list = sorted(y, reverse=True)
                keys_list = list(x.keys())

                for v in values_list:
                    for k in keys_list:
                        if x[k] == v:
                            score_dict[k] = v
            with open(json_file, 'w') as write_file:
                json.dump(score_dict, write_file, indent=4)
        else:
            with open(json_file, 'x') as create_file:
                json.dump(score_dict, create_file)

    def __window_center_root(self, window_name, width: int, height: int):
        """
        Center the window in the middle of the Application window
        """
        root_height = self.ms.winfo_height()
        root_width = self.ms.winfo_width()

        # window_height = 598, window_width = 458

        root_x = self.ms.winfo_x()
        root_y = self.ms.winfo_y()

        x = int((root_width - width) / (2 * self.ms.scale_factor))
        y = int((root_height - height) / 2)

        window_name.geometry('{}x{}+{}+{}'.format(width, height, x + root_x, y + root_y))