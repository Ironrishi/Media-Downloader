import os
import subprocess

DOWNLOADS = os.path.join(os.path.expanduser("~"), "Downloads")

def mp4(url):
    output_template = os.path.join(DOWNLOADS, "%(title)s.%(ext)s")
    command = [
        "yt-dlp",
        "-f", "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
        "--merge-output-format", "mp4",

        "--add-metadata",
        "--embed-metadata",
        "--embed-thumbnail",
        "--embed-chapters",

        "--sub-langs", "all",
        "--embed-subs",

        "-o", output_template,
        url
    ]
    try:
        subprocess.run(command, check=True)
        print("Video downloaded")
    except subprocess.CalledProcessError as e:
        print(f"Video download failed: {e}")
    except FileNotFoundError:
        print("yt-dlp not found in PATH, install using 'pip install yt-dlp'")

def mp3(url):
    output_template = os.path.join(DOWNLOADS, "%(title)s.%(ext)s")
    command = [
        "yt-dlp",
        "-f", "bestaudio",

        "--extract-audio",
        "--audio-format", "mp3",
        "--audio-quality", "0",

        "--add-metadata",
        "--embed-metadata",
        "--embed-thumbnail",

        "-o", output_template,
        url
    ]
    try:
        subprocess.run(command, check=True)
        print("Audio downloaded")
    except subprocess.CalledProcessError as e:
        print(f"Audio download failed: {e}")
    except FileNotFoundError:
        print("yt-dlp not found in PATH, install using 'pip install yt-dlp'")

def spotify(playlist_url):
    os.makedirs(DOWNLOADS, exist_ok=True)
    command = [
        "spotdl",
        playlist_url,

        "--format", "flac",
        "--bitrate", "auto",

        "--threads", "4",
        "--preload",

        "--output", f"{DOWNLOADS}/%(artist)s/%(album)s/%(track-number)02d - %(title)s.%(ext)s"
    ]
    try:
        subprocess.run(command, check=True)
        print("Spotify download complete")
    except subprocess.CalledProcessError as e:
        print(f"Spotify download failed: {e}")
    except FileNotFoundError:
        print("spotdl not found in PATH, install using 'pip install spotdl'")


if __name__ == "__main__":
    while True:
        print("\n1. Video")
        print("2. Audio")
        print("3. Spotify Playlist")
        print("4. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            mp4(input("Enter video URL: ").strip())
        elif choice == "2":
            mp3(input("Enter audio URL: ").strip())
        elif choice == "3":
            spotify(input("Enter Spotify playlist URL: ").strip())
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")
