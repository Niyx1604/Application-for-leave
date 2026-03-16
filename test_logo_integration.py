#!/usr/bin/env python3
"""
Test to verify logo integration is working
"""

import tempfile
import os
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from unittest.mock import Mock
import sys

# Import the fixed version
sys.path.insert(0, '.')
from leave_app_complete import LeaveApplicationEncoder

def test_logo_integration():
    """Test that logos are being drawn in the header"""
    
    # Create temporary PDF
    temp_dir = tempfile.mkdtemp()
    test_pdf_path = os.path.join(temp_dir, "test_logo.pdf")
    
    try:
        # Create mock app instance
        app = Mock()
        app.draw_pdf_header = LeaveApplicationEncoder.draw_pdf_header.__get__(app, LeaveApplicationEncoder)
        app.draw_logo = LeaveApplicationEncoder.draw_logo.__get__(app, LeaveApplicationEncoder)
        
        # Create canvas
        c = canvas.Canvas(test_pdf_path, pagesize=A4)
        width, height = A4
        
        # Track drawImage calls
        logo_calls = []
        original_drawImage = c.drawImage
        
        def track_logo_calls(image_path, x, y, width=None, height=None, mask=None):
            logo_calls.append({
                'image_path': str(image_path),
                'x': x,
                'y': y,
                'width': width,
                'height': height
            })
            print(f"Logo drawn: {os.path.basename(image_path)} at ({x:.1f}, {y:.1f})")
            return original_drawImage(image_path, x, y, width, height, mask)
        
        c.drawImage = track_logo_calls
        
        # Call header drawing
        print("Testing logo integration...")
        final_y = app.draw_pdf_header(c, width, height)
        c.save()
        
        print(f"\nCaptured {len(logo_calls)} logo drawing calls:")
        for i, call in enumerate(logo_calls):
            print(f"  {i+1}: {os.path.basename(call['image_path'])} at ({call['x']:.1f}, {call['y']:.1f})")
        
        # Check for expected logos
        philhealth_logos = [call for call in logo_calls if 'philhealth' in call['image_path'].lower()]
        bagong_logos = [call for call in logo_calls if 'bagong' in call['image_path'].lower()]
        
        if philhealth_logos:
            print("✅ PhilHealth logo integration working")
        else:
            print("❌ PhilHealth logo not found")
            
        if bagong_logos:
            print("✅ Bagong Pilipinas logo integration working")
        else:
            print("❌ Bagong Pilipinas logo not found")
            
        return len(logo_calls) > 0
            
    except Exception as e:
        print(f"❌ Error testing logos: {e}")
        return False
        
    finally:
        # Cleanup
        if os.path.exists(test_pdf_path):
            os.remove(test_pdf_path)
        os.rmdir(temp_dir)

if __name__ == "__main__":
    test_logo_integration()