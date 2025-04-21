#!/usr/bin/env python3

import argparse
import os
import platform
import sys

# Ensure yt_dlp module is available
try:
    import yt_dlp
except ModuleNotFoundError:
    print("Error: yt_dlp module not found. Please install with `pip install yt-dlp`")
    sys.exit(1)

from pyfiglet import Figlet

# Determine clear-screen command based on operating system
CLEAR_CMD = 'cls' if platform.system() == 'Windows' else 'clear'

# Parse command-line arguments
parser = argparse.ArgumentParser(description="YouTube Downloader")
parser.add_argument('-o', '--output', default='yt-downloads',
                    help="Download folder (default: yt-downloads)")
args = parser.parse_args()
DOWNLOAD_DIR = os.path.abspath(args.output)
# Create the download directory if it doesn't exist
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

f = Figlet(font='slant')
entry = (f.renderText('YT-DL'))
done = (f.renderText('DONE'))

download_list = []

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    

def download_video(mode):
    
    # Set up yt_dlp options based on mode
    if mode == "full":
        print(f"\n{bcolors.HEADER}{bcolors.BOLD}{bcolors.UNDERLINE}"
              f"{bcolors.OKGREEN}Downloading as MP4... {bcolors.ENDC}\n")
        ydl_opts = {
            'format': 'bv*+ba/b',
            'outtmpl': os.path.join(DOWNLOAD_DIR, '%(uploader)s/%(title)s.%(ext)s'),
        }
    else:  # mode == "audio"
        print(f"\n{bcolors.HEADER}{bcolors.BOLD}{bcolors.UNDERLINE}"
              f"{bcolors.OKGREEN}Downloading and Converting to MP3... {bcolors.ENDC}\n")
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': os.path.join(DOWNLOAD_DIR, '%(uploader)s/%(title)s.%(ext)s'),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

    # Download each URL in the list
    for index, url in enumerate(download_list, start=1):
        print(f"\n{bcolors.HEADER}{bcolors.BOLD}{bcolors.UNDERLINE}"
              f"Working on item {index} of {len(download_list)}... {bcolors.ENDC}\n")
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            print(f"{bcolors.OKGREEN}Download completed successfully.{bcolors.ENDC}")
        except Exception as e:
            print(f"{bcolors.FAIL}An error occurred: {e}{bcolors.ENDC}")
            input("Press Enter to continue and view the error...")
            return False

    download_list.clear()
    return True

def get_video_list(mode=None):
    os.system(CLEAR_CMD)
    print(f"{bcolors.OKGREEN}{bcolors.BOLD}{entry}{bcolors.ENDC}")
    
    if mode:
        print(f"{bcolors.OKBLUE}Download mode set to {mode}.{bcolors.ENDC}")
    
    if download_list:
        print(f"{bcolors.HEADER}Current Queue:{bcolors.ENDC}")
        for item in download_list:
            print(f"{bcolors.OKCYAN}\t- {item}{bcolors.ENDC}")
    
    url = input(f"{bcolors.HEADER}\nEnter the video URL (BLANK to continue or type 'q' to quit): {bcolors.ENDC}").strip()
    
    return url

def prompt_download_type():
    os.system(CLEAR_CMD)
    print(f"{bcolors.OKGREEN}{bcolors.BOLD}{entry}{bcolors.ENDC}")
    download_type = None
    while True:
        choice = input(f"{bcolors.HEADER}\nDo you want to download the (F)ull video, just the (A)udio, or (Q)uit? (f/a/q): {bcolors.ENDC}").strip()
        if choice == 'f':
            download_type = "full"
            break
        elif choice == 'a':
            download_type = "audio"
            break
        elif choice == 'q':
            return None
        else:
            print(f"{bcolors.WARNING}Invalid choice \"{choice}\", must be either \"f, a, or q\"... try again... {bcolors.ENDC}")
        
    return download_type


def main():
    success = False
    download_type = prompt_download_type()
    while True:
        url = get_video_list(mode=download_type)
        if url.lower() == 'q':
            break
        elif url.startswith(("http", "https")):
            download_list.append(url)
        elif not url:
            if len(download_list) == 0:
                print(f"{bcolors.OKBLUE}No Items added to list, exiting...{bcolors.ENDC}")
                break
            print(f"{bcolors.HEADER}Starting download of {len(download_list)} item(s)....{bcolors.ENDC}")
            success = download_video(mode=download_type)
            
            if success:
                print(f"{bcolors.OKGREEN}{bcolors.BOLD}\n{done}\n{bcolors.ENDC}")
                input("Press any key to exit...")
                return
            if not success:
                print(f"{bcolors.WARNING}Looks like there was an error.... {bcolors.ENDC}")
                input("Press any key to exit...")
                return
            
        else:
            print(f"{bcolors.WARNING}Doesn't look like thats a url... try again... {bcolors.ENDC}")

    
if __name__ == "__main__":
    main()
    print(f"\n\n{bcolors.HEADER}Exiting...{bcolors.HEADER}")
