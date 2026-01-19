#!/usr/bin/env python3
"""
Script untuk menambahkan <blockquote> ke semua pesan yang belum memilikinya
"""
import os
import re
from pathlib import Path

def add_blockquote_to_file(filepath):
    """Tambahkan blockquote ke file jika belum ada"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    modified = False
    original_content = content
    
    # 1. Fix __HELP__ strings
    def fix_help(match):
        nonlocal modified
        prefix = match.group(1)
        quote_type = match.group(2)
        help_content = match.group(3)
        
        # Cek apakah sudah ada blockquote
        if '<blockquote>' in help_content:
            return match.group(0)
        
        # Jika kosong, skip
        if not help_content.strip():
            return match.group(0)
        
        modified = True
        # Tambahkan blockquote
        help_content = help_content.strip()
        if not help_content.startswith('<blockquote>'):
            help_content = '<blockquote>' + help_content
        if not help_content.endswith('</blockquote>'):
            help_content = help_content + '</blockquote>'
        
        return f'{prefix}__HELP__{quote_type} {quote_type}{help_content}{quote_type}'
    
    # Pattern untuk __HELP__ = """...""" atau __HELP__ = '''...'''
    pattern = r'(__MODULE__\s*=\s*["\'][^"\']*["\'][\s\n]*)?__HELP__\s*=\s*("""|\'\'\'|f""")(.*?)\2'
    content = re.sub(pattern, fix_help, content, flags=re.DOTALL)
    
    # 2. Fix message.reply() tanpa blockquote
    def fix_message_reply(match):
        nonlocal modified
        prefix = match.group(1)
        msg_content = match.group(2)
        
        # Cek apakah sudah ada blockquote
        if '<blockquote>' in msg_content:
            return match.group(0)
        
        modified = True
        msg_content = msg_content.strip()
        if not msg_content.startswith('<blockquote>'):
            msg_content = '<blockquote>' + msg_content
        if not msg_content.endswith('</blockquote>'):
            msg_content = msg_content + '</blockquote>'
        
        return f'{prefix}"{msg_content}"'
    
    # Pola untuk reply dengan pesan string
    pattern_reply = r'(\.reply\s*\(\s*)(f?["\'](?:<[^>]+>)?.*?(?:</[^>]+>)?["\'])'
    content = re.sub(pattern_reply, fix_message_reply, content, flags=re.DOTALL | re.MULTILINE)
    
    if modified and content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    
    return False

def process_directory(directory):
    """Process semua file Python dalam direktori"""
    modules_dir = Path(directory) / 'PyroUbot' / 'modules'
    helpers_dir = Path(directory) / 'PyroUbot' / 'core' / 'helpers'
    
    modified_files = []
    
    for py_file in modules_dir.glob('*.py'):
        if add_blockquote_to_file(str(py_file)):
            modified_files.append(str(py_file))
            print(f'✅ Modified: {py_file.name}')
    
    for py_file in helpers_dir.glob('*.py'):
        if py_file.name == 'text.py':  # Skip text.py karena sudah di-handle manual
            continue
        if add_blockquote_to_file(str(py_file)):
            modified_files.append(str(py_file))
            print(f'✅ Modified: {py_file.name}')
    
    print(f'\n📊 Total files modified: {len(modified_files)}')
    return modified_files

if __name__ == '__main__':
    process_directory('/workspaces/YUKA-sz')
    print('\n✨ Selesai! Semua pesan sudah menggunakan blockquote.')
