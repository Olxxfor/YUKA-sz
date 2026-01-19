#!/usr/bin/env python3
"""
Advanced script untuk menambah blockquote ke semua pesan dalam semua Python files
Menggunakan tokenization untuk menghindari false positives
"""
import re
from pathlib import Path
from typing import Dict, List

def find_string_literals(line: str) -> List[tuple]:
    """Find semua string literals dalam baris"""
    results = []
    i = 0
    while i < len(line):
        if line[i] in ('"', "'"):
            quote = line[i]
            start = i
            i += 1
            while i < len(line):
                if line[i] == quote and (i == 0 or line[i-1] != '\\'):
                    results.append((start, i+1, quote, line[start+1:i]))
                    break
                i += 1
            else:
                i = start + 1
        else:
            i += 1
    return results

def needs_blockquote(text: str) -> bool:
    """Check apakah string perlu blockquote"""
    text = text.strip()
    
    # Jika sudah ada blockquote, tidak perlu
    if '<blockquote>' in text and '</blockquote>' in text:
        return False
    
    # Jika kosong, tidak perlu
    if not text or text.isspace():
        return False
    
    # Jika mengandung HTML tags, perlu blockquote
    if '<' in text and '>' in text:
        return True
    
    # Jika mengandung emoji id, perlu blockquote
    if '<emoji' in text:
        return True
    
    # Jika mengandung error/info messages panjang, perlu blockquote
    if len(text) > 30 and any(kw in text.lower() for kw in ['error', 'failed', 'success', 'warning', 'info']):
        return True
    
    return False

def process_line(line: str) -> str:
    """Process satu line untuk menambah blockquote"""
    if '<blockquote>' in line:
        return line
    
    # Cari method calls yang mungkin mengandung pesan
    message_methods = ['message.reply', 'edit_message_text', 'send_message', 'answer', '.edit', '.delete']
    if not any(method in line for method in message_methods):
        return line
    
    # Find string literals
    strings = find_string_literals(line)
    
    if not strings:
        return line
    
    # Process strings dari belakang ke depan untuk maintain indices
    modified_line = line
    for start, end, quote, text in reversed(strings):
        if needs_blockquote(text):
            wrapped = f'<blockquote>{text.strip()}</blockquote>'
            modified_line = modified_line[:start+1] + wrapped + modified_line[end-1:]
    
    return modified_line

def process_file(filepath: str) -> bool:
    """Process single file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        original_lines = lines.copy()
        modified_lines = []
        
        for line in lines:
            # Skip comments dan empty lines
            if line.strip().startswith('#') or not line.strip():
                modified_lines.append(line)
                continue
            
            processed_line = process_line(line)
            modified_lines.append(processed_line)
        
        if modified_lines != original_lines:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.writelines(modified_lines)
            return True
    except Exception as e:
        print(f'Error in {filepath}: {e}')
    
    return False

def main():
    """Main"""
    base_dir = Path('/workspaces/YUKA-sz/PyroUbot')
    
    # Process modules
    modules_dir = base_dir / 'modules'
    helpers_dir = base_dir / 'core/helpers'
    
    modified_count = 0
    
    print('🔄 Processing files...')
    for directory in [modules_dir, helpers_dir]:
        for py_file in sorted(directory.glob('*.py')):
            if py_file.name in ['__init__.py', '__main__.py', 'text.py']:
                continue
            
            if process_file(str(py_file)):
                modified_count += 1
                print(f'✅ {py_file.name}')
    
    print(f'\n✨ Done! Modified {modified_count} files')

if __name__ == '__main__':
    main()
