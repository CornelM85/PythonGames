import customtkinter as ctk

# dict = {0: {'a': 1}, 1: {'b': 3}, 2: {'c': 2}, 3: {'d': 4}}
#
# values_list = dict.values()
#
# unsorted_ls = []
#
# data = {}
#
# for dictionary in values_list:
#     for k, v in dictionary.items():
#         unsorted_ls.append(v)
#
# sorted_list = sorted(unsorted_ls, reverse=True)
# for i in range(len(values_list)):
#     for y in values_list:
#         for key in y.keys():
#             if y[key] == sorted_list[i]:
#                 data[i] = {key: sorted_list[i]}
#
# print(data)


def font_size(text):
    text = ctk.CTkFont(size=15)