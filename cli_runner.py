import os
from research import fetch_trending_deals
from script import generate_comedy_script
from voice import generate_voice_over
from media import fetch_product_media
from sfx import get_background_track
from render import render_short_video
from upload import upload_to_youtube
from state import log_campaign_state

def main():
    topic = os.getenv("INPUT_TOPIC", "")
    affiliate_link = os.getenv("INPUT_AFFILIATE", "")
    lang = os.getenv("INPUT_LANG", "hinglish")
    mode = "product" if topic else "auto"

    print(f"--- Starting Pipeline | Mode: {mode} | Topic: {topic} ---")

    # 1. Fetch Deal Info
    deal_info = fetch_trending_deals(mode=mode, topic=topic, affiliate_link=affiliate_link)
    
    # 2. Script Generation
    script_json = generate_comedy_script(deal_info, lang=lang)
    
    # 3. Voice Generation
    audio_files = generate_voice_over(script_json['scenes'])
    
    # 4. Media Assets
    media_assets = fetch_product_media(script_json['scenes'], deal_info)
    
    # 5. SFX & Background Music
    bgm_file = get_background_track()
    
    # 6. Render Video
    video_path = render_short_video(script_json, audio_files, media_assets, bgm_file)
    
    # 7. Upload to YouTube
    upload_result = upload_to_youtube(video_path, script_json, deal_info)
    
    # 8. Log State
    log_campaign_state(deal_info, script_json, upload_result)
    print("--- Pipeline Completed Successfully ---")

if __name__ == "__main__":
    main()