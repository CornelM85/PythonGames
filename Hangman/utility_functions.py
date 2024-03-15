import ctypes
import json
import os.path
import sys

import customtkinter as ctk


def add_scorers_labels(master, place_number, name, score):
    """
    Creates a line of labels in TopScore Frame class
    :param master: master object
    :param place_number: int
    :param name: string
    :param score: int
    """
    ctk.CTkLabel(master, width=70, text=f'{str(place_number)}.  Player name:',
                 font=ctk.CTkFont(size=15)).grid(row=place_number, column=0, padx=10)

    ctk.CTkLabel(master, width=150, text=name, text_color='#3282F6', anchor='w',
                 font=ctk.CTkFont(size=17)).grid(row=place_number, column=1)

    ctk.CTkLabel(master, width=50, text='Score:', anchor='e',
                 font=ctk.CTkFont(size=15)).grid(row=place_number, column=2, padx=10)

    ctk.CTkLabel(master, width=50, text=score, text_color='#3282F6', anchor='w',
                 font=ctk.CTkFont(size=17)).grid(row=place_number, column=3)


def create_file(file_name):
    """
     Creates a file name in the Application folder
    :param file_name: json type file name ex: (file_name.json)
    """
    if not os.path.exists(file_name):
        with open(file_name, 'x') as add_file:
            json.dump({}, add_file)


def sort_descending_scores():
    """
    Sort data from dictionary in descending order
    """
    data: dict = {}
    unsorted_ls: list = []
    json_file = resource_path('high_scorers.json')
    create_file(json_file)
    with open(json_file, 'r+') as file:
        file_data = json.load(file)
        values_list = file_data.values()

        for dictionary in values_list:
            for v in dictionary.values():
                unsorted_ls.append(v)

        sorted_list = sorted(unsorted_ls, reverse=True)

        for i in range(len(file_data)):
            for k, v in file_data.items():
                for key in v.keys():
                    if v[key] == sorted_list[i] and len(file_data) < 10:
                        data[k] = {key: sorted_list[i]}

        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=4)


def place_window_in_center(master, width, height, multiply=False, window_name=None):
    """
    Center the Application in the middle of the screen (window_name is None)
        Center the window in the middle of the Application window (window_name is not None)
    :param master: root
    :param width: the desired width of the window (int)
    :param height: the desired height of the window (int)
    :param window_name: default = None
    :param multiply: default = False
    """

    scale_factor = ctypes.windll.shcore.GetScaleFactorForDevice(0) / 100

    if multiply is False or scale_factor == 1:

        multiply_by = 1

    else:

        multiply_by = 2

    multiplication_scale = 2 * multiply_by

    if window_name is None:

        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()

        x_coordinate = int((screen_width - width) * scale_factor / 2)
        y_coordinate = int((screen_height - height) / 2)

        master.geometry('{}x{}+{}+{}'.format(width, height, x_coordinate, y_coordinate))

    else:

        root_height = master.winfo_height()
        root_width = master.winfo_width()

        root_x = master.winfo_x()
        root_y = master.winfo_y()

        x = int((root_width - width) / (scale_factor * multiplication_scale))
        y = int((root_height - height) / (2 * scale_factor))

        window_name.geometry('{}x{}+{}+{}'.format(width, height, x + root_x, y + root_y))


def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)
