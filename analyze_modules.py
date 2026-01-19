#!/usr/bin/env python3
"""
Comprehensive analysis of Python modules to find broken/error features
"""

import os
import re
import ast
from pathlib import Path
from collections import defaultdict

class IssueAnalyzer:
    def __init__(self, modules_dir):
        self.modules_dir = modules_dir
        self.issues = defaultdict(list)
        self.file_contents = {}
        self.defined_functions = defaultdict(set)
        self.imported_modules = defaultdict(set)
        
    def analyze(self):
        """Main analysis function"""
        module_files = sorted([f for f in Path(self.modules_dir).glob("*.py") if f.name != "__init__.py"])
        
        # First pass: collect all function definitions and imports
        for file_path in module_files:
            self._collect_definitions(file_path)
        
        # Second pass: analyze each file for issues
        for file_path in module_files:
            self._analyze_file(file_path)
        
        return self.issues
    
    def _collect_definitions(self, file_path):
        """Collect function definitions from file"""
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                self.file_contents[file_path.name] = content
                
            try:
                tree = ast.parse(content)
                for node in ast.walk(tree):
                    if isinstance(node, ast.FunctionDef):
                        self.defined_functions[file_path.name].add(node.name)
                    elif isinstance(node, ast.Import):
                        for alias in node.names:
                            self.imported_modules[file_path.name].add(alias.name)
                    elif isinstance(node, ast.ImportFrom):
                        if node.module:
                            self.imported_modules[file_path.name].add(node.module)
            except SyntaxError:
                pass
        except Exception:
            pass
    
    def _analyze_file(self, file_path):
        """Analyze single file for issues"""
        filename = file_path.name
        content = self.file_contents.get(filename, "")
        lines = content.split('\n')
        
        # Check for syntax errors
        self._check_syntax(filename, content, lines)
        
        # Check for import errors
        self._check_imports(filename, lines)
        
        # Check for API endpoints
        self._check_api_endpoints(filename, lines)
        
        # Check for undefined functions
        self._check_function_calls(filename, lines)
        
        # Check for error handling
        self._check_error_handling(filename, content, lines)
        
        # Check for hardcoded secrets
        self._check_secrets(filename, lines)
        
        # Check for incomplete code
        self._check_incomplete_code(filename, lines)
    
    def _check_syntax(self, filename, content, lines):
        """Check for syntax errors"""
        try:
            ast.parse(content)
        except SyntaxError as e:
            self.issues[filename].append({
                'severity': 'Critical',
                'line': e.lineno or '?',
                'type': 'SyntaxError',
                'description': f"Syntax error: {e.msg}"
            })
    
    def _check_imports(self, filename, lines):
        """Check for import errors"""
        dangerous_patterns = {
            'from unknown_module': 'Unknown module import',
            'import nonexistent': 'Non-existent module import',
        }
        
        # Check for imports of deprecated or missing modules
        for i, line in enumerate(lines, 1):
            # Check for common problematic imports
            if re.match(r'\s*from\s+(\w+)\s+import', line):
                module = re.match(r'\s*from\s+(\w+)\s+import', line).group(1)
                # Check if it looks like a non-existent module
                if module.startswith('http') or module.startswith('urllib'):
                    continue
            
            # Check for specific problematic patterns
            if 'from unknown' in line.lower() or 'import unknown' in line.lower():
                self.issues[filename].append({
                    'severity': 'Critical',
                    'line': i,
                    'type': 'ImportError',
                    'description': f"Import of unknown/non-existent module"
                })
    
    def _check_api_endpoints(self, filename, lines):
        """Check for potentially broken API endpoints"""
        api_patterns = [
            (r'https?://[^\s"\']+api[^\s"\']*', 'API endpoint'),
            (r'https?://[^\s"\']+v\d+[^\s"\']*', 'Versioned API'),
        ]
        
        suspicious_endpoints = [
            'localhost',
            '127.0.0.1',
            'example.com',
            'test.com',
        ]
        
        for i, line in enumerate(lines, 1):
            for pattern, desc in api_patterns:
                matches = re.findall(pattern, line)
                for match in matches:
                    if any(sus in match for sus in suspicious_endpoints):
                        self.issues[filename].append({
                            'severity': 'Medium',
                            'line': i,
                            'type': 'APIError',
                            'description': f"Suspicious API endpoint: {match}"
                        })
    
    def _check_function_calls(self, filename, lines):
        """Check for undefined function calls"""
        content = self.file_contents.get(filename, "")
        try:
            tree = ast.parse(content)
            
            # Get all function definitions in this file
            defined_in_file = self.defined_functions.get(filename, set())
            
            # Find all function calls
            for node in ast.walk(tree):
                if isinstance(node, ast.Call):
                    if isinstance(node.func, ast.Name):
                        func_name = node.func.id
                        # Check common built-ins and imports
                        if not self._is_builtin_or_imported(func_name, filename):
                            if func_name not in defined_in_file:
                                # Check if it's a likely external function
                                line_no = node.lineno
                                # Only report if it looks problematic
                                if func_name.startswith('_') and 'self' not in str(node):
                                    self.issues[filename].append({
                                        'severity': 'Low',
                                        'line': line_no,
                                        'type': 'UndefinedFunction',
                                        'description': f"Possible undefined function: {func_name}()"
                                    })
        except:
            pass
    
    def _is_builtin_or_imported(self, name, filename):
        """Check if name is builtin or imported"""
        builtins = {
            'print', 'len', 'range', 'str', 'int', 'float', 'bool', 'list', 'dict', 'set',
            'tuple', 'open', 'input', 'output', 'map', 'filter', 'sorted', 'enumerate',
            'zip', 'sum', 'min', 'max', 'abs', 'round', 'isinstance', 'issubclass',
            'getattr', 'setattr', 'hasattr', 'callable', 'type', 'object', 'super',
            'classmethod', 'staticmethod', 'property', 'next', 'iter', 'reversed',
            'Exception', 'BaseException', 'KeyError', 'ValueError', 'TypeError',
            'AttributeError', 'IndexError', 'RuntimeError', 'NotImplementedError',
            'any', 'all', 'exec', 'eval', 'compile', 'repr', 'ascii', 'format',
            'bytes', 'bytearray', 'memoryview', 'complex', 'divmod', 'pow',
            'ord', 'chr', 'bin', 'oct', 'hex', 'slice', 'frozenset',
            'globals', 'locals', 'vars', 'dir', 'help', 'id', 'hash',
            'Copyright', 'credits', 'license',
        }
        return name in builtins or name in self.imported_modules.get(filename, set())
    
    def _check_error_handling(self, filename, content, lines):
        """Check for poor error handling"""
        # Check for bare except clauses
        for i, line in enumerate(lines, 1):
            if re.search(r'\s*except\s*:\s*$', line):
                self.issues[filename].append({
                    'severity': 'Medium',
                    'line': i,
                    'type': 'BadErrorHandling',
                    'description': "Bare except clause - catches all exceptions including KeyboardInterrupt"
                })
            
            # Check for except Exception that might hide real issues
            if re.search(r'except\s+Exception\s*:', line):
                # This is actually fine, but let's check what's in the except block
                if i < len(lines) and lines[i].strip() in ['pass', '']:
                    self.issues[filename].append({
                        'severity': 'Medium',
                        'line': i,
                        'type': 'BadErrorHandling',
                        'description': "Exception caught but silently ignored (pass statement)"
                    })
        
        # Check for except blocks with only pass
        for i in range(len(lines)-1):
            if re.search(r'except\s+\w+', lines[i]):
                if i+1 < len(lines) and re.match(r'\s*pass\s*$', lines[i+1]):
                    self.issues[filename].append({
                        'severity': 'Medium',
                        'line': i+1,
                        'type': 'BadErrorHandling',
                        'description': "Silent exception handling - errors are ignored"
                    })
    
    def _check_secrets(self, filename, lines):
        """Check for hardcoded API keys and tokens"""
        secret_patterns = [
            (r'api[_-]?key\s*=\s*["\'][\w\-]{20,}["\']', 'Hardcoded API Key'),
            (r'token\s*=\s*["\'][\w\-]{20,}["\']', 'Hardcoded Token'),
            (r'password\s*=\s*["\'][\w\-]{4,}["\']', 'Hardcoded Password'),
            (r'secret\s*=\s*["\'][\w\-]{20,}["\']', 'Hardcoded Secret'),
            (r'authorization\s*:\s*["\']Bearer\s+[\w\-]+["\']', 'Hardcoded Bearer Token'),
        ]
        
        for i, line in enumerate(lines, 1):
            for pattern, desc in secret_patterns:
                if re.search(pattern, line, re.IGNORECASE):
                    self.issues[filename].append({
                        'severity': 'Critical',
                        'line': i,
                        'type': 'HardcodedSecret',
                        'description': desc
                    })
    
    def _check_incomplete_code(self, filename, lines):
        """Check for incomplete code"""
        for i, line in enumerate(lines, 1):
            # Check for TODO, FIXME, XXX comments
            if re.match(r'\s*#\s*(TODO|FIXME|XXX|HACK|BUG)', line, re.IGNORECASE):
                self.issues[filename].append({
                    'severity': 'Low',
                    'line': i,
                    'type': 'IncompleteCode',
                    'description': f"Incomplete code marker: {line.strip()}"
                })
            
            # Check for ellipsis (...)
            if '...' in line and not line.strip().startswith('#'):
                if 'docstring' not in line.lower() and '"""' not in line and "'''" not in line:
                    self.issues[filename].append({
                        'severity': 'Low',
                        'line': i,
                        'type': 'IncompleteCode',
                        'description': "Ellipsis (...) found - might indicate incomplete code"
                    })
    
    def print_issues(self, issues):
        """Print issues grouped by severity"""
        severity_order = ['Critical', 'High', 'Medium', 'Low']
        
        for severity in severity_order:
            files_with_severity = {}
            for filename, issues_list in issues.items():
                severity_issues = [i for i in issues_list if i['severity'] == severity]
                if severity_issues:
                    files_with_severity[filename] = severity_issues
            
            if not files_with_severity:
                continue
            
            print(f"\n{'='*80}")
            print(f"🔴 {severity.upper()} SEVERITY ISSUES")
            print(f"{'='*80}\n")
            
            for filename in sorted(files_with_severity.keys()):
                file_issues = files_with_severity[filename]
                if file_issues:
                    print(f"📄 {filename}")
                    for issue in file_issues:
                        print(f"   ├─ Line {issue['line']}: [{issue['type']}]")
                        print(f"   └─ {issue['description']}")
                    print()

def main():
    modules_dir = "/workspaces/YUKA-sz/PyroUbot/modules"
    analyzer = IssueAnalyzer(modules_dir)
    issues = analyzer.analyze()
    analyzer.print_issues(issues)
    
    # Print summary
    total_issues = sum(len(v) for v in issues.values())
    print(f"\n{'='*80}")
    print(f"📊 SUMMARY")
    print(f"{'='*80}")
    print(f"Total files with issues: {len(issues)}")
    print(f"Total issues found: {total_issues}")

if __name__ == "__main__":
    main()
