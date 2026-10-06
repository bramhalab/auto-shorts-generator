import os

def fetch_trending_deals(mode="auto", topic="", affiliate_link=""):
    """
    Fetches trending tech product deals, specs, price drops, and affiliate links.
    """
    if topic:
        product_name = topic
    else:
        product_name = "Boat Airdopes 141 Bluetooth Earbuds"
        
    return {
        "product_name": product_name,
        "price": "₹1,299",
        "original_price": "₹4,490",
        "discount_pct": "71%",
        "rating": "4.1",
        "key_features": [
            "42H Playback time",
            "Beast Mode for Gaming (80ms low latency)",
            "IPX4 Sweat Resistance"
        ],
        "funny_flaws": [
            "Itna bass hai ki kaan me dholak bajne lagti hai",
            "Case itna glossy hai ki finger prints ka crime scene ban jata hai"
        ],
        "affiliate_url": affiliate_link if affiliate_link else "https://amzn.to/example_tag"
    }