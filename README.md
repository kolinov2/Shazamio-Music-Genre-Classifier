# Shazam Music Genre Classifier
[![python](https://img.shields.io/badge/Python-3.9-3776AB.svg?style=flat&logo=python&logoColor=white)](https://www.python.org) 
## Description

This project is a simple GUI application that utilizes the Shazam API to classify music files into different genres. Users can select a music genre from a dropdown list, and the application will analyze the music files in a specified folder to determine their genre. Files matching the selected genre will be moved to a separate folder.

## Features

- User-friendly GUI interface
- Selection of music genre from a dropdown list
- Utilizes the Shazam API for music classification
- Automatically moves files of the selected genre to a destination folder

## How to Use

1. Clone the repository to your local machine.
2. Install the required dependencies 
3. Run the script `Converter_[1].py`.
4. After that run the script `Genre_Picker_[2].py`.
5. Select a music genre from the dropdown list.
6. Click the "Start" button to initiate the classification process.
7. Run `Final_[3].py`
8. *Optional* run `Cleaner_[Optional].py` to clean your mess :)

## Requirements

- Python 3.x
- `shazamio` library (`pip install shazamio`)
- `tkinter` library (usually included in Python standard library)
- `moviepy` library (only if converting MP4 to MP3)

## Folder Structure

- `non-filtred`: Folder containing the original music files.
- `filtred`: Destination folder for files classified as the selected genre.
- `genre_folder`: Temporary folder used during the classification process.
- `rak`: Final folder

## Photos
![obraz](https://github.com/kolinov2/Shazamio-Music-Genre-Classifier-From-MP4/assets/94188817/2ef6d9d8-77f4-46d1-bb03-f369e133e579)
![obraz](https://github.com/kolinov2/Shazamio-Music-Genre-Classifier-From-MP4/assets/94188817/71fa1def-51fb-44c2-90bb-4c65c8a4095b)

## Author

[kolino_v](https://github.com/kolinov2)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
