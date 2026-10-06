import json
import os
from datetime import datetime

def log_campaign_state(deal_info, script_json, upload_result):
    """
    Logs campaign history.
    """
    os.makedirs("logs", exist_ok=True)
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "product": deal_info['product_name'],
        "price": deal_info['price'],
        "affiliate_url": deal_info['affiliate_url'],
        "video_id": upload_result.get("video_id"),
        "status": upload_result.get("status")
    }
    
    with open("logs/campaign_state.jsonl", "a") as f:
        f.write(json.dumps(log_entry) + "\n")
    print("State logged successfully.")