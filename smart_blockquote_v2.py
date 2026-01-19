#!/usr/bin/env python3
"""
Advanced blockquote adder v2 - lebih aggressive
"""
import re
from pathlib import Path

def add_blockquote_to_strings(content: str) -> str:
    """Tambah blockquote ke semua string literals yang mengandung pesan"""
    
    lines = content.split('\n')
    result_lines = []
    
    for line in lines:
        # Skip lines yang sudah ada blockquote
        if '<blockquote>' in line and '</blockquote>' in line:
            result_lines.append(line)
            continue
        
        # Skip comments dan imports
        if line.strip().startswith('#') or line.strip().startswith('import') or line.strip().startswith('from'):
            result_lines.append(line)
            continue
        
        # Pattern untuk message methods
        if any(method in line for method in ['message.reply', '.edit(', '.send_message', '.answer(', 'client.send_message']):
            # Find f-strings dan regular strings
            # Pattern: (f)?"...", (f)'...', dll
            
            # Handle f"..." patterns
            line = re.sub(
                r'(\.reply\s*\(\s*|\.edit\s*\(\s*|\.send_message\s*\(\s*|\.answer\s*\(\s*)(f?)("|\')((?:(?!\3)[^\\]|\\.)*?)\3',
                lambda m: f'{m.group(1)}{m.group(2)}{m.group(3)}<blockquote>{m.group(4).strip()}</blockquote>{m.group(3)}' if '<blockquote>' not in m.group(4) else m.group(0),
                line
            )
            
            # Handle format() calls
            if '{0}' in line or '{' in line and '}' in line:
                # Preserve format() calls
                result_lines.append(line)
                continue
        
        result_lines.append(line)
    
    return '\n'.join(result_lines)

def process_file_v2(filepath: str) -> bool:
    """Process file dengan v2 algorithm"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            original_content = f.read()
        
        # Apply blockquote additions
        modified_content = add_blockquote_to_strings(original_content)
        
        if modified_content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(modified_content)
            return True
    except Exception as e:
        print(f'Error: {filepath}: {e}')
    
    return False

if __name__ == '__main__':
    base_dir = Path('/workspaces/YUKA-sz/PyroUbot')
    
    modified = 0
    for py_file in sorted(base_dir.glob('modules/*.py')):
        if py_file.name.startswith('__'):
            continue
        if process_file_v2(str(py_file)):
            modified += 1
            print(f'✅ {py_file.name}')
    
    print(f'\n✨ Modified {modified} files')
