#!/usr/bin/env python3
"""
Advanced analysis for import errors and API issues
"""

import os
import re
from pathlib import Path
from collections import defaultdict

class AdvancedAnalyzer:
    def __init__(self, modules_dir):
        self.modules_dir = modules_dir
        self.issues = defaultdict(list)
        
    def analyze(self):
        """Main analysis for API and import issues"""
        module_files = sorted([f for f in Path(self.modules_dir).glob("*.py") if f.name != "__init__.py"])
        
        for file_path in module_files:
            self._analyze_imports_and_api(file_path)
    
    def _analyze_imports_and_api(self, file_path):
        """Analyze imports and API endpoints in detail"""
        filename = file_path.name
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                lines = content.split('\n')
        except Exception:
            return
        
        # Known problematic API endpoints
        problematic_apis = {
            'instagram-downloader-download-instagram-videos-stories.p.rapidapi.com': 'Instagram API might require valid subscription',
            'api.bing.com': 'Bing API endpoint might be deprecated',
            'gateway.okeconnect.com': 'OKE payment gateway - requires valid API key',
            'localhost': 'Test endpoint - will not work in production',
            'example.com': 'Placeholder domain - not functional',
        }
        
        # Check for API keys and tokens with patterns
        api_key_patterns = {
            'RAPIDAPI_KEY': 'RapidAPI Key hardcoded',
            'API_KEY': 'Generic API key hardcoded',
            'MERCHANT_ID': 'Merchant ID hardcoded',
            'CODE_QR': 'QR code data hardcoded',
            'authorization': 'Authorization token hardcoded',
        }
        
        # Check for deprecated imports
        deprecated_modules = {
            'requests': 'Should check version compatibility',
            'PIL': 'Image library - should verify installation',
            'cv2': 'OpenCV - requires system dependencies',
            'bs4': 'BeautifulSoup - check if installed',
        }
        
        for i, line in enumerate(lines, 1):
            # Check for API endpoints
            for api_domain, issue_desc in problematic_apis.items():
                if api_domain in line:
                    self.issues[filename].append({
                        'severity': 'High',
                        'line': i,
                        'type': 'APIEndpoint',
                        'description': f"API: {issue_desc}"
                    })
            
            # Check for hardcoded secrets
            for secret_name in api_key_patterns.keys():
                if re.search(rf'{secret_name}\s*=\s*["\']', line):
                    # Extract the value
                    match = re.search(rf'{secret_name}\s*=\s*["\']([^"\']+)["\']', line)
                    if match:
                        value = match.group(1)
                        if len(value) > 10 and value not in ['placeholder', 'your_key_here']:
                            self.issues[filename].append({
                                'severity': 'Critical',
                                'line': i,
                                'type': 'HardcodedSecret',
                                'description': f"Exposed {secret_name}: {value[:20]}..."
                            })
            
            # Check for deprecated imports
            if re.match(r'\s*import\s+(\w+)', line) or re.match(r'\s*from\s+(\w+)', line):
                for module in deprecated_modules.keys():
                    if module in line:
                        self.issues[filename].append({
                            'severity': 'Medium',
                            'line': i,
                            'type': 'DeprecatedModule',
                            'description': f"Module '{module}' imported - {deprecated_modules[module]}"
                        })

def main():
    modules_dir = "/workspaces/YUKA-sz/PyroUbot/modules"
    analyzer = AdvancedAnalyzer(modules_dir)
    analyzer.analyze()
    
    print("\n" + "="*80)
    print("🔍 DETAILED API AND IMPORT ANALYSIS")
    print("="*80 + "\n")
    
    severity_order = ['Critical', 'High', 'Medium', 'Low']
    
    for severity in severity_order:
        files_with_severity = {}
        for filename, issues_list in analyzer.issues.items():
            severity_issues = [i for i in issues_list if i['severity'] == severity]
            if severity_issues:
                files_with_severity[filename] = severity_issues
        
        if not files_with_severity:
            continue
        
        print(f"\n{'─'*80}")
        print(f"{severity.upper()} SEVERITY")
        print(f"{'─'*80}\n")
        
        for filename in sorted(files_with_severity.keys()):
            file_issues = files_with_severity[filename]
            print(f"📄 {filename}")
            for issue in file_issues:
                print(f"   • Line {issue['line']}: [{issue['type']}]")
                print(f"     └─ {issue['description']}\n")

if __name__ == "__main__":
    main()
