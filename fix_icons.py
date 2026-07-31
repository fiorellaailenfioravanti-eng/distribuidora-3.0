import os, re
directory = r'c:\Users\rohan\Documents\GitHub\distribuidora-3.0\templates'
for root, _, files in os.walk(directory):
    for file in files:
        if file.endswith('.html') and not file.startswith('base_'):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            new_content = re.sub(r'(<h1[^>]*>)\s*<i[^>]*>.*?</i>\s*', r'\1', content, flags=re.IGNORECASE)
            new_content = new_content.replace('class="d-flex flex-wrap align-items-center justify-content-between mb-4 gap-3"', 'class="d-flex justify-content-between align-items-center mb-4"')
            new_content = new_content.replace('class="d-flex justify-content-between align-items-center mb-4 flex-wrap gap-3"', 'class="d-flex justify-content-between align-items-center mb-4"')
            new_content = new_content.replace('class="d-flex justify-content-between align-items-start mb-4 flex-wrap gap-3"', 'class="d-flex justify-content-between align-items-center mb-4"')
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f'Updated {file}')
