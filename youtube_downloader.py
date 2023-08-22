import os
import argparse
import yt_dlp
import ssl
import textwrap
from urllib.parse import urlparse, parse_qs

ssl._create_default_https_context = ssl._create_unverified_context


def download_content(url, content_type):
    # Create a Downloads folder if it doesn't already exist
    if not os.path.exists("Downloads"):
        os.makedirs("Downloads")

    ydl_opts = {
        'outtmpl': 'Downloads/%(title)s.%(ext)s',
        'format': 'best',
        'nocheckcertificate': True
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print(f"{content_type.capitalize()} downloaded successfully!")
    except yt_dlp.DownloadError as e:
        print(f"Failed to download {content_type}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def parse_url(url, content_type):
    url_parts = urlparse(url)
    query_params = parse_qs(url_parts.query)
    id = query_params.get('v' if content_type == 'video' else 'list', [None])[0]

    # Usage:
    # ======
    # 	python youtube_downloader.py <url> -d=<type>
    #
    # Examples:
    # =========
    # To download a video:
    # 	python youtube_downloader.py "https://www.youtube.com/watch?v=5PS2p1AZzFY" -d=video
    #
    # To download a playlist:
    # 	python youtube_downloader.py "https://www.youtube.com/playlist?list=PLXmi76euGSyyq1nw21U1M4tTsM0Zysayk" -d=playlist
    #
    # Have fun!

    # Parse the URL and the download type from the command line arguments
    parser = argparse.ArgumentParser(description="Download a YouTube video or playlist.", formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("url", help="The URL of the YouTube video or playlist.")
    parser.add_argument("-d", "--download", metavar="type", help="Specify whether to download a video or playlist. Default is 'video'.", choices=["video", "playlist"], default="video")
    args = parser.parse_args()

if __name__ == "__main__":
    # Define the help message
    help_message = textwrap.dedent('''

    if id is None:
        raise ValueError(f"Invalid URL. The specified URL is not a valid {content_type} URL.")

    return f"https://www.youtube.com/watch?v={id}" if content_type == 'video' else f"https://www.youtube.com/playlist?list={id}"
    try:
        url = parse_url(args.url, args.download)
        download_content(url, args.download)
    except ValueError as e:
        print(e)
        exit()
