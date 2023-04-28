import os
import argparse
import yt_dlp
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

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

    print("All videos downloaded successfully!")

if __name__ == "__main__":
    # Parse the playlist ID from the command line arguments
    parser = argparse.ArgumentParser(description="Download a YouTube playlist.")
    parser.add_argument("playlist_id", help="The ID of the YouTube playlist.")
    args = parser.parse_args()

    # Download the playlist
    download_playlist(args.playlist_id)
