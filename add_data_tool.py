import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import json

def get_lists(kind, filename="lists.json"):
    with open(filename, "r") as info:
        data = json.load(info)
    return data[kind]

def add_to_tag():
    selected_item = tags_combo.get()
    current_text = tags_entry_var.get()
    global updated_tags_list

    if current_text:
        if selected_item not in current_text:
            tags_entry_var.set(current_text + f", {selected_item}")
    else:
        tags_entry_var.set(selected_item)

    if selected_item not in tags_list:
        updated_tags_list = updated_tags_list + list(selected_item)

    tags.remove(selected_item)
    tags_combo['values'] = tags

def add_to_equipment():
    selected_item = equipment_combo.get()
    current_text = equipment_entry_var.get()
    global updated_equipment_list

    if current_text:
        if selected_item not in current_text:
            equipment_entry_var.set(current_text + f", {selected_item}")
    else:
        equipment_entry_var.set(selected_item)

    if selected_item not in tags_list:
        updated_equipment_list = updated_equipment_list + list(selected_item)

    equipment.remove(selected_item)
    equipment_combo['values'] = equipment


def update_lists(filename="lists.json"):

    with open(filename, "r") as info:
        data = json.load(info)

    data["tags"] = updated_tags_list
    data["equipment"] = updated_equipment_list

    with open(filename, "w") as f:
        json.dump(data, f, indent=1)

def add_exercise(filename="data.json"):
    with open(filename, "r") as info:
        data = json.load(info)
    
    exercise_id = str(len(data)+1)
    
    new_exercise_data = {
        "name": NameVar.get(),
        "difficulty": DifficultyVar.get(),
        "tag": tags_entry_var.get(),
        "description": Description_text.get("1.0", "end-1c"),
        "equipment": equipment_entry_var.get()
    }

    data[exercise_id] = new_exercise_data

    # Write the updated JSON data to a file (optional)
    with open("data.json", "w") as json_file:
        json.dump(data, json_file, indent=1)

tags_list = get_lists("tags")
equipment_list = get_lists("equipment")

updated_tags_list = tags_list
updated_equipment_list = equipment_list

window = Tk()
window.title("Add Data")
window.resizable(False, False)
window.geometry("400x500")

frame = Frame(window)
frame.pack(fill=X)

tags_entry_var = StringVar()
equipment_entry_var = StringVar()

NameVar = StringVar()
DifficultyVar = IntVar()

basic_info_frame = LabelFrame(frame, text="Basic Info")
basic_info_frame.grid(row= 0, column=0, padx=20, pady=10, sticky="ew")

name_label = Label(basic_info_frame, text=f"Name: ")
name_label.grid(row=1, column=0, sticky=NW)
name_entry = Entry(basic_info_frame, width=40, textvariable=NameVar)
name_entry.grid(row=1, column=1, padx=10, sticky=NW)

difficulty_label = Label(basic_info_frame, text=f"Difficulty: ")
difficulty_label.grid(row=2, column=0)
difficulty_slider = Scale(basic_info_frame, from_=1, to=5, orient=HORIZONTAL, length=240, variable=DifficultyVar)
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

tags = tags_list
tags_combo = ttk.Combobox(list_info_frame, values=tags)
tags_combo.grid(row=1, column=1, padx=10,sticky=NW)

equipment_label = Label(list_info_frame, text=f"Equipment: ")
equipment_label.grid(row=3, column=0)
equipment_entry = tk.Entry(list_info_frame, textvariable=equipment_entry_var, width=30)
equipment_entry.grid(row=3, column=1, padx=10,sticky=NW)

add_to_equipment_button = tk.Button(list_info_frame, text="Tilføj", command=add_to_equipment)
add_to_equipment_button.grid(row=4, column=0, padx=10,sticky=NW)

equipment = equipment_list
equipment_combo = ttk.Combobox(list_info_frame, values=equipment)
equipment_combo.grid(row=4, column=1, padx=10,sticky=NW)

add_exercise_button = Button(frame, text="Tilføj øvelse", command=add_exercise)
add_exercise_button.grid(row=3, column=0)


window.mainloop()