from pytube import YouTube
import tkinter as tk
from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def download_video(url, save_path):
    """Download the highest resolution MP4 video from YouTube."""
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(progressive=True, file_extension="mp4").get_highest_resolution()
        stream.download(output_path=save_path)
        print("Video downloaded successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

def select_save_directory():
    """Open a dialog to select the save directory."""
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")
    return folder

def main():
    """Main function to handle video download."""
    root = tk.Tk()
    root.withdraw()  # Hide the root window

    video_url = input("Please enter a YouTube URL: ")
    save_dir = select_save_directory()

    if save_dir:
        print("Starting download...")
        download_video(video_url, save_dir)
    else:
        print("Invalid save location.")

if __name__ == "__main__":
    main()


