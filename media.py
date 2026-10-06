import os
import requests

def fetch_product_media(scenes, deal_info):
    """
    Fetches high-resolution 1080x1920 images directly without needing any API Key.
    Uses Unsplash/Picsum direct photo endpoints.
    """
    media_paths = []
    os.makedirs("temp_media", exist_ok=True)
    
    query = deal_info.get("product_name", "gadgets").replace(" ", ",")
    
    for scene in scenes:
        media_file = f"temp_media/scene_{scene['id']}.jpg"
        image_url = f"https://picsum.photos/1080/1920?random={scene['id']}"
        
        try:
            response = requests.get(image_url, timeout=10)
            if response.status_code == 200:
                with open(media_file, "wb") as f:
                    f.write(response.content)
            else:
                raise Exception("Failed to fetch image")
        except Exception as e:
            # Fallback placeholder image
            fallback_url = f"https://picsum.photos/1080/1920"
            res = requests.get(fallback_url)
            with open(media_file, "wb") as f:
                f.write(res.content)
                
        media_paths.append(media_file)
        
    return media_paths