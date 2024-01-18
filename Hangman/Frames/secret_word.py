import random
import customtkinter as ctk
from CTkMessagebox import CTkMessagebox

from Hangman.Frames.info import InfoFrame
from Hangman.Frames.keyboard import KeyboardFrame
from Hangman.Frames.status import StatusImageFrame


class SecretWordFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.ms = master

        self.text = self.set_text()

        self.box = list(range(len(self.text)))

        for i in range(len(self.text)):
            self.box[i] = ctk.CTkLabel(master=self, text='*', width=30, font=ctk.CTkFont(size=20, underline=True))
            self.box[i].grid(row=0, column=i)

    def get_list(self):

        if self.ms.category_frame.category == 'Animals':

            animal_list = ['lion', 'wolf', 'elephant', 'zebra', 'monkey', 'horse', 'donkey',
                           'lizard', 'hippopotamus', 'giraffe', 'crocodile', 'lion', 'wolf']
            return animal_list

        elif self.ms.category_frame.category == 'House':

            house_list = ['chair', 'table', 'plate', 'wardrobe', 'convenience', 'kitchen',
                          'bathroom', 'sofa', 'carpet', 'refrigerator', 'shower']
            return house_list

        elif self.ms.category_frame.category == 'Ocean':

            ocean_list = ['whale', 'walrus', 'penguin', 'dolphin', 'coral', 'shark',
                          'turtle', 'shrimp', 'tide', 'waves', 'seagulls']
            return ocean_list

        elif self.ms.category_frame.category == 'Space':

            space_list = ['pluto', 'mars', 'jupiter', 'neptune', 'saturn', 'venus',
                          'milkyway', 'galaxy', 'stars', 'astronaut', 'satellite']
            return space_list

        elif self.ms.category_frame.category == 'Sports':

            sport_list = ['football', 'basketball', 'curling', 'swimming', 'handball', 'tennis',
                          'gymnastics', 'fencing', 'rugby', 'cycling', 'snooker']
            return sport_list

        elif self.ms.category_frame.category == 'Cities':

            city_list = ['barcelona', 'berlin', 'washington', 'amsterdam', 'paris', 'brussels',
                         'moscow', 'tokyo', 'beijing', 'stockholm', 'taiwan']
            return city_list

        else:

            return ['default']

    def set_text(self):
        random_list = self.get_list()

        if not self.ms.category_frame.ls:
            result = random.choice(random_list).upper()
            return result

        else:
            left_ls = list(set(random_list) - set(self.ms.category_frame.ls))
            if len(left_ls) != 0:
                result = random.choice(left_ls).upper()
                return result

    def restart_game(self):

        message = CTkMessagebox(master=self.ms, title='Restart', icon='question',
                                message=f'You finished the Game! '
                                        f'Restart the Game?', option_1='Yes', option_2='No')
        response = message.get()

        if response == 'No':

            self.ms.destroy()

        else:
            self.ms.category_frame.category = 'Animals'
            self.ms.category_frame.ls = []
            self.ms.score_frame.reset_score()
            return self.ms.category_frame.refresh_sc_wd_frame()

    def next_category(self):

        message = CTkMessagebox(master=self.ms, title='Continue', icon='question',
                                message=f'You finished the {self.ms.category_frame.category} category! '
                                        f'Continue with the next category?', option_1='Yes', option_2='No')
        response = message.get()

        if response == 'No':

            self.ms.destroy()

        else:

            self.ms.category_frame.get_next_category()
            random_list = self.get_list()
            self.ms.category_frame.ls = []
            result = random.choice(random_list).upper()
            return result
