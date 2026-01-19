import json
import os
import random
from jinja2 import Environment, FileSystemLoader

# ==========================================
# Configuration
# ==========================================
TEMPLATE_DIR = 'templates'
TEMPLATE_FILE = 'template.html'
CONFIG_FILE = 'config.json'
OUTPUT_FILE = 'index.html'

ALLOWED_IDS = [
    "GT", 
    "qwn-refined",
    "sabotaged",
    "qwn-omni"
] 

# ==========================================
# Build Logic
# ==========================================
def build():
    if not os.path.exists(CONFIG_FILE):
        print(f"Error: {CONFIG_FILE} not found.")
        return

    with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)

    if 'questions' in data:
        print(f"Processing {len(data['questions'])} questions...")
        
        for q in data['questions']:
            original_captions = q.get('captions', [])
            
            if ALLOWED_IDS:
                filtered_captions = [
                    cap for cap in original_captions 
                    if cap.get('id') in ALLOWED_IDS
                ]
            else:
                filtered_captions = original_captions

            random.shuffle(filtered_captions)
            
            q['captions'] = filtered_captions
            
    # -------------------------------------------------

    env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
    template = env.get_template(TEMPLATE_FILE)

    # Pass the processed data dictionary to the template
    output_html = template.render(**data)

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(output_html)

    print(f"Success! Generated {OUTPUT_FILE}")
    if ALLOWED_IDS:
        print(f"  - Filtered IDs: {ALLOWED_IDS}")
    print(f"  - Captions shuffled: Yes")

if __name__ == "__main__":
    build()