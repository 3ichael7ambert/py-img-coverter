import os
import tkinter as tk
from tkinter import filedialog

def rename_files(input_folder, output_folder, file_extension):
    try:
        files = os.listdir(input_folder)
        files = [f for f in files if f.endswith(file_extension)]

        if not files:
            status_label.config(text="No files found in input folder!")
            return

        for i, file in enumerate(files):
            old_path = os.path.join(input_folder, file)
            new_path = os.path.join(output_folder, f"img{i+1:03d}.{file_extension}")
            os.rename(old_path, new_path)
        
        status_label.config(text=f"Renaming completed! {len(files)} files renamed.")
    except Exception as e:
        status_label.config(text=f"An error occurred: {str(e)}")


def select_input_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        input_folder_entry.delete(0, tk.END)
        input_folder_entry.insert(0, folder_path)

def select_output_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        output_folder_entry.delete(0, tk.END)
        output_folder_entry.insert(0, folder_path)

def start_rename():
    input_folder = input_folder_entry.get()
    output_folder = output_folder_entry.get()
    file_extension = file_type_var.get()

    if not os.path.isdir(input_folder):
        status_label.config(text="Invalid input folder path!")
        return
    if not os.path.isdir(output_folder):
        status_label.config(text="Invalid output folder path!")
        return

    rename_files(input_folder, output_folder, file_extension)

app = tk.Tk()
app.title("Photo Renamer")

file_type_var = tk.StringVar(app)
file_type_var.set(".png")

input_folder_label = tk.Label(app, text="Input Folder:")
input_folder_label.grid(row=0, column=0, sticky="e")

input_folder_entry = tk.Entry(app, width=50)
input_folder_entry.grid(row=0, column=1, padx=5, pady=5)

input_folder_button = tk.Button(app, text="Browse", command=select_input_folder)
input_folder_button.grid(row=0, column=2, padx=5, pady=5)

output_folder_label = tk.Label(app, text="Output Folder:")
output_folder_label.grid(row=1, column=0, sticky="e")

output_folder_entry = tk.Entry(app, width=50)
output_folder_entry.grid(row=1, column=1, padx=5, pady=5)

output_folder_button = tk.Button(app, text="Browse", command=select_output_folder)
output_folder_button.grid(row=1, column=2, padx=5, pady=5)

file_type_label = tk.Label(app, text="File Type:")
file_type_label.grid(row=2, column=0, sticky="e")

file_type_menu = tk.OptionMenu(app, file_type_var, ".png", ".jpg", ".gif")
file_type_menu.grid(row=2, column=1, padx=5, pady=5)

start_button = tk.Button(app, text="Start", command=start_rename)
start_button.grid(row=3, column=1, padx=5, pady=10)

status_label = tk.Label(app, text="")
status_label.grid(row=4, column=0, columnspan=3)

app.mainloop()
