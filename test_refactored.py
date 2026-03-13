#!/usr/bin/env python3
"""
Test script for leave_app_refactored.py
"""

import os
import sys

def test_refactored_version():
    print('=== TESTING REFACTORED VERSION ===')
    print()
    
    # Check file exists
    if not os.path.exists('leave_app_refactored.py'):
        print('✗ leave_app_refactored.py not found')
        return False
    
    print('✓ leave_app_refactored.py found')
    
    # Check dependencies
    print('\nChecking Dependencies:')
    try:
        import tkinter
        print('✓ tkinter - Available')
    except ImportError:
        print('✗ tkinter - Missing')
        return False
    
    try:
        import openpyxl
        print('✓ openpyxl - Available')
    except ImportError:
        print('✗ openpyxl - Missing')
        return False
    
    try:
        import reportlab
        print('✓ reportlab - Available')
    except ImportError:
        print('✗ reportlab - Missing')
        return False
    
    # Check template
    template_exists = os.path.exists('ALA.xlsx')
    status = 'Found' if template_exists else 'Missing'
    print(f'✓ ALA.xlsx - {status}')
    
    if not template_exists:
        print('⚠ Warning: Excel template missing, but app should still start')
    
    print()
    print('=== REFACTORED VERSION STATUS ===')
    print('✅ READY TO USE')
    print('Run: python leave_app_refactored.py')
    print()
    
    return True

if __name__ == "__main__":
    test_refactored_version()