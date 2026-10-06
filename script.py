import os
import sys
import json

def generate_comedy_script(deal_info, lang="hinglish", custom_script=""):
    """
    Generates a comedy script for the deal info using Gemini API, Groq, custom script, or template fallback.
    """
    custom_script_input = (custom_script or os.getenv("INPUT_CUSTOM_SCRIPT", "") or os.getenv("INPUT_SCRIPT", "")).strip()
    topic_input = deal_info.get("product_name", "") if isinstance(deal_info, dict) else str(deal_info)
    
    if custom_script_input:
        print(">>> Custom Script detected! Bypassing AI generation...")
        try:
            script_data = json.loads(custom_script_input)
        except json.JSONDecodeError:
            script_data = {
                "title": f"Review: {topic_input}" if topic_input else "Custom Video",
                "scenes": [
                    {
                        "id": 1,
                        "scene_number": 1,
                        "voiceover": custom_script_input,
                        "caption": "Watch Till End! 🚀",
                        "visual_keywords": topic_input if topic_input else "product"
                    }
                ]
            }
    else:
        gemini_api_key = os.getenv("GEMINI_API_KEY", "").strip()
        groq_api_key = os.getenv("GROQ_API_KEY", "").strip()
        script_data = None

        prompt = f"""
        Create a highly engaging, sarcastic, roast-style YouTube Short script in 2 SCENES ONLY.
        Topic/Product: {topic_input if topic_input else 'Trending Tech Product'}
        Language: {lang}

        Return strictly a valid JSON object with no markdown formatting or backticks:
        {{
          "title": "Short Title",
          "scenes": [
            {{
              "id": 1,
              "scene_number": 1,
              "voiceover": "Sarcastic hook and roast text here (0-8s)",
              "caption": "Short punchy caption with emoji",
              "visual_keywords": "search terms for visual clips"
            }},
            {{
              "id": 2,
              "scene_number": 2,
              "voiceover": "Price roast and call to action text here (8-15s)",
              "caption": "Offer detail + Link in bio caption",
              "visual_keywords": "search terms for visual clips"
            }}
          ]
        }}
        """

        if gemini_api_key:
            print(">>> Generating script via Gemini AI...")
            try:
                import google.generativeai as genai
                genai.configure(api_key=gemini_api_key)
                model = genai.GenerativeModel('gemini-2.5-flash')
                response = model.generate_content(prompt)
                raw_text = response.text.replace("```json", "").replace("```", "").strip()
                script_data = json.loads(raw_text)
            except Exception as e:
                print(f"Gemini API generation failed: {e}")

        if not script_data and groq_api_key:
            print(">>> Trying Groq AI fallback...")
            try:
                from groq import Groq
                client = Groq(api_key=groq_api_key)
                chat_completion = client.chat.completions.create(
                    messages=[{"role": "user", "content": prompt}],
                    model="llama-3.3-70b-versatile",
                )
                raw_text = chat_completion.choices[0].message.content.replace("```json", "").replace("```", "").strip()
                script_data = json.loads(raw_text)
            except Exception as e:
                print(f"Groq API generation failed: {e}")

        if not script_data:
            print(">>> Using local template fallback script...")
            price = deal_info.get("price", "special price") if isinstance(deal_info, dict) else ""
            flaws = deal_info.get("funny_flaws", ["Itna hype kyon hai bhai?"]) if isinstance(deal_info, dict) else ["Itna hype!"]
            script_data = {
                "title": f"Truth about {topic_input}",
                "scenes": [
                    {
                        "id": 1,
                        "scene_number": 1,
                        "voiceover": f"Kya aap bhi {topic_input} lene ka soch rahe ho? {flaws[0]}!",
                        "caption": f"Is {topic_input} worth it? 🤔",
                        "visual_keywords": topic_input
                    },
                    {
                        "id": 2,
                        "scene_number": 2,
                        "voiceover": f"Mera manno to {price} me theek hai. Link description me hai, jaakar check karo!",
                        "caption": f"Buy at {price} 💥 Link in Bio",
                        "visual_keywords": f"{topic_input} gadget"
                    }
                ]
            }

    # Ensure scenes have 'id' key
    for idx, scene in enumerate(script_data.get("scenes", []), 1):
        if "id" not in scene:
            scene["id"] = scene.get("scene_number", idx)

    print("\n--- Final Script Processing ---")
    print(json.dumps(script_data, indent=2))

    with open("generated_script.json", "w", encoding="utf-8") as f:
        json.dump(script_data, f, ensure_ascii=False, indent=2)

    return script_data

if __name__ == "__main__":
    topic_env = os.getenv("INPUT_TOPIC", "Tech Product")
    generate_comedy_script({"product_name": topic_env})
