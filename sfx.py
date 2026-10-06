import os
import subprocess

def get_background_track():
    """
    Returns background music track or creates a dummy audio file using FFmpeg if not present.
    """
    os.makedirs("temp_sfx", exist_ok=True)
    bgm_path = "temp_sfx/bgm_upbeat.mp3"
    if not os.path.exists(bgm_path) or os.path.getsize(bgm_path) < 100:
        cmd = [
            "ffmpeg", "-y", "-f", "lavfi", "-i", "anullsrc=r=44100:cl=stereo",
            "-t", "30", "-q:a", "9", "-acodec", "libmp3lame", bgm_path
        ]
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    return bgm_path