#!/usr/bin/env python3
"""
Batch update semua pesan untuk menggunakan blockquote
"""
import re
from pathlib import Path
from typing import List, Tuple

def add_blockquote_safe(text: str) -> str:
    """Tambah blockquote jika belum ada"""
    text = text.strip()
    # Jika sudah ada blockquote, return as is
    if text.startswith('<blockquote>') and text.endswith('</blockquote>'):
        return text
    # Wrap dengan blockquote
    return f'<blockquote>{text}</blockquote>'

def process_file_safe(filepath: str) -> bool:
    """Process file dengan safety checks"""
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    modified = False
    output_lines = []
    i = 0
    
    while i < len(lines):
        line = lines[i]
        
        # Check for message.reply, edit_message_text, send_message, answer
        if any(method in line for method in ['message.reply', 'edit_message_text', 'send_message', '.answer']):
            # Check jika line tersebut dimulai dengan await atau hanya method call
            if '(' in line and '"' in line and '<blockquote>' not in line:
                # Cek apakah ini multi-line call
                if not line.rstrip().endswith(')'):
                    # Multi-line, collect full statement
                    full_stmt = line
                    i += 1
                    while i < len(lines) and ')' not in lines[i]:
                        full_stmt += lines[i]
                        i += 1
                    if i < len(lines):
                        full_stmt += lines[i]
                    
                    # Coba extract string content dan wrap dengan blockquote
                    if '("' in full_stmt:
                        # Find string pattern
                        match = re.search(r'(["\'])([^"\']*)\1', full_stmt)
                        if match and '<blockquote>' not in match.group(2):
                            wrapped = add_blockquote_safe(match.group(2))
                            full_stmt = full_stmt.replace(match.group(0), f'{match.group(1)}{wrapped}{match.group(1)}', 1)
                            modified = True
                    
                    output_lines.append(full_stmt)
                    i += 1
                    continue
        
        output_lines.append(line)
        i += 1
    
    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(output_lines)
        return True
    
    return False

# Main execution
if __name__ == '__main__':
    base_path = Path('/workspaces/YUKA-sz/PyroUbot')
    modules = list((base_path / 'modules').glob('*.py'))
    
    modified_files = []
    for py_file in sorted(modules):
        try:
            if process_file_safe(str(py_file)):
                modified_files.append(py_file.name)
                print(f'✅ {py_file.name}')
        except Exception as e:
            print(f'⚠️  {py_file.name}: {e}')
    
    print(f'\n📊 Total: {len(modified_files)} files modified')
