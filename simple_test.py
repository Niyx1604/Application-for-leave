#!/usr/bin/env python3
"""
Simple test to check the refactored version
"""

import sys
import os

def test_import():
    """Test if the refactored version can be imported"""
    try:
        # Check if file exists
        if not os.path.exists('leave_app_refactored.py'):
            print("❌ leave_app_refactored.py not found")
            return False
        
        print("✅ File exists")
        
        # Try to read and compile
        with open('leave_app_refactored.py', 'r') as f:
            code = f.read()
        
        compile(code, 'leave_app_refactored.py', 'exec')
        print("✅ Syntax is valid")
        
        return True
        
    except SyntaxError as e:
        print(f"❌ Syntax Error: {e}")
        print(f"Line {e.lineno}: {e.text}")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    test_import()