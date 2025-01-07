#  Media Downloader

This comprehensive script facilitates the retrieval of video, audio, and Spotify playlists by leveraging robust tools such as `yt-dlp`, `spotdl`, and `ffmpeg`. Designed with efficiency and flexibility in mind, it offers a streamlined command-line interface for managing diverse media downloads.

## Core Features

- **High-Quality Video Downloading:** Secure videos in the highest available resolution.
- **Audio Extraction:** Seamlessly extract and save high-quality audio tracks from video files.
- **Spotify Playlist Archival:** Download complete playlists from Spotify with precision.
- **Video Format Conversion:** Utilize FFmpeg to convert downloaded videos into standardized MP4 formats when necessary.

## Prerequisites

### Required Tools

1. [yt-dlp](https://github.com/yt-dlp/yt-dlp)

   - Installation: `pip install yt-dlp`

2. [FFmpeg](https://ffmpeg.org/)

   - Ensure FFmpeg is added to your system PATH (environment variable).

3. [spotdl](https://github.com/spotDL/spotify-downloader)

   - Installation: `pip install spotdl`

### Python Dependencies

The script employs the following Python libraries:

- `subprocess`
- `os`
- `glob`

Ensure Python 3 is installed, and all necessary tools are configured prior to use.

## Setup Instructions

1. Clone the repository or copy the script into a Python file with a `.py` extension.
2. Verify the installation of all dependencies and tools outlined above.

## Usage Guidelines

Execute the script via Python as follows:

```bash
python main.py
```

### Functional Menu

Upon execution, the script presents the following options:

1. **Download Video:** Input a video URL to initiate download.
2. **Download Audio:** Provide a video URL to extract and save the audio as an MP3 file.
3. **Download Spotify Playlist:** Enter a Spotify playlist URL to download all contained tracks.
4. **Exit:** Terminate the program.

### Workflow Examples

#### Video Download

1. Select option `1` from the menu.
2. Input the video URL.
3. The video will be downloaded and saved to the Desktop directory by default.

#### Audio Download

1. Select option `2` from the menu.
2. Provide the video URL.
3. The extracted audio will be saved as an MP3 file in the Desktop directory.

#### Spotify Playlist Download

1. Choose option `3` from the menu.
2. Provide the Spotify playlist URL.
3. Tracks will be downloaded into the `downloaded_songs` subdirectory on the Desktop.

## File Storage

- Video and audio files default to storage at `C:\Users\<YourUsername>\OneDrive\Desktop`.
- Spotify tracks are saved in a dedicated subdirectory named `downloaded_songs` within the Desktop folder.

## Troubleshooting Tips

- Confirm that all dependencies are correctly installed and accessible via the system PATH.
- For missing tools, refer to their respective documentation for installation guidance.
- Verify file system permissions if downloads fail to save properly.

## License Information

This project is distributed under the MIT License.

## Contribution Opportunities

Contributors are welcome to submit issues, suggest enhancements, or create pull requests to improve this script.

## Acknowledgments

We acknowledge the following projects for enabling the development of this script:

- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- [FFmpeg](https://ffmpeg.org/)
- [spotDL](https://github.com/spotDL/spotify-downloader)

