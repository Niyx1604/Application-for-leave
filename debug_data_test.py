#!/usr/bin/env python3
"""
Debug test to check form data population
"""

import tkinter as tk
from datetime import datetime
import os

def debug_form_data():
    """Debug the form data to see what's being populated"""
    print("=== DEBUGGING FORM DATA ===")
    
    # Create a hidden root window
    root = tk.Tk()
    root.withdraw()
    
    try:
        # Import and create the application
        with open('leave_app_refactored.py', 'r', encoding='utf-8') as f:
            code = f.read()
        exec(code, globals())
        app = LeaveApplicationEncoder(root)
        
        # Set test data
        test_data = {
            'office_department': 'LHIO - Digos',
            'name': {
                'last': 'Mendoza',
                'first': 'Anthony',
                'middle': 'Berja'
            },
            'date_filing': datetime(2025, 3, 13),
            'position': 'Administrative Aide VI',
            'salary': '25000',
            'leave_types': {
                'vacation': True,
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
                'start': datetime(2025, 3, 15),
                'end': datetime(2025, 3, 16)
            },
            'working_days': 2,
            'commutation': {
                'not_requested': True,
                'requested': False
            }
        }
        
        # Set the form data
        app.form_data = test_data
        
        print("✅ Form data set successfully")
        print("\n📋 Data contents:")
        print(f"Office/Department: '{app.form_data['office_department']}'")
        print(f"Last Name: '{app.form_data['name']['last']}'")
        print(f"First Name: '{app.form_data['name']['first']}'")
        print(f"Middle Name: '{app.form_data['name']['middle']}'")
        print(f"Date Filing: {app.form_data['date_filing']}")
        print(f"Position: '{app.form_data['position']}'")
        print(f"Salary: '{app.form_data['salary']}'")
        print(f"Vacation Leave: {app.form_data['leave_types']['vacation']}")
        
        # Generate PDF
        print("\n🔄 Generating PDF...")
        app.generate_pdf()
        print("✅ PDF generated")
        
        return True
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        return False
    finally:
        root.destroy()

if __name__ == "__main__":
    debug_form_data()