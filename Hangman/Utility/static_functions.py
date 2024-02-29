import json
import os.path

import customtkinter as ctk


def add_scorers_labels(place_number, master, name, score):
    ctk.CTkLabel(master, width=70, text=f'{str(place_number)}.  Player name:',
                 font=ctk.CTkFont(size=15)).grid(row=place_number, column=0, padx=10)

    ctk.CTkLabel(master, width=150, text=name, text_color='#3282F6', anchor='w',
                 font=ctk.CTkFont(size=20)).grid(row=place_number, column=1)

    ctk.CTkLabel(master, width=50, text='Score:', anchor='e',
                 font=ctk.CTkFont(size=15)).grid(row=place_number, column=2)

    ctk.CTkLabel(master, width=50, text=score, text_color='#3282F6', anchor='e',
                 font=ctk.CTkFont(size=20)).grid(row=place_number, column=3)


def create_file(file_name):
    if not os.path.exists(file_name):
        with open(file_name, 'x') as add_file:
            json.dump({}, add_file)


def sort_descending_scores():
    data: dict = {}
    unsorted_ls: list = []
    json_file = 'high_scorers.json'
    create_file(json_file)
    with open(json_file, 'r+') as file:
        file_data = json.load(file)
        values_list = file_data.values()

        for dictionary in values_list:
            for k, v in dictionary.items():
                unsorted_ls.append(v)

        sorted_list = sorted(unsorted_ls, reverse=True)
        for i in range(10):
            for values in values_list:
                for key in values.keys():
                    if values[key] == sorted_list[i]:
                        data[i] = {key: sorted_list[i]}
        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=4)
