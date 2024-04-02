import os
from moviepy.editor import *

def convert_mp4_to_mp3(input_folder, output_folder):
    # Tworzenie folderu wyjściowego, jeśli nie istnieje
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Przeszukiwanie folderu wejściowego i jego podfolderów
    for root, dirs, files in os.walk(input_folder):
        for file in files:
            if file.endswith(".mp4"):
                input_path = os.path.join(root, file)
                output_path = os.path.join(output_folder, os.path.splitext(file)[0] + ".mp3")

                # Konwersja pliku MP4 do MP3
                video = VideoFileClip(input_path)
                audio = video.audio
                # Sprawdzamy czy istnieje ścieżka dźwiękowa
                if audio is not None:
                    audio.write_audiofile(output_path)
                    print(f"Skonwertowano: {input_path} -> {output_path}")
                else:
                    print(f"Plik {input_path} nie zawiera ścieżki dźwiękowej. Pomijam konwersję.")

# Wskazanie folderu wejściowego i wyjściowego
input_folder = "non-filtred"
output_folder = "filtred"

# Wywołanie funkcji konwertującej
convert_mp4_to_mp3(input_folder, output_folder)
