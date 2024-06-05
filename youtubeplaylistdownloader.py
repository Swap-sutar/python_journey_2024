import re
import os
from pytube import Playlist
from tqdm import tqdm

def download_playlist(playlist_url, download_dir):
    try:
        playlist = Playlist(playlist_url)
        playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
        YOUTUBE_STREAM_720P = 22
        for video in tqdm(playlist.videos, desc="Downloading", unit="video"):
            stream_720p = video.streams.get_by_itag(YOUTUBE_STREAM_720P)
            stream_720p.download(output_path=download_dir)

        print("Download completed successfully!")
    except Exception as e:
        print(f"Error: {e}")

def main():
    print("YouTube Playlist Downloader")

    playlist_url = input("Enter your URL: ")
    download_dir = input("Enter File path: ")

    if not os.path.exists(download_dir):
        print("Error: Invalid path. Please provide a valid directory.")
        return

    download_playlist(playlist_url, download_dir)

if __name__ == "__main__":
    main()
