<h1>YTDownloader</h1>

<p>YTDownloader is a Python script that uses the <code>yt_dlp</code> library to download videos from a YouTube playlist.</p>

<h2>Prerequisites</h2>

<p>Before you can use YTDownloader, you need to have the following software installed on your computer:</p>

<ul>
  <li>Python 3</li>
  <li><code>pip</code>, the Python package manager</li>
</ul>

<h2>Installation</h2>

<p>To install YTDownloader, follow these steps:</p>

<ol>
  <li>Clone the repository by typing the following command:</li>
</ol>

<pre><code>git clone https://github.com/FiditeNeminiOpenSource/YTDownloader.git
</code></pre>

<ol start="2">
  <li>Navigate to the cloned repository by typing the following command:</li>
</ol>

<pre><code>cd YTDownloader
</code></pre>

<ol start="3">
  <li>Create a new <code>venv</code> called <code>YTDownloader</code> by typing the following command:</li>
</ol>

<pre><code>python3 -m venv YTDownloader
</code></pre>

<ol start="4">
  <li>Activate the <code>venv</code> by typing the following command:</li>
</ol>

<pre><code>source YTDownloader/bin/activate
</code></pre>

<ol start="5">
  <li>Install the necessary libraries by typing the following command:</li>
</ol>

<pre><code>pip install yt-dlp
</code></pre>

<h2>Usage</h2>

<p>To use YTDownloader, follow these steps:</p>

<ol>
  <li>Activate the <code>venv</code> by typing the following command:</li>
</ol>

<pre><code>source YTDownloader/bin/activate
</code></pre>

<ol start="2">
  <li>Run the script by typing the following command, replacing <code>&lt;playlist_id&gt;</code> with the ID of the YouTube playlist you want to download:</li>
</ol>

<pre><code>python3 downloader.py &lt;playlist_id&gt;
</code></pre>

<p>This will run the script and download the videos in the playlist with the specified ID. The downloaded videos will be saved in a new directory called <code>Downloads</code> in the current directory.</p>

<h2>Contributing</h2>

<p>If you would like to contribute to YTDownloader, feel free to submit a pull request or open an issue on the GitHub repository. We welcome any contributions or feedback.</p>
