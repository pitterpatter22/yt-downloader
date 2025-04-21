# YouTube Downloader

A simple command-line tool for downloading YouTube videos or extracting audio using the `yt_dlp` Python module.

## Features

- Download full videos in MP4 format.
- Download audio-only tracks and convert them to MP3.
- Specify a custom output directory (defaults to `yt-downloads`).
- Cross-platform support (Windows, macOS, Linux).
- Graceful error handling with pauses to review any issues.
- Dependency checks for required Python modules.

## Prerequisites

- Python 3.6 or higher
- [yt-dlp](https://github.com/yt-dlp/yt-dlp) (`pip install yt-dlp`)
- [pyfiglet](https://github.com/pwaller/pyfiglet) (`pip install pyfiglet`)
- [ffmpeg](https://ffmpeg.org/) (for MP3 conversion)

## Installation

1. Clone this repository or download `downloader.py`.
2. Install the required Python packages:

   ```bash
   pip install yt-dlp pyfiglet
   ```

3. Ensure `ffmpeg` is installed and available in your PATH.

## Usage

Run the downloader script with optional output directory:

```bash
python downloader.py [-o OUTPUT_DIR]
```

- `-o, --output`  
  Specify the folder to save downloads. Defaults to `yt-downloads`.

After launching, select:

1. **Full** to download video (MP4).  
2. **Audio** to download and convert to MP3.  
3. Enter one or more video URLs to queue.  
4. Leave the URL prompt blank to begin downloading the queued items.

## Examples

Download videos into the default folder:

```bash
python downloader.py
```

Download audio into a custom folder:

```bash
python downloader.py -o /path/to/my-music
```

## Error Handling

If the script encounters an error (e.g., missing dependencies or download failure), it will display the error message and wait for you to press Enter before exiting, allowing you to review what went wrong.

## License

This project is licensed under the MIT License.
