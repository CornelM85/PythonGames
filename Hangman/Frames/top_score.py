import json
import customtkinter as ctk

from utility_functions import add_scorers_labels, sort_descending_scores, place_window_in_center


class TopScore(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.__window = None

        self.ms = master

        self.top_scorers_button = ctk.CTkButton(self, text='Top Scorers', font=ctk.CTkFont(size=12, underline=True),
                                                text_color='white', fg_color='#242424', cursor='hand2', anchor='w',
                                                hover_color='#242424', command=self.__on_click_top_scorers)
        self.top_scorers_button.grid(row=0, column=0, padx=(30, 0))

        self.player_label = ctk.CTkLabel(self, text='Guest', font=ctk.CTkFont(size=15), width=240,
                                         text_color='#3282F6', anchor='e')
        self.player_label.grid(row=0, column=1)

        self.edit_name_button = ctk.CTkButton(self, text='Edit', width=30, font=ctk.CTkFont(size=10, underline=True),
                                              anchor='w', text_color='white', cursor='hand2', fg_color='#242424',
                                              hover_color='#242424', command=self.__on_click_edit_name)

        self.__on_hover()

    def __on_enter(self, event):
        """
        Changes the displayed text color of the button on hover_in
        """
        buttons = [self.top_scorers_button, self.edit_name_button]
        if event.widget.master.cget('text') == 'Top Scorers':
            buttons[0].configure(text_color='#874B2D')
        else:
            buttons[1].configure(text_color='#874B2D')

    def __on_leave(self, event):
        """
        Changes the displayed text color of the button on hover_out
        """
        buttons = [self.top_scorers_button, self.edit_name_button]
        if event.widget.master.cget('text') == 'Top Scorers':
            buttons[0].configure(text_color='white')
        else:
            buttons[1].configure(text_color='white')

    def __on_hover(self):
        """
        Binds the buttons with the custom methods for button hover
        """
        buttons = [self.top_scorers_button, self.edit_name_button]
        for button in buttons:
            button.bind('<Enter>', self.__on_enter, add='+')
            button.bind('<Leave>', self.__on_leave, add='+')

    def __on_click_top_scorers(self):
        """
        Displays a window on top of the Application with Top Scorers results and names
        """
        if not self.__window:
            self.__window = ctk.CTkToplevel(self.ms, fg_color='#242424')

            self.__window.resizable(width=False, height=False)

            sort_descending_scores()

            with (open('high_scorers.json', 'r') as read_file):
                body = json.load(read_file)
                values = body.values()

                i = 1
                for dictionary in values:
                    for k, v in dictionary.items():
                        add_scorers_labels(master=self.__window, place_number=i, name=k, score=v)
                        i += 1

                if len(values) < 11:
                    k = ''
                    v = ''
                    for j in range(len(values)+1, 11):
                        add_scorers_labels(master=self.__window, place_number=j, name=k, score=v)

                ctk.CTkButton(self.__window, height=20, width=50, text='OK', font=ctk.CTkFont(size=10),
                              cursor='hand2', fg_color='#874B2D',
                              command=self.__window.destroy).grid(row=11, columnspan=5, padx=10, pady=5, sticky='w')

            place_window_in_center(master=self.ms, window_name=self.__window, width=400, height=320)

            self.__window.wm_transient(self.ms)

            self.__window = None

    def __on_click_edit_name(self):
        """
        Changes the name of the player
        """
        self.set_player_name()

    def set_player_name(self):
        """
        Displays an input dialog box for adding the name of the player
        """
        input_dialog = ctk.CTkInputDialog(title='Player Name', text='Enter a player name (Max 15 characters):')

        place_window_in_center(master=self.ms, window_name=input_dialog, width=300, height=150)

        name = input_dialog.get_input()

        if name is None or not name.isalnum():

            self.player_label.configure(text='Guest')

        else:

            if len(name) < 15:

                self.player_label.configure(text=name)

            else:

                self.set_player_name()
