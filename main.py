import os
import glob
import subprocess

# Download video
def mp4(url, output_path_template=r'C:\Users\hrish\OneDrive\Desktop\%(title)s.%(ext)s'):  # Replace with your desired output folder
    command = ['yt-dlp', '-f', 'bestvideo+bestaudio/best', '-o', output_path_template, url]
    try:
        subprocess.run(command, check=True)
        print(f"Video downloaded successfully with output template: {output_path_template}")

        # Locate downloaded file
        search_path = output_path_template.replace('%(title)s', '*').replace('%(ext)s', '*')
        downloaded_files = glob.glob(search_path)
        downloaded_files = [f for f in downloaded_files if os.path.isfile(f) and f.lower().endswith(('.mp4', '.webm'))]

        if not downloaded_files:
            raise FileNotFoundError("Could not locate the downloaded video file.")

        actual_path = downloaded_files[0]
        print(f"Located downloaded file: {actual_path}")

        # Convert to MP4
        converted_path = os.path.splitext(actual_path)[0] + '.mp4'
        convert_video(actual_path, converted_path)
    except FileNotFoundError as e:
        print(e)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred during video download: {e}")

# Convert video using FFmpeg
def convert_video(input_path, output_path):
    command = ['ffmpeg', '-i', input_path, output_path]
    try:
        subprocess.run(command, check=True)
        print(f"Video converted successfully and saved to {output_path}")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred during video conversion: {e}")

# Download audio
def mp3(url, output_path_template=r'C:\Users\hrish\OneDrive\Desktop\%(title)s.%(ext)s'): # Replace with your desired output folder
    command = ['yt-dlp', '-f', 'bestaudio', '-o', output_path_template, url]
    try:
        subprocess.run(command, check=True)
        print(f"Audio downloaded successfully with output template: {output_path_template}")
         # Locate downloaded file
        search_path = output_path_template.replace('%(title)s', '*').replace('%(ext)s', '*')
        downloaded_files = glob.glob(search_path)
        downloaded_files = [f for f in downloaded_files if os.path.isfile(f) and f.lower().endswith(('.webm'))]

        if not downloaded_files:
            raise FileNotFoundError("Could not locate the downloaded audio file.")

        actual_path = downloaded_files[0]
        print(f"Located downloaded file: {actual_path}")

        # Convert to MP4
        converted_path = os.path.splitext(actual_path)[0] + '.mp3'
        convert_video(actual_path, converted_path)
    except FileNotFoundError as e:
        print(e)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred during audio download: {e}")


# Download Spotify playlist
def spotify(playlist_url, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    command = ['spotdl', playlist_url, '--output', f"{output_folder}/%(title)s.%(ext)s"]
    try:
        subprocess.run(command, check=True)
        print(f"Spotify playlist downloaded to {output_folder}")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred during Spotify download: {e}")

if __name__ == "__main__":
    while True:
        print("1 for video\n2 for audio\n3 for Spotify\n4 to exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            url = input("Enter the video URL: ").strip()
            mp4(url)
        elif choice == "2":
            url = input("Enter the audio URL: ").strip()
            mp3(url)
        elif choice == "3":
            playlist_url = input("Enter the Spotify playlist URL: ").strip()
            # Replace with your desired output folder
            output_folder = r"C:\Users\hrish\OneDrive\Desktop" 
            spotify(playlist_url, output_folder)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
