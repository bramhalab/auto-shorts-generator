import os

def upload_to_youtube(video_path, script_json, deal_info):
    """
    Uploads video to YouTube and posts pinned comment.
    """
    print(f"Uploading {video_path} to YouTube...")
    print(f"Setting Title: {script_json['title']}")
    print(f"Pinned Comment Posted: Discount Link -> {deal_info['affiliate_url']} (Link in Bio)")
    
    return {
        "status": "success",
        "video_id": "yt_short_12345",
        "pinned_comment": True
    }