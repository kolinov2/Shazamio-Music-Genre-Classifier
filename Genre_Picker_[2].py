import os
import asyncio
import tkinter as tk
from tkinter import ttk
from shazamio import Shazam

def shazam(folder_path, selected_genre):
    async def main():
        try:
            shazam_instance = Shazam()
            genre_folder = 'genre_folder'
            if not os.path.exists('genre_folder'):
                os.makedirs('genre_folder')
            for filename in os.listdir(folder_path):
                if filename.endswith('.mp3'):
                    file_path = os.path.join(folder_path, filename)
                    out = await shazam_instance.recognize(file_path)
                    if 'track' in out:
                        track_info = out['track']
                        genre = track_info.get('genres', {}).get('primary', 'Unknown')
                        print(f"Plik: {filename}, Gatunek: {genre}")
                        if genre == selected_genre:
                            destination_folder = genre_folder
                            destination_path = os.path.join(destination_folder, filename)
                            os.rename(file_path, destination_path)
                            print(f"Przeniesiono plik {filename} do folderu {destination_folder}")
                        else:
                            print(f"Plik {filename} nie jest gatunku {selected_genre}, zostaje pominięty.")
                    else:
                        print(f"Nie udało się rozpoznać utworu dla pliku {filename}.")
        except Exception as e:
            print("Wystąpił błąd:", e)

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

def start_shazam():
    selected_genre = genre_combobox.get()
    folder_path = 'filtred'  # Ścieżka do folderu, możesz zmienić według potrzeb
    shazam(folder_path, selected_genre)

# Tworzenie interfejsu użytkownika
root = tk.Tk()
root.title("Shazam")
root.geometry("300x150")

# Etykieta wyboru gatunku
genre_label = ttk.Label(root, text="Wybierz gatunek muzyczny:")
genre_label.pack(pady=5)

# Lista rozwijana z gatunkami muzycznymi
genres = ['Hip-Hop/Rap', 'Hip-Hop', 'Pop', 'Metal', 'Electronic', 'Urbano latino', 'Rock', 'Alternative', 'Folk', 'Hard Rock', 'R&B', 'J-Pop']
genre_combobox = ttk.Combobox(root, values=genres)
genre_combobox.pack(pady=5)
genre_combobox.set(genres[0])  # Ustawienie domyślnej wartości

# Przycisk rozpoczęcia procesu Shazam
start_button = ttk.Button(root, text="Start", command=start_shazam)
start_button.pack(pady=5)

root.mainloop()
