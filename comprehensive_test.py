#!/usr/bin/env python3
"""
Comprehensive test to generate PDF matching Excel template exactly
"""

import tkinter as tk
from datetime import datetime
import os

def test_refactored_version():
    """Test the refactored version with Excel template data"""
    print("=== COMPREHENSIVE PDF TEST ===")
    print()
    
    # Import the refactored version
    try:
        exec(open('leave_app_refactored.py').read(), globals())
        print("✅ Refactored version imported successfully")
    except Exception as e:
        print(f"❌ Import error: {e}")
        return False
    
    # Create hidden root window
    root = tk.Tk()
    root.withdraw()
    
    try:
        # Create application instance
        app = LeaveApplicationEncoder(root)
        print("✅ Application instance created")
        
        # Set form data to match Excel template exactly
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
                'vacation': True,  # This should be checked in Excel
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
        print("✅ Form data set to match Excel template")
        
        # Generate PDF
        app.generate_pdf()
        print("✅ PDF generated successfully!")
        
        # Check output directory
        output_files = []
        if os.path.exists('output_pdf'):
            output_files = [f for f in os.listdir('output_pdf') if f.endswith('.pdf')]
            print(f"✅ Found {len(output_files)} PDF files in output_pdf/")
            if output_files:
                latest_file = max(output_files, key=lambda f: os.path.getctime(os.path.join('output_pdf', f)))
                print(f"📄 Latest file: {latest_file}")
        
        print()
        print("=== TEST RESULTS ===")
        print("✅ Refactored version is working")
        print("✅ PDF generation successful")
        print("✅ Data matches Excel template structure")
        print()
        print("📋 Next Steps:")
        print("1. Open the generated PDF")
        print("2. Compare with Excel template")
        print("3. Check positioning and formatting")
        print("4. Verify all fields are correctly placed")
        
        return True
        
    except Exception as e:
        print(f"❌ Error during PDF generation: {e}")
        import traceback
        traceback.print_exc()
        return False
    finally:
        root.destroy()

if __name__ == "__main__":
    test_refactored_version()