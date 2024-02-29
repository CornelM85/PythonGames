import json
import customtkinter as ctk

from Utility.static_functions import add_scorers_labels, sort_descending_scores


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

        sort_descending_scores()

        with (open('high_scorers.json', 'r') as read_file):
            body = json.load(read_file)
            values = body.values()

            i = 1
            for dictionary in values:
                for k, v in dictionary.items():
                    add_scorers_labels(master=window, place_number=i, name=k, score=v)
                    i += 1

            if len(values) < 11:
                k = ''
                v = ''
                for j in range(len(values)+1, 11):
                    add_scorers_labels(master=window, place_number=j, name=k, score=v)

            ctk.CTkButton(window, height=20, width=50, text='OK', font=ctk.CTkFont(size=10), cursor='hand2',
                          fg_color='#874B2D', command=window.destroy).grid(row=11, columnspan=5, pady=5, sticky='e')

        self.__window_center_root(window, width=400, height=320)

        window.wm_transient(self.ms)

    def __window_center_root(self, window_name, width, height):
        """
        Center the window in the middle of the Application window
        """
        multiplication_scale: int

        root_height = self.ms.winfo_height()
        root_width = self.ms.winfo_width()

        root_x = self.ms.winfo_x()
        root_y = self.ms.winfo_y()

        if self.ms.scale_factor == 1:
            multiplication_scale = 2

        else:
            multiplication_scale = 4

        x = int((root_width - width) / (self.ms.scale_factor * multiplication_scale))
        y = int((root_height - height) / 2)

        window_name.geometry('{}x{}+{}+{}'.format(width, height, x + root_x, y + root_y))

