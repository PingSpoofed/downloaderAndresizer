from pytube import YouTube
import os
import requests
from io import BytesIO
from PIL import Image
import datetime

class YouTubeDownloader:
    @staticmethod
    def download_video(url, download_path='C:/users/test/Desktop/Videos'):
        yt = YouTube(url)

        # Display information about the video
        print("Title: ", yt.title)
        print("Number of views: ", yt.views)
        print("Length of video: ", yt.length, "seconds")
        print("Ratings: ", yt.rating)

        # Select the first stream with only audio
        ys = yt.streams.filter(only_audio=True).order_by('abr').desc().first()
        print("Downloading video: ", yt.title)

        # Download the video to the specified path
        ys.download(output_path=download_path, filename=f"{yt.title}.mp3")

        print("Done downloading video: ", yt.title)

    @staticmethod
    def resize_image(input_path, output_folder="C:/Users/test/desktop/Images", new_size=(1000, 1000)):
        # Extract the extension from the input file
        _, ext = os.path.splitext(input_path)
        ext = ext.lower()

        # Check if the extension is valid and supported
        if ext not in ['.jpg', '.jpeg', '.png', '.bmp', '.gif']:
            raise ValueError("Unsupported file extension.")

        # Generate a unique filename with the current date and time
        timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        output_name = f"resized-{timestamp}{ext}"
        output_path = os.path.join(output_folder, output_name)

        with Image.open(input_path) as image:
            # Resize the image using LANCZOS (formerly ANTIALIAS)
            resized_image = image.resize(new_size, Image.Resampling.LANCZOS)

            # Save the resized image
            resized_image.save(output_path)
            print(f"Image saved as {output_path}")