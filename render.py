import os
import subprocess
import json

def render_short_video(script_json, audio_files, media_assets, bgm_file):
    """
    Composes vertical short video using FFmpeg.
    Combines scene images, scene voiceovers, and subtitles/captions into an MP4 file.
    """
    os.makedirs("output", exist_ok=True)
    os.makedirs("temp_render", exist_ok=True)
    output_path = "output/generated_short.mp4"
    
    scene_videos = []
    scenes = script_json.get("scenes", [])

    for i, (audio, img) in enumerate(zip(audio_files, media_assets)):
        scene_output = f"temp_render/scene_{i}.mp4"
        caption = scenes[i].get("caption", "") if i < len(scenes) else ""
        caption_clean = caption.replace("'", "").replace('"', '').replace(":", " -")

        # Command to construct scene video from image + voiceover + caption text filter
        cmd = [
            "ffmpeg", "-y",
            "-loop", "1", "-i", img,
            "-i", audio,
            "-vf", f"scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,drawtext=text='{caption_clean}':fontcolor=white:fontsize=45:box=1:boxcolor=black@0.6:boxborderw=20:x=(w-text_w)/2:y=h-300",
            "-c:v", "libx264", "-tune", "stillimage",
            "-c:a", "aac", "-b:a", "192k",
            "-pix_fmt", "yuv420p",
            "-shortest",
            scene_output
        ]
        
        res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        if res.returncode != 0:
            # Fallback without drawtext if font/filter fails
            cmd_simple = [
                "ffmpeg", "-y",
                "-loop", "1", "-i", img,
                "-i", audio,
                "-vf", "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920",
                "-c:v", "libx264", "-tune", "stillimage",
                "-c:a", "aac", "-b:a", "1920k",
                "-pix_fmt", "yuv420p",
                "-shortest",
                scene_output
            ]
            subprocess.run(cmd_simple, check=True)

        scene_videos.append(scene_output)

    # Create list file for concat
    list_file = "temp_render/concat_list.txt"
    with open(list_file, "w", encoding="utf-8") as f:
        for v in scene_videos:
            f.write(f"file '{os.path.abspath(v)}'\n")

    # Concat scenes into final output video
    concat_cmd = [
        "ffmpeg", "-y",
        "-f", "concat", "-safe", "0",
        "-i", list_file,
        "-c", "copy",
        output_path
    ]
    subprocess.run(concat_cmd, check=True)

    print(f"Video rendered successfully at: {output_path}")
    return output_path