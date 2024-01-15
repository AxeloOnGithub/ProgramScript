import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import json
from subprocess import call



def add_to_tag():
    selected_item = tags_combo.get()
    current_text = tags_entry_var.get()

    if current_text:
        if selected_item not in current_text:
            tags_entry_var.set(current_text + f", {selected_item}")
    else:
        tags_entry_var.set(selected_item)

    tags.remove(selected_item)
    tags_combo['values'] = tags

window = Tk()
window.title("Add Data")
window.resizable(False, False)
window.geometry("400x500")

frame = Frame(window)
frame.pack(fill=X)

tags_entry_var = StringVar()

basic_info_frame = LabelFrame(frame, text="Basic Info")
basic_info_frame.grid(row= 0, column=0, padx=20, pady=10, sticky="ew")

name_label = Label(basic_info_frame, text=f"Name: ")
name_label.grid(row=1, column=0, sticky=NW)
name_entry = Entry(basic_info_frame, width=40)
name_entry.grid(row=1, column=1, padx=10, sticky=NW)

difficulty_label = Label(basic_info_frame, text=f"Difficulty: ")
difficulty_label.grid(row=2, column=0)
difficulty_slider = Scale(basic_info_frame, from_=1, to=5, orient=HORIZONTAL, length=240)
difficulty_slider.grid(row=2, column=1, padx=10,sticky=NW)

Description_label = Label(basic_info_frame, text=f"Description: ")
Description_label.grid(row=3, column=0)
Description_text = Text(basic_info_frame, height=4, width=30)
Description_text.grid(row=3, column=1, padx=10,sticky=NW)

list_info_frame = LabelFrame(frame, text="List Info")
list_info_frame.grid(row= 1, column=0, padx=20, pady=10, sticky="ew")

tags_label = Label(list_info_frame, text=f"Tags: ")
tags_label.grid(row=0, column=0)
tags_entry = tk.Entry(list_info_frame, textvariable=tags_entry_var, width=30)
tags_entry.grid(row=0, column=1, padx=10,sticky=NW)

add_to_tag_button = tk.Button(list_info_frame, text="Tilføj", command=add_to_tag)
add_to_tag_button.grid(row=1, column=0, padx=10,sticky=NW)

tags = ["Option 1", "Option 2", "Option 3", "Option 4"]
tags_combo = ttk.Combobox(list_info_frame, values=tags)
tags_combo.grid(row=1, column=1, padx=10,sticky=NW)



def add_exercise():
    return

window.mainloop()