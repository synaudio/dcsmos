import json
import os
from jinja2 import Environment, FileSystemLoader

# Config
TEMPLATE_DIR = 'templates'
TEMPLATE_FILE = 'template.html'
CONFIG_FILE = 'config.json'
OUTPUT_FILE = 'index.html'

def build():
    if not os.path.exists(CONFIG_FILE):
        print(f"Error: {CONFIG_FILE} not found.")
        return

    with open(CONFIG_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)

    env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
    template = env.get_template(TEMPLATE_FILE)

    # Pass the entire data dictionary to the template
    output_html = template.render(**data)

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(output_html)

    print(f"Success! Generated {OUTPUT_FILE}")

if __name__ == "__main__":
    build()