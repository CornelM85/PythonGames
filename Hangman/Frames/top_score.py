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

        with (open('high_scorers.json', 'r') as read_file):
            body = json.load(read_file)
            values = body.values()
            i = 1
            for dictionary in values:
                for k, v in dictionary.items():
                    self.add_scorers_labels(master=window, place_number=i, name=k, score=v)
                    i += 1
                    print(len(values))
            if len(values) < 11:
                k = ''
                v = ''
                for j in range(len(values)+1, 11):
                    self.add_scorers_labels(master=window, place_number=j, name=k, score=v)

            ctk.CTkButton(window, height=20, width=50, text='OK', font=ctk.CTkFont(size=10), cursor='hand2',
                          fg_color='#874B2D', command=window.destroy).grid(row=11, columnspan=5, pady=5, sticky='e')

        self.__window_center_root(window, width=400, height=320)

        window.wm_transient(self.ms)

    @staticmethod
    def sort_descending_scores():
        data: dict = {}
        unsorted_ls: list = []
        json_file = 'high_scorers.json'
        if os.path.exists(json_file):
            with open(json_file, 'r+') as file:
                file_data = json.load(file)
                values_list = file_data.values()

                for dictionary in values_list:
                    for k, v in dictionary.items():
                        unsorted_ls.append(v)

                sorted_list = sorted(unsorted_ls, reverse=True)
                for i in range(len(values_list)):
                    for values in values_list:
                        for key in values.keys():
                            if values[key] == sorted_list[i]:
                                data[i] = {key: sorted_list[i]}
                file.seek(0)
                file.truncate()
                json.dump(data, file, indent=4)
        else:
            with open(json_file, 'x') as create_file:
                json.dump(data, create_file)

    def __window_center_root(self, window_name, width, height):
        """
        Center the window in the middle of the Application window
        """

        root_height = self.ms.winfo_height()
        root_width = self.ms.winfo_width()

        root_x = self.ms.winfo_x()
        root_y = self.ms.winfo_y()

        x = int((root_width - width) / (2 * self.ms.scale_factor))
        y = int((root_height - height) / 2)

        window_name.geometry('{}x{}+{}+{}'.format(width, height, x + root_x, y + root_y))

    @staticmethod
    def add_scorers_labels(place_number, master, name, score):
        ctk.CTkLabel(master, width=70, text=f'{str(place_number)}.  Player name:',
                     font=ctk.CTkFont(size=15)).grid(row=place_number, column=0, padx=10)

        ctk.CTkLabel(master, width=150, text=name, text_color='#3282F6', anchor='w',
                     font=ctk.CTkFont(size=20)).grid(row=place_number, column=1)

        ctk.CTkLabel(master, width=50, text='Score:', anchor='e',
                     font=ctk.CTkFont(size=15)).grid(row=place_number, column=2)

        ctk.CTkLabel(master, width=50, text=score, text_color='#3282F6', anchor='e',
                     font=ctk.CTkFont(size=20)).grid(row=place_number, column=3)
