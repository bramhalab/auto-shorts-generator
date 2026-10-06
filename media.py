import os
import requests
from PIL import Image, ImageDraw, ImageFont

def create_card_image(text, output_file, bg_color=(30, 30, 40), text_color=(255, 255, 255)):
    """Creates a 1080x1920 card image with title text."""
    img = Image.new('RGB', (1080, 1920), color=bg_color)
    draw = ImageDraw.Draw(img)

    # Try using default or simple font
    try:
        font = ImageFont.truetype("DejaVuSans-Bold.ttf", 60)
    except IOError:
        font = ImageFont.load_default()

    # Draw simple centered text / box
    draw.rectangle([50, 600, 1030, 1300], fill=(50, 50, 70), outline=(255, 215, 0), width=5)

    # Text line split
    lines = [text[i:i+30] for i in range(0, len(text), 30)]
    y_pos = 700
    for line in lines:
        draw.text((100, y_pos), line, fill=text_color, font=font)
        y_pos += 80

    img.save(output_file)

def fetch_product_media(scenes, deal_info):
    """
    Fetches high-resolution 1080x1920 images directly or generates placeholder images if network fails.
    """
    media_paths = []
    os.makedirs("temp_media", exist_ok=True)
    
    product_name = deal_info.get("product_name", "Product") if isinstance(deal_info, dict) else str(deal_info)
    
    for idx, scene in enumerate(scenes, 1):
        scene_id = scene.get('id', scene.get('scene_number', idx))
        media_file = f"temp_media/scene_{scene_id}.jpg"
        image_url = f"https://picsum.photos/1080/1920?random={scene_id}"
        
        success = False
        try:
            response = requests.get(image_url, timeout=5)
            if response.status_code == 200 and len(response.content) > 1000:
                with open(media_file, "wb") as f:
                    f.write(response.content)
                success = True
        except Exception as e:
            print(f"Image download failed for scene {scene_id}: {e}")

        if not success:
            caption = scene.get("caption", product_name)
            create_card_image(f"{product_name}\n\n{caption}", media_file)
                
        media_paths.append(media_file)
        
    return media_paths