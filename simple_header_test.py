#!/usr/bin/env python3
"""
Simple test to verify the PDF header bug exists
"""

import tempfile
import os
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from unittest.mock import Mock
import sys

# Import the unfixed version
sys.path.insert(0, '.')
from leave_app_complete import LeaveApplicationEncoder

def test_header_bug():
    """Simple test to show the header bug exists"""
    
    # Create temporary PDF
    temp_dir = tempfile.mkdtemp()
    test_pdf_path = os.path.join(temp_dir, "test_header.pdf")
    
    try:
        # Create mock app instance
        app = Mock()
        app.draw_pdf_header = LeaveApplicationEncoder.draw_pdf_header.__get__(app, LeaveApplicationEncoder)
        
        # Create canvas
        c = canvas.Canvas(test_pdf_path, pagesize=A4)
        width, height = A4
        
        # Track Y coordinates
        y_coordinates = []
        original_drawCentredString = c.drawCentredString
        
        def track_y_coords(x, y, text):
            y_coordinates.append(y)
            print(f"Text: '{text}' at Y: {y:.1f}")
            return original_drawCentredString(x, y, text)
        
        c.drawCentredString = track_y_coords
        
        # Call header drawing
        print("Calling draw_pdf_header...")
        final_y = app.draw_pdf_header(c, width, height)
        c.save()
        
        print(f"\nCaptured {len(y_coordinates)} Y coordinates:")
        for i, y in enumerate(y_coordinates):
            print(f"  {i+1}: {y:.1f}")
        
        # Check for overlaps
        unique_y = set(y_coordinates)
        if len(unique_y) < len(y_coordinates):
            print(f"\n❌ BUG CONFIRMED: Text overlap detected!")
            print(f"   {len(y_coordinates)} text elements but only {len(unique_y)} unique Y positions")
            return False
        else:
            print(f"\n✅ No overlap detected - {len(unique_y)} unique positions")
            return True
            
    finally:
        # Cleanup
        if os.path.exists(test_pdf_path):
            os.remove(test_pdf_path)
        os.rmdir(temp_dir)

if __name__ == "__main__":
    print("Testing PDF header for Y-axis overlap bug...")
    test_header_bug()