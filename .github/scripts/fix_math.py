import os
import re

TARGET_DIRS = [
    "_posts",
    "_thoughts/"
]

def fix_math_in_text(text):
    pattern = r'(```[\s\S]*?```|`[^`\n]*`)'
    parts = re.split(pattern, text)
    new_parts = []
    for part in parts:
        if part.startswith('`'):
            new_parts.append(part)
        else:
            fixed_part = re.sub(r'(?<![\$\\])\$(?!\$)', '$$', part)
            new_parts.append(fixed_part)
            
    return "".join(new_parts)

def process_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content = fix_math_in_text(content)
        
        if new_content != content:
            print(f"  [Fixed] {file_path}")
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
    except Exception as e:
        print(f"  [Error] Failed to process {file_path}: {e}")

def main():
    print("Starting MathJax Fixer...")
    for target in TARGET_DIRS:
        if not os.path.exists(target):
            print(f"Skipping {target} (Not found)")
            continue
        if os.path.isdir(target):
            print(f"Scanning directory: {target}...")
            for root, _, files in os.walk(target):
                for file in files:
                    if file.endswith(".md"):
                        process_file(os.path.join(root, file))
        elif os.path.isfile(target) and target.endswith(".md"):
            print(f"Scanning file: {target}...")
            process_file(target)
    print("Done.")

if __name__ == "__main__":
    main()
