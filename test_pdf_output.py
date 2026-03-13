#!/usr/bin/env python3
"""
Test script to generate PDF output from the refactored version
"""

import tkinter as tk
from datetime import datetime
import sys
import os

# Import the refactored application
exec(open('leave_app_refactored.py').read())

def test_pdf_generation():
    """Generate a test PDF to compare with Excel template"""
    print("Testing PDF generation...")
    
    # Create a root window (hidden)
    root = tk.Tk()
    root.withdraw()  # Hide the window
    
    # Create the application instance
    app = LeaveApplicationEncoder(root)
    
    # Set test data matching the Excel template
    app.form_data = {
        'office_department': 'LHIO - Digos',
        'name': {
            'last': 'Mendoza',
            'first': 'Anthony',
            'middle': 'Berja'
        },
        'date_filing': datetime(2025, 10, 14),
        'position': 'Administrative Aide VI',
        'salary': '25000',
        'leave_types': {
            'vacation': True,  # Checked in Excel
            'mandatory': False,
            'sick': False,
            'maternity': False,
            'paternity': False,
            'special_privilege': False,
            'solo_parent': False,
            'study': False,
            'vawc_10day': False,
            'rehabilitation': False,
            'special_women': False,
            'special_emergency': False,
            'adoption': False
        },
        'inclusive_dates': {
            'start': datetime(2025, 10, 29),
            'end': datetime(2025, 10, 30)
        },
        'working_days': 2,
        'commutation': {
            'not_requested': True,
            'requested': False
        }
    }
    
    # Generate PDF
    try:
        app.generate_pdf()
        print("✅ PDF generated successfully!")
        print("Check the output_pdf/ directory for the generated file.")
        return True
    except Exception as e:
        print(f"❌ Error generating PDF: {e}")
        return False
    finally:
        root.destroy()

if __name__ == "__main__":
    test_pdf_generation()