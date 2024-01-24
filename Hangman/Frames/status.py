import customtkinter as ctk

from PIL import Image


class StatusImageFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.ms = master

        self.path = self.set_path()

        self.image = ctk.CTkImage(Image.open(self.path), size=(200, 150))

        self.status_image_label = ctk.CTkLabel(self, text='', image=self.image, width=458)
        self.status_image_label.grid(row=0, column=0)

        self.category_chosen = ctk.CTkLabel(master=self, text_color='#3282F6',
                                            text=f'Current category: {self.ms.category_frame.category.upper()}',
                                            font=ctk.CTkFont(size=15))
        self.category_chosen.grid(row=1, column=0, pady=10)

    def set_path(self):
        if self.ms.score_frame.get_remaining_tries() == 4:

            set_path = 'Images/img_1.png'

        elif self.ms.score_frame.get_remaining_tries() == 3:

            set_path = 'Images/img_2.png'

        elif self.ms.score_frame.get_remaining_tries() == 2:

            set_path = 'Images/img_3.png'

        elif self.ms.score_frame.get_remaining_tries() == 1:

            set_path = 'Images/img_4.png'

        elif self.ms.score_frame.get_remaining_tries() == 0:

            set_path = 'Images/img_5.png'

        else:

            set_path = 'Images/img_0.png'

        return set_path

    def update_image(self):
        if self.ms.status_frame.winfo_exists():

            self.ms.status_frame.destroy()
            self.ms.status_frame = StatusImageFrame(master=self.ms, fg_color='#242424')
            self.ms.status_frame.grid(row=5, column=0, pady=10, sticky='nsew')
