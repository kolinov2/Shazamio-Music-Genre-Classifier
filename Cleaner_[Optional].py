import os
import shutil
import tkinter as tk
from tkinter import ttk, messagebox

def clean_folders(clean_rak):
    folders_to_clean = ['filtred']
    if clean_rak:
        folders_to_clean.append('rak')
    
    confirmation = messagebox.askyesno("Confirmation", "Are you sure you want to clear the contents of folders and optionally the rak folder?")
    
    if confirmation:
        for folder in folders_to_clean:
            clean_folder(folder)

def clean_folder(folder):
    for root, dirs, files in os.walk(folder):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
            except Exception as e:
                print(f"Error while deleting the file: {file_path}: {e}")
    
    for root, dirs, files in os.walk(folder, topdown=False):
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            try:
                if os.path.isdir(dir_path):
                    os.rmdir(dir_path)
            except Exception as e:
                print(f"Error while deleting the directory: {dir_path}: {e}")

def clean_folders_gui():
    def clean():
        clean_rak = rak_var.get()
        clean_folders(clean_rak)
    
    root = tk.Tk()
    root.title("Clean Folders")
    root.geometry("400x150")
    
    warning_label = ttk.Label(root, text="WARNING: This action will delete all files in the selcted folders!")
    warning_label.pack(pady=5)
    
    rak_var = tk.BooleanVar()
    rak_checkbox = ttk.Checkbutton(root, text="Also clean 'rak' folder", variable=rak_var)
    rak_checkbox.pack(pady=5)
    
    clean_button = ttk.Button(root, text="CLEAN", command=clean)
    clean_button.pack(pady=5)
    
    root.mainloop()

# Uruchomienie skryptu
clean_folders_gui()
