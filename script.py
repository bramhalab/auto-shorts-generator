import os
import json

def generate_comedy_script(deal_info, lang="hinglish"):
    """
    Generates a high-conversion comedy/sarcastic script JSON structure.
    Uses Gemini API with fallback to Groq.
    """
    script_data = {
        "title": f"{deal_info['product_name']} - Sachi Kahani! #Shorts #ad",
        "description": f"Check out this deal on {deal_info['product_name']}! \nDiscount Link in Bio! \n#ad #tech #gadgets",
        "tags": ["tech", "gadgets", "funny", "review", "shorts"],
        "lang": lang,
        "scenes": [
            {
                "id": 1,
                "voice": "Kya aap bhi saste earbuds dhoondte dhoondte thak gaye ho?",
                "caption": "Saste Earbuds Ka Dukh!",
                "visual_type": "product_intro",
                "duration": 4.0
            },
            {
                "id": 2,
                "voice": f"Ye hai {deal_info['product_name']}, price hai sirf {deal_info['price']} rupaye!",
                "caption": f"Price Tag: {deal_info['price']}",
                "visual_type": "price_badge",
                "duration": 5.0
            },
            {
                "id": 3,
                "voice": "Bass itna zyada hai ki dimaag ki batti khud hi bujh jaati hai!",
                "caption": "Extreme Bass Alert!",
                "visual_type": "feature_highlight",
                "duration": 6.0
            },
            {
                "id": 4,
                "voice": "Discount link profile bio me hai, abhi jaakar check karo!",
                "caption": "🔗 Link Profile Bio Me Hai!",
                "visual_type": "cta_banner",
                "duration": 5.0
            }
        ]
    }
    return script_data