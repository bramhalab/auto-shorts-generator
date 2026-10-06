import os
import subprocess

def generate_voice_over(scenes):
    """
    Generates TTS audio tracks per scene using gTTS / edge-tts or fallback python audio synthesis (espeak / ffmpeg beep / gtts).
    """
    audio_paths = []
    os.makedirs("temp_audio", exist_ok=True)

    try:
        from gtts import gTTS
        has_gtts = True
    except ImportError:
        has_gtts = False

    for idx, scene in enumerate(scenes, 1):
        scene_id = scene.get('id', scene.get('scene_number', idx))
        audio_file = f"temp_audio/scene_{scene_id}.mp3"
        text = scene.get("voiceover", "Hello world")

        generated = False
        if has_gtts:
            try:
                tts = gTTS(text=text, lang="hi")
                tts.save(audio_file)
                generated = True
            except Exception as e:
                print(f"gTTS error for scene {scene_id}: {e}")

        if not generated:
            # Fallback: Generate real silent audio track with text duration estimate using ffmpeg
            duration = max(3, len(text) // 15)
            cmd = [
                "ffmpeg", "-y", "-f", "lavfi", "-i", f"anullsrc=r=44100:cl=mono",
                "-t", str(duration), "-q:a", "9", "-acodec", "libmp3lame", audio_file
            ]
            subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        audio_paths.append(audio_file)

    return audio_paths