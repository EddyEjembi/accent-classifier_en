import yt_dlp
import os

class VideoProcessor:
    """
    Class to handle video downloading and processing using yt-dlp.
    """
    def __init__(self):
        self.download_dir = "temp_downloads"
        os.makedirs(self.download_dir, exist_ok=True)
    
    def download_video(self, url):
        """
        Download video and extract audio as WAV file
        """
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': f'{self.download_dir}/%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'wav',
                'preferredquality': '192',
            }],
            'postprocessor_args': [
                '-ar', '16000' 
            ],
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            # Get the base filename without extension
            base_filename = ydl.prepare_filename(info)
            # Construct the audio file path by replacing the original extension with .wav
            audio_path = os.path.splitext(base_filename)[0] + '.wav'
            
            print(f"Audio downloaded and converted to: {audio_path}")
            return audio_path