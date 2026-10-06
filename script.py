import os
import sys
import json
import google.generativeai as genai

# Read inputs from GitHub Workflow environment
topic_input = os.getenv("INPUT_TOPIC", "").strip()
custom_script_input = os.getenv("INPUT_CUSTOM_SCRIPT", "").strip()
affiliate_link = os.getenv("INPUT_AFFILIATE_LINK", "").strip()
language = os.getenv("INPUT_LANGUAGE", "hinglish").strip()
gemini_api_key = os.getenv("GEMINI_API_KEY", "").strip()

script_data = None

# Logic: Custom Script Check
if custom_script_input:
    print(">>> Custom Script detected! Bypassing AI generation...")
    
    # Check if input is valid JSON or plain text
    try:
        script_data = json.loads(custom_script_input)
    except json.JSONDecodeError:
        # Fallback if text is provided directly instead of JSON
        script_data = {
            "title": topic_input if topic_input else "Custom Video",
            "scenes": [
                {
                    "scene_number": 1,
                    "voiceover": custom_script_input,
                    "caption": "Watch Till End! 🚀",
                    "visual_keywords": topic_input if topic_input else "product"
                }
            ]
        }
else:
    print(">>> No Custom Script provided. Generating via Gemini AI...")
    
    if not gemini_api_key:
        print("Error: GEMINI_API_KEY secret missing!")
        sys.exit(1)

    genai.configure(api_key=gemini_api_key)
    model = genai.GenerativeModel('gemini-2.5-flash')

    prompt = f"""
    Create a highly engaging, sarcastic, roast-style YouTube Short script in 2 SCENES ONLY.
    Topic/Product: {topic_input if topic_input else 'Trending Tech Product'}
    Language: {language}

    Return strictly a valid JSON object with no markdown formatting or backticks:
    {{
      "title": "Short Title",
      "scenes": [
        {{
          "scene_number": 1,
          "voiceover": "Sarcastic hook and roast text here (0-8s)",
          "caption": "Short punchy caption with emoji",
          "visual_keywords": "search terms for visual clips"
        }},
        {{
          "scene_number": 2,
          "voiceover": "Price roast and call to action text here (8-15s)",
          "caption": "Offer detail + Link in bio caption",
          "visual_keywords": "search terms for visual clips"
        }}
      ]
    }}
    """

    response = model.generate_content(prompt)
    raw_text = response.text.replace("```json", "").replace("```", "").strip()
    script_data = json.loads(raw_text)

# Output Script Result
print("\n--- Final Script Processing ---")
print(json.dumps(script_data, indent=2))

# Save script to local JSON for video rendering step
with open("generated_script.json", "w", encoding="utf-8") as f:
    json.dump(script_data, f, ensure_ascii=False, indent=2)

print(">>> Script successfully created and saved to generated_script.json!")
