import customtkinter as ctk
from .secret_word import SecretWordFrame


class CategoryFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.ms = master

        self.set_category = ''

        self.words_category = ['Animals', 'House', 'Space', 'Ocean', 'Sports', 'Cities']

        for i in range(6):
            self.btn = ctk.CTkButton(master=self, text=self.words_category[i], width=40, font=ctk.CTkFont(size=15),
                                     cursor='hand2')
            self.btn.bind('<Button-1>', self.on_click)
            self.btn.grid(row=0, column=i, padx=5)

    def on_click(self, event):
        text = event.widget.master.cget('text')
        self.ms.score_frame.reset_score()
        self.set_category = text
        if self.ms.info_label.winfo_exists():
            self.ms.info_label.destroy()
            self.ms.image_label.destroy()
            self.ms.status_frame.grid(row=5, column=0, pady=10, sticky='nsew')
            self.ms.kb_frame.grid(row=6, column=0, padx=26, pady=20, sticky='nsew')
        self.refresh_sc_wd_frame()

    def refresh_sc_wd_frame(self):
        self.ms.sc_wd_frame.destroy()
        self.ms.sc_wd_frame = SecretWordFrame(master=self.ms, fg_color='#242424')
        self.ms.sc_wd_frame.grid(row=3, column=0, padx=self.pad_x(), pady=20, sticky='nsew')

    def pad_x(self):
        x = (458 - len(self.ms.sc_wd_frame.text) * 30) / 2
        return x
