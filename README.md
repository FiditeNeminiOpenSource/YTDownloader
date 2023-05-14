
This is a Python script that can be used to download YouTube videos or 
playlists. The script uses the `yt_dlp` library, which is a fork of 
`youtube-dl`. It can handle different types of YouTube URLs and allows the 
user to choose between downloading a video or a playlist.

## Installation

To use this script, you need to have Python 3 installed on your system. 
You can download Python from the official website: 
https://www.python.org/downloads/

You also need to install the `yt_dlp` library. You can install it using 
pip:

```
pip install yt-dlp
```

## Usage

To use the script, open a terminal or command prompt and navigate to the 
directory where the script is located. Then, run the script with the 
following command:

```
python youtube_downloader.py "<url>" --download <type>
```

Replace `<url>` with the URL of the YouTube video or playlist that you 
want to download. Replace `<type>` with either `video` or `playlist`, 
depending on what you want to download. For example, to download a video 
with the URL `https://www.youtube.com/watch?v=5PS2p1AZzFY`, run the 
following command:

```
python youtube_downloader.py "https://www.youtube.com/watch?v=5PS2p1AZzFY" 
--download video
```

To download a playlist with the URL 
`https://www.youtube.com/playlist?list=PLXmi76euGSyyq1nw21U1M4tTsM0Zysayk`, 
run the following command:

```
python youtube_downloader.py 
"https://www.youtube.com/playlist?list=PLXmi76euGSyyq1nw21U1M4tTsM0Zysayk" 
--download playlist
```

If the URL is in the format 
`https://www.youtube.com/watch?v=5PS2p1AZzFY&list=PLXmi76euGSyyq1nw21U1M4tTsM0Zysayk&index=4`, 
the user will be prompted to choose between downloading a video or a 
playlist.

Before each video is downloaded, the script checks to see if it already 
exists in the Downloads folder and skips it if it does. The downloaded 
videos or playlists are saved in a folder called `Downloads` in the same 
directory as the script.

## Conclusion

That's it! You should now be able to download YouTube videos and playlists 
using this Python script. If you encounter any issues or have any 
questions, feel free to open an issue in the GitHub repository or contact 
the author directly.
