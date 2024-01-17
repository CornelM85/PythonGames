import random
import customtkinter as ctk
from CTkMessagebox import CTkMessagebox


class SecretWordFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.ms = master

        self.text = self.set_text()

        self.box = list(range(len(self.text)))

        for i in range(len(self.text)):
            self.box[i] = ctk.CTkLabel(master=self, text='*', width=30, font=ctk.CTkFont(size=20, underline=True))
            self.box[i].grid(row=0, column=i)

    def set_text(self):

        if self.ms.category_frame.set_category == 'Animals':

            random_list = ['lion', 'wolf', 'elephant', 'zebra', 'monkey', 'horse', 'donkey',
                           'lizard', 'hippopotamus', 'giraffe', 'crocodile', 'lion', 'wolf']

        elif self.ms.category_frame.set_category == 'House':

            random_list = ['chair', 'table',  'plate', 'wardrobe', 'convenience', 'kitchen',
                           'bathroom', 'sofa', 'carpet', 'refrigerator', 'shower']

        elif self.ms.category_frame.set_category == 'Ocean':

            random_list = ['whale', 'walrus', 'penguin', 'dolphin', 'coral', 'shark',
                           'turtle', 'shrimp', 'tide', 'waves', 'seagulls']

        elif self.ms.category_frame.set_category == 'Space':

            random_list = ['pluto', 'mars', 'jupiter', 'neptune', 'saturn', 'venus',
                           'milkyway', 'galaxy', 'stars', 'astronaut', 'satellite']

        elif self.ms.category_frame.set_category == 'Sports':

            random_list = ['football', 'basketball', 'curling', 'swimming', 'handball', 'tennis',
                           'gymnastics', 'fencing', 'rugby', 'cycling', 'snooker']

        elif self.ms.category_frame.set_category == 'Cities':

            random_list = ['barcelona', 'berlin', 'washington', 'amsterdam', 'paris', 'brussels',
                           'moscow', 'tokyo', 'beijing', 'stockholm', 'taiwan']

        else:
            random_list = ['default']

        if not self.ms.category_frame.ls:

            result = random.choice(random_list).upper()
            return result

        else:

            left_ls = list(set(random_list) - set(self.ms.category_frame.ls))

            if len(left_ls) == 1:

                self.ms.category_frame.set_category = 'House'

            if len(left_ls) == 0:

                message = CTkMessagebox(master=self.ms, title='Continue', icon='question',
                                        message=f'You finished the {self.ms.category_frame.set_category} category! '
                                                f'Continue with the next category?', option_1='Yes', option_2='No')
                response = message.get()

                if response == 'No':

                    self.ms.destroy()

                else:
                    self.ms.category_frame.ls = []
                    result = random.choice(random_list).upper()
                    return result

            else:

                result = random.choice(left_ls).upper()
                return result
