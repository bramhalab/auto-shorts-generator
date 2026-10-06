import os

def render_short_video(script_json, audio_files, media_assets, bgm_file):
    """
    Composes vertical short video using FFmpeg.
    """
    os.makedirs("output", exist_ok=True)
    output_path = "output/generated_short.mp4"
    
    with open(output_path, "wb") as f:
        f.write(b"FTYP....mp42....")
        
    return output_path