#!/usr/bin/env python
"""
Check for version collisions between multiple requirements.txt files.
"""
import glob
import sys
import re
from pathlib import Path
from collections import defaultdict

def parse_requirement_line(line):
    """Parse a requirement line and return (package, version)."""
    line = line.strip()
    if not line or line.startswith('#'):
        return None, None
    
    # Handle different formats: pkg==version, pkg>=version, etc.
    match = re.match(r'^([a-zA-Z0-9_.-]+)\s*([>=<~!]+)\s*([^;]+)', line)
    if match:
        package = match.group(1).lower()  # Package names are case-insensitive
        operator = match.group(2)
        version = match.group(3).strip()
        return package, f"{operator}{version}"
    
    return None, None

def check_collisions(requirement_files):
    """Check for version collisions across multiple requirements files."""
    package_versions = defaultdict(dict)  # {package: {file: version}}
    
    # Parse all files
    for file_path in requirement_files:
        if not Path(file_path).exists():
            print(f"Warning: {file_path} not found", file=sys.stderr)
            continue
            
        with open(file_path, 'r') as f:
            for line_num, line in enumerate(f, 1):
                package, version = parse_requirement_line(line)
                if package and version:
                    package_versions[package][file_path] = {
                        'version': version,
                        'line': line_num,
                        'raw_line': line.strip()
                    }
    
    # Check for collisions
    collisions = []
    for package, file_versions in package_versions.items():
        if len(file_versions) > 1:
            versions = set(info['version'] for info in file_versions.values())
            if len(versions) > 1:
                collisions.append((package, file_versions))
    
    return collisions

def main():
    # requirement_files = sys.argv[1:]
    requirement_files = glob.glob("*/requirements.txt")
    collisions = check_collisions(requirement_files)
    
    if not collisions:
        print("No version collisions found!")
        return
    
    print(f"Found {len(collisions)} version collision(s):\n")
    
    for package, file_versions in collisions:
        print(f"Package: {package}")
        for file_path, info in file_versions.items():
            print(f"  {file_path}:{info['line']} -> {info['version']}")
            print(f"    {info['raw_line']}")
        print()

if __name__ == "__main__":
    main()
