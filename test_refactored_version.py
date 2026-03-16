#!/usr/bin/env python3
"""
Test the refactored version to identify the actual header issues
"""

import tkinter as tk
from leave_app_refactored import LeaveApplicationEncoder
import os

def test_refactored_pdf():
    """Generate PDF using the refactored version"""
    
    # Create tkinter root (required for the app)
    root = tk.Tk()
    root.withdraw()  # Hide the window
    
    try:
        # Create the app
        app = LeaveApplicationEncoder(root)
        
        # Set some test data
        app.name_last_var.set("Mendoza")
        app.name_first_var.set("Anthony")
        app.name_middle_var.set("Berja")
        app.position_var.set("Administrative Aide VI")
        app.working_days_var.set("1 day")
        app.leave_vars['vacation'].set(True)  # Select vacation leave
        
        # Generate PDF
        print("Generating PDF with refactored version...")
        app.generate_pdf()
        
        # List generated PDFs
        if os.path.exists("output_pdf"):
            files = os.listdir("output_pdf")
            pdf_files = [f for f in files if f.endswith('.pdf')]
            if pdf_files:
                latest_pdf = sorted(pdf_files)[-1]
                pdf_path = os.path.join("output_pdf", latest_pdf)
                print(f"✅ PDF generated: {pdf_path}")
                return pdf_path
            else:
                print("❌ No PDF files found in output_pdf/")
        else:
            print("❌ output_pdf directory not found")
            
    except Exception as e:
        print(f"❌ Error generating PDF: {e}")
        import traceback
        traceback.print_exc()
        return None
        
    finally:
        root.destroy()

if __name__ == "__main__":
    test_refactored_pdf()