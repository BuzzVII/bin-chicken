#  This program takes a mov file and converts it to a mp4 file with H.264 encoding.
#  The program uses the ffmpeg command line tool to do the conversion.

import os
import subprocess
import argparse


def convert_mov_to_mp4(mov_file, mp4_file):
    # Check if the mov file exists
    if not os.path.exists(mov_file):
        print("Error: mov file does not exist.")
        return

    # Check if the mp4 file already exists
    if os.path.exists(mp4_file):
        print("Error: mp4 file already exists.")
        return

    # Runthe ffmpeg command to convert the mov file to mp4
    ffmpeg_command = [
        "ffmpeg",
        "-i",
        mov_file,
        "-c:v",
        "libx264",
        "-crf",
        "23",
        "-c:a",
        "aac",
        "-strict",
        "experimental",
        "-b:a",
        "192k",
        mp4_file,
    ]
    ffmpeg_process = subprocess.Popen(ffmpeg_command)
    ffmpeg_process.wait()

    # Check if the mp4 file was created
    if not os.path.exists(mp4_file):
        print("Error: mp4 file was not created.")
    else:
        print("Conversion successful.")


def main():
    # Parse the command line arguments
    parser = argparse.ArgumentParser(
        description="Convert a mov file to a mp4 file with H.264 encoding."
    )
    parser.add_argument("mov_file", help="The input mov file.")
    parser.add_argument("mp4_file", help="The output mp4 file.")
    args = parser.parse_args()

    # Convert the mov file to mp4
    convert_mov_to_mp4(args.mov_file, args.mp4_file)


if __name__ == "__main__":
    main()
