import customtkinter as ctk
from CTkMessagebox import CTkMessagebox


class KeyboardFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.ms = master

        self.sc_frame = master.score_frame

        self.keyboard_text = 'abcdefghijklmnopqrstuvwxyz'.upper()

        for i in range(len(self.keyboard_text)):
            self.btn = ctk.CTkButton(master=self, width=31, text=self.keyboard_text[i], font=ctk.CTkFont(size=15),
                                     cursor='hand2')
            self.btn.bind('<Button-1>', self.on_click)
            if i <= 12:
                self.btn.grid(row=0, column=i)
            else:
                self.btn.grid(row=1, column=i - 13)

        self.status()

    def on_click(self, event):
        char = event.widget.master.cget('text')

        if char in self.ms.sc_wd_frame.text:
            for i in range(len(self.ms.sc_wd_frame.text)):
                if self.ms.sc_wd_frame.text[i] == char:
                    self.ms.sc_wd_frame.box[i].configure(text=char)
                    self.sc_frame.set_score()

        else:
            self.sc_frame.set_attempt()
            self.sc_frame.set_remaining_tries()
            self.ms.status_frame.update_image()

    def status(self):
        count = 0
        for i in range(len(self.ms.sc_wd_frame.text)):

            if self.ms.sc_wd_frame.box[i].cget('text') != '*':
                count += 1

        if count == len(self.ms.sc_wd_frame.text) and self.sc_frame.get_remaining_tries() > 0:
            self.ms.category_frame.list_update()
            self.ms.category_frame.refresh_sc_wd_frame()

        elif self.sc_frame.get_remaining_tries() == 0:
            message = CTkMessagebox(master=self.master, title='Exit or Continue', icon='question',
                                    message='You lose! Exit the application or try again?', option_1='Yes',
                                    option_2='No')
            response = message.get()
            if response == 'No':
                self.ms.destroy()
            else:
                self.sc_frame.reset_score()
                self.ms.category_frame.ls = []
                self.status()
                return self.ms.category_frame.refresh_sc_wd_frame()

        self.after(1000, lambda: self.status())

