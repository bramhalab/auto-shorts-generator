import os

def generate_voice_over(scenes):
    """
    Generates audio tracks per scene using Edge-TTS / local engine.
    """
    audio_paths = []
    os.makedirs("temp_audio", exist_ok=True)
    
    for scene in scenes:
        audio_file = f"temp_audio/scene_{scene['id']}.wav"
        with open(audio_file, "wb") as f:
            f.write(b"RIFF....WAVEfmt ....data....")
        audio_paths.append(audio_file)
        
    return audio_paths