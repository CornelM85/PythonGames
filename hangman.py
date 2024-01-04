import customtkinter as ctk
from CTkMessagebox import CTkMessagebox


class SecretWordFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.keyboard_text = 'alb'.upper()

        self.box = list(range(3))

        self.text = 'Ala'.upper()

        for i in range(len(self.text)):
            self.box[i] = ctk.CTkLabel(master=self, text='*', font=ctk.CTkFont(size=20, underline=True))
            self.box[i].grid(row=0, column=i)

        for i in range(len(self.keyboard_text)):
            self.btn = ctk.CTkButton(master=self, width=10, text=self.keyboard_text[i], font=ctk.CTkFont(size=10))
            self.btn.bind('<Button-1>', self.on_click)
            self.btn.grid(row=1, column=i)

    def on_click(self, event):
        # self.children.pop('[!ctkcanvas]')
        print(event.widget.master.cget('text'))
        # if str(event.widget).count('label') == 1:
        #     text = event.widget.cget('text')
        #     for i in range(len(self.text)):
        #         if self.text[i] == text:
        #             self.box[i].configure(text=text)


class HangMan(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.resizable(width=False, height=False)

        self.configure(fg_color='#242424')

        self.title('HangMan')
        self.__title_label = ctk.CTkLabel(self, text='HangMan',
                                          font=ctk.CTkFont(size=30, weight='bold'),
                                          text_color='white')

        self.__title_label.grid(padx=150, pady=(40, 20))

        self.__root_center_screen(window_height=598, window_width=458)

        self.myframe = SecretWordFrame(master=self)
        self.myframe.grid(row=5, column=0, padx=20, pady=20, sticky='nsew')

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
