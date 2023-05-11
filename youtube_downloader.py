import os
import argparse
import yt_dlp
import ssl
from urllib.parse import urlparse, parse_qs

ssl._create_default_https_context = ssl._create_unverified_context


def download_video(video_id):
    # Create a Downloads folder if it doesn't already exist
    if not os.path.exists("Downloads"):
        os.makedirs("Downloads")

    ydl_opts = {
        'outtmpl': 'Downloads/%(title)s.%(ext)s',
        'format': 'best',
        'nocheckcertificate': True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([f"https://www.youtube.com/watch?v={video_id}"])

    print("Video downloaded successfully!")


def download_playlist(playlist_id):
    # Create a Downloads folder if it doesn't already exist
    if not os.path.exists("Downloads"):
        os.makedirs("Downloads")

    ydl_opts = {
        'outtmpl': 'Downloads/%(title)s.%(ext)s',
        'format': 'best',
        'nocheckcertificate': True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([f"https://www.youtube.com/playlist?list={playlist_id}"])

    print("Playlist downloaded successfully!")


if __name__ == "__main__":
    # Parse the URL and the download type from the command line arguments
    parser = argparse.ArgumentParser(description="Download a YouTube video or playlist.")
    parser.add_argument("url", help="The URL of the YouTube video or playlist.")
    parser.add_argument("--download", help="Specify whether to download a video or playlist.", choices=["video", "playlist"], required=True)
    args = parser.parse_args()

    # Parse the video or playlist ID from the URL
    url_parts = urlparse(args.url)
    query_params = parse_qs(url_parts.query)
    video_id = query_params.get('v', [None])[0]
    playlist_id = query_params.get('list', [None])[0]

    if args.download == "video":
        if video_id is None:
            print("Error: Invalid URL. The specified URL is not a valid video URL.")
            exit()
        download_video(video_id)

    elif args.download == "playlist":
        if playlist_id is None:
            print("Error: Invalid URL. The specified URL is not a valid playlist URL.")
            exit()
        download_playlist(playlist_id)

    else:
        print("Error: Invalid download type. The specified download type must be either 'video' or 'playlist'.")
        exit()

