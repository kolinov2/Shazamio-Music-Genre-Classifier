import os
import shutil

def find_matching_files(folder_mp3, folder_mp4, folder_destination):
    # Funkcja pomocnicza do rekurencyjnego przeszukiwania katalogów
    def list_files(directory):
        files = []
        for root, _, filenames in os.walk(directory):
            for filename in filenames:
                files.append(os.path.join(root, filename))
        return files
    
    # Pobieramy listę plików mp3
    mp3_files = [os.path.splitext(os.path.basename(f))[0] for f in list_files(folder_mp3) if f.endswith('.mp3')]

    # Pobieramy listę plików mp4
    mp4_files = [f for f in list_files(folder_mp4) if f.endswith('.mp4')]

    # Porównujemy każdy plik mp3 z każdym plikiem mp4
    for mp3_name in mp3_files:
        for mp4_file in mp4_files:
            mp4_name = os.path.splitext(os.path.basename(mp4_file))[0]
            if mp3_name == mp4_name:
                # Tworzymy ścieżki plików
                source_path = mp4_file
                destination_path = os.path.join(folder_destination, os.path.basename(mp4_file))
                try:
                    # Przenosimy plik mp4 do folderu docelowego
                    shutil.move(source_path, destination_path)
                    print(f"Przeniesiono plik {mp4_file} do {folder_destination}")
                except FileNotFoundError:
                    print(f"Nie udało się znaleźć pliku {mp4_file}. Ignoruję ten plik.")
    shutil.rmtree("genre_folder")

if __name__ == "__main__":
    # Wskazujemy ścieżki do folderów
    folder_mp3 = "genre_folder"
    folder_mp4 = "non-filtred"
    folder_destination = "rak"

    # Sprawdzamy czy ścieżki istnieją
    if not os.path.isdir(folder_mp3) or not os.path.isdir(folder_mp4) or not os.path.isdir(folder_destination):
        print("Podane ścieżki do folderów są nieprawidłowe.")
    else:
        find_matching_files(folder_mp3, folder_mp4, folder_destination)
