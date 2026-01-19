#!/usr/bin/env python3
"""
Script untuk menambahkan <blockquote> ke semua pesan Python
Menggunakan regex untuk handle berbagai format
"""
import os
import re
from pathlib import Path

def wrap_blockquote(text):
    """Wrap teks dengan blockquote jika belum ada"""
    text = text.strip()
    if text.startswith('<blockquote>') and text.endswith('</blockquote>'):
        return text
    return f'<blockquote>{text}</blockquote>'

def process_help_string(content):
    """Process __HELP__ = """...""""
    # Match __HELP__ = """...""" atau __HELP__ = '''...'''
    def replacer(match):
        full_match = match.group(0)
        prefix = match.group(1) or ''
        quote = match.group(2)
        help_text = match.group(3)
        
        # Jika kosong atau hanya whitespace
        if not help_text.strip():
            return full_match
        
        # Jika sudah ada blockquote, skip
        if '<blockquote>' in help_text and '</blockquote>' in help_text:
            return full_match
        
        # Wrap dengan blockquote
        wrapped = wrap_blockquote(help_text)
        return f'{prefix}__HELP__ = {quote}{wrapped}{quote}'
    
    pattern = r'(__MODULE__\s*=\s*[fu]?["\'][^"\']*["\'][\s\n]+)?__HELP__\s*=\s*("""|\'\'\'|f"""|f\'\'\'|fr"""|fr\'\'\')(.*?)\2'
    return re.sub(pattern, replacer, content, flags=re.DOTALL)

def process_reply_messages(content):
    """Process message.reply(...) dan similar"""
    
    # Match f"..." atau "..." dalam reply/edit_message_text/send_message
    def replacer(match):
        full_match = match.group(0)
        method = match.group(1)
        prefix = match.group(2) or ''
        quote = match.group(3)
        msg_text = match.group(4)
        
        # Skip jika sudah ada blockquote
        if '<blockquote>' in msg_text and '</blockquote>' in msg_text:
            return full_match
        
        # Skip jika pesan terlalu pendek atau tidak penting
        if len(msg_text.strip()) < 3:
            return full_match
        
        # Skip jika tidak mengandung HTML tags
        if '<' not in msg_text and '>' not in msg_text:
            return full_match
        
        # Wrap dengan blockquote
        wrapped = wrap_blockquote(msg_text)
        return f'{method}({prefix}{quote}{wrapped}{quote}'
    
    # Pattern untuk reply, edit_message_text, send_message
    pattern = r'(\.(?:reply|edit_message_text|send_message|answer)\s*\(\s*)(["\'])?(["\']|f["\']|fr["\'])((?:(?!\3).)*?)\3'
    return re.sub(pattern, replacer, content, flags=re.DOTALL)

def process_file(filepath):
    """Process satu file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original_content = content
        
        # Process __HELP__ strings
        content = process_help_string(content)
        
        # Process reply messages
        content = process_reply_messages(content)
        
        # Tulis kembali jika ada perubahan
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
    except Exception as e:
        print(f'❌ Error processing {filepath}: {e}')
    
    return False

def main():
    """Main function"""
    base_dir = Path('/workspaces/YUKA-sz')
    modules_dir = base_dir / 'PyroUbot' / 'modules'
    helpers_dir = base_dir / 'PyroUbot' / 'core' / 'helpers'
    
    modified_count = 0
    error_count = 0
    
    # Process modules
    print('📝 Processing modules...')
    for py_file in sorted(modules_dir.glob('*.py')):
        if py_file.name.startswith('__'):
            continue
        if process_file(str(py_file)):
            modified_count += 1
            print(f'  ✅ {py_file.name}')
    
    # Process helpers
    print('📝 Processing helpers...')
    for py_file in sorted(helpers_dir.glob('*.py')):
        if py_file.name.startswith('__'):
            continue
        if py_file.name in ['text.py']:  # Skip text.py
            continue
        if process_file(str(py_file)):
            modified_count += 1
            print(f'  ✅ {py_file.name}')
    
    print(f'\n✨ Total files modified: {modified_count}')

if __name__ == '__main__':
    main()
