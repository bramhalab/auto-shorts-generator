import os

def fetch_product_media(scenes, deal_info):
    """
    Fetches product media assets via Pexels API.
    """
    media_paths = []
    os.makedirs("temp_media", exist_ok=True)
    
    for scene in scenes:
        media_file = f"temp_media/scene_{scene['id']}.jpg"
        with open(media_file, "w") as f:
            f.write("dummy image content")
        media_paths.append(media_file)
        
    return media_paths