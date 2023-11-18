# main.py
from ytdwn import YouTubeDownloader

# Definieer de YouTube video URL
video_url = "https://www.youtube.com/watch?v=X-BYDYoM_3w"

# Roep de download_video methode aan
YouTubeDownloader.download_video(video_url)

# Definieer het pad naar je input afbeelding
input_image_path = "C:/users/test/Desktop/87167.jpg"

# Roep de resize_image methode aan
YouTubeDownloader.resize_image(input_image_path)