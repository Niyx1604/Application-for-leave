#!/usr/bin/env python3
"""
Test actual PDF generation to see the real output
"""

import tkinter as tk
from leave_app_complete import LeaveApplicationEncoder
import os

def test_pdf_generation():
    """Generate an actual PDF to see the current output"""
    
    # Create tkinter root (required for the app)
    root = tk.Tk()
    root.withdraw()  # Hide the window
    
    try:
        # Create the app
        app = LeaveApplicationEncoder(root)
        
        # Set some test data
        app.name_var.set("Test User")
        app.position_var.set("Administrative Aide I")
        app.working_days_var.set("1 day")
        
        # Generate PDF
        print("Generating PDF...")
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
        return None
        
    finally:
        root.destroy()

if __name__ == "__main__":
    test_pdf_generation()