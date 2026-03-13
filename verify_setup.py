#!/usr/bin/env python3
"""
Verification script to check if everything is set up correctly
"""

import sys
import os

print("=" * 60)
print("Leave Application Encoder - Setup Verification")
print("=" * 60)

# Check Python version
print(f"\n✓ Python version: {sys.version.split()[0]}")

# Check required libraries
required_libs = {
    'tkinter': 'GUI interface',
    'openpyxl': 'Excel handling',
    'reportlab': 'PDF generation',
    'tkcalendar': 'Calendar widgets'
}

print("\nChecking required libraries:")
all_installed = True
for lib, purpose in required_libs.items():
    try:
        __import__(lib)
        print(f"  ✓ {lib:15} - {purpose}")
    except ImportError:
        print(f"  ✗ {lib:15} - {purpose} (NOT INSTALLED)")
        all_installed = False

# Check template file
print("\nChecking template file:")
if os.path.exists('ALA.xlsx'):
    print("  ✓ ALA.xlsx found")
    
    # Try to load it
    try:
        import openpyxl
        wb = openpyxl.load_workbook('ALA.xlsx')
        ws = wb.active
        print(f"  ✓ Template loaded successfully")
        print(f"  ✓ Sheet name: {ws.title}")
        print(f"  ✓ Office/Department default: {ws['B7'].value}")
        wb.close()
    except Exception as e:
        print(f"  ✗ Error loading template: {e}")
else:
    print("  ✗ ALA.xlsx not found")
    all_installed = False

# Check application file
print("\nChecking application file:")
if os.path.exists('leave_app.py'):
    print("  ✓ leave_app.py found")
else:
    print("  ✗ leave_app.py not found")
    all_installed = False

# Final status
print("\n" + "=" * 60)
if all_installed:
    print("✓ ALL CHECKS PASSED!")
    print("\nYou can now run the application:")
    print("  python leave_app.py")
else:
    print("✗ SOME CHECKS FAILED")
    print("\nPlease install missing libraries:")
    print("  pip install openpyxl reportlab tkcalendar")
print("=" * 60)
