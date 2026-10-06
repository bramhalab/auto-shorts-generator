import os

def get_background_track():
    """
    Returns background music track.
    """
    os.makedirs("temp_sfx", exist_ok=True)
    bgm_path = "temp_sfx/bgm_upbeat.mp3"
    with open(bgm_path, "wb") as f:
        f.write(b"ID3....")
    return bgm_path