import os
import re

def fix_imports_in_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace all SYSTUM imports with ZEFMUSIC
    new_content = re.sub(r'from SYSTUM\s*\.', 'from ZEFMUSIC.', content)
    new_content = re.sub(r'import SYSTUM\s*\.', 'import ZEFMUSIC.', content)
    new_content = re.sub(r'from SYSTUM\s+', 'from ZEFMUSIC ', new_content)
    new_content = re.sub(r'import SYSTUM\s+', 'import ZEFMUSIC ', new_content)
    
    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Fixed imports in {file_path}")

def process_directory(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                fix_imports_in_file(file_path)

if __name__ == "__main__":
    process_directory("ZEFMUSIC")
    print("All imports have been fixed!") 