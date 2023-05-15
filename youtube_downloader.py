import os
import argparse
import yt_dlp
import ssl
import textwrap
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
    # Define the help message
    help_message = textwrap.dedent('''

Usage:
======
	python youtube_downloader.py <url> -d=<type>

Examples:
=========
To download a video:
	python youtube_downloader.py "https://www.youtube.com/watch?v=5PS2p1AZzFY" -d=vide0

To download a playlist:
	python youtube_downloader.py "https://www.youtube.com/playlist?list=PLXmi76euGSyyq1nw21U1M4tTsM0Zysayk" -d=playlist

Have fun!
''')

    # Parse the URL and the download type from the command line arguments
    parser = argparse.ArgumentParser(description="Download a YouTube video or playlist.", formatter_class=argparse.RawDescriptionHelpFormatter, add_help=help_message, epilog=help_message)
    parser.add_argument("url", help="The URL of the YouTube video or playlist.")
    parser.add_argument("-d", "--download", metavar="type", help="Specify whether to download a video or playlist. Default is 'video'.", choices=["video", "playlist"], default="video")
    # parser.add_argument("-h", "--help", action="help", help=help_message)
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
