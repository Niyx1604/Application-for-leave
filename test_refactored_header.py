#!/usr/bin/env python3
"""
Test the refactored version header to identify issues
"""

import tempfile
import os
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from unittest.mock import Mock
import sys

# Import the refactored version
sys.path.insert(0, '.')
from leave_app_refactored import LeaveApplicationEncoder

def test_refactored_header():
    """Test the refactored header for issues"""
    
    # Create temporary PDF
    temp_dir = tempfile.mkdtemp()
    test_pdf_path = os.path.join(temp_dir, "test_refactored_header.pdf")
    
    try:
        # Create mock app instance
        app = Mock()
        app.draw_header_with_logos = LeaveApplicationEncoder.draw_header_with_logos.__get__(app, LeaveApplicationEncoder)
        app.draw_logo = LeaveApplicationEncoder.draw_logo.__get__(app, LeaveApplicationEncoder)
        app.philhealth_logo_var = Mock()
        app.philhealth_logo_var.get.return_value = "logos/philhealth_logo.png"
        app.bagong_logo_var = Mock()
        app.bagong_logo_var.get.return_value = "logos/bagong_pilipinas_logo.png"
        
        # Create canvas
        c = canvas.Canvas(test_pdf_path, pagesize=A4)
        width, height = A4
        
        # Track Y coordinates and logo calls
        y_coordinates = []
        logo_calls = []
        
        original_drawCentredString = c.drawCentredString
        original_drawImage = c.drawImage
        
        def track_y_coords(x, y, text):
            y_coordinates.append(y)
            print(f"Text: '{text}' at Y: {y:.1f}")
            return original_drawCentredString(x, y, text)
        
        def track_logo_calls(image_path, x, y, width=None, height=None, mask=None):
            logo_calls.append({
                'image_path': str(image_path),
                'x': x,
                'y': y,
                'width': width,
                'height': height
            })
            print(f"Logo: {os.path.basename(image_path)} at ({x:.1f}, {y:.1f})")
            return original_drawImage(image_path, x, y, width, height, mask)
        
        c.drawCentredString = track_y_coords
        c.drawImage = track_logo_calls
        
        # Call header drawing
        print("Testing refactored header...")
        app.draw_header_with_logos(c)
        c.save()
        
        print(f"\nCaptured {len(y_coordinates)} Y coordinates:")
        for i, y in enumerate(y_coordinates):
            print(f"  {i+1}: {y:.1f}")
        
        print(f"\nCaptured {len(logo_calls)} logo calls:")
        for i, call in enumerate(logo_calls):
            print(f"  {i+1}: {os.path.basename(call['image_path'])} at ({call['x']:.1f}, {call['y']:.1f})")
        
        # Check for overlaps
        unique_y = set(y_coordinates)
        if len(unique_y) < len(y_coordinates):
            print(f"\n❌ BUG CONFIRMED: Text overlap detected!")
            print(f"   {len(y_coordinates)} text elements but only {len(unique_y)} unique Y positions")
            return False
        else:
            print(f"\n✅ No text overlap - {len(unique_y)} unique positions")
            
        # Check logo integration
        if len(logo_calls) > 0:
            print(f"✅ Logo integration working - {len(logo_calls)} logos drawn")
        else:
            print(f"❌ No logos drawn")
            
        return True
            
    except Exception as e:
        print(f"❌ Error testing refactored header: {e}")
        import traceback
        traceback.print_exc()
        return False
        
    finally:
        # Cleanup
        if os.path.exists(test_pdf_path):
            os.remove(test_pdf_path)
        os.rmdir(temp_dir)

if __name__ == "__main__":
    test_refactored_header()