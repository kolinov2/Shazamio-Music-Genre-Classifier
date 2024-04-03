import os
from moviepy.editor import *

def convert_mp4_to_mp3(input_folder, output_folder):
    # Creating the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Searching through the input folder and its subfolders
    for root, dirs, files in os.walk(input_folder):
        for file in files:
            if file.endswith(".mp4"):
                input_path = os.path.join(root, file)
                output_path = os.path.join(output_folder, os.path.splitext(file)[0] + ".mp3")

                # Converting MP4 file to MP3
                video = VideoFileClip(input_path)
                audio = video.audio
                # Checking if audio stream exists
                if audio is not None:
                    audio.write_audiofile(output_path)
                    print(f"Converted: {input_path} -> {output_path}")
                else:
                    print(f"The file {input_path} does not contain an audio stream. Skipping conversion.")

# Specifying the input and output folders
input_folder = "non-filtred"
output_folder = "filtred"

# Calling the conversion function
convert_mp4_to_mp3(input_folder, output_folder)
