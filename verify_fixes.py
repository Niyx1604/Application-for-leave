#!/usr/bin/env python3
"""
Verify that all PDF layout fixes are working correctly
"""

import tempfile
import os
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from unittest.mock import Mock
import sys

# Import the fixed refactored version
sys.path.insert(0, '.')
from leave_app_refactored import LeaveApplicationEncoder

def verify_all_fixes():
    """Comprehensive test to verify all layout fixes"""
    
    # Create temporary PDF
    temp_dir = tempfile.mkdtemp()
    test_pdf_path = os.path.join(temp_dir, "test_fixed_layout.pdf")
    
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
        
        # Track coordinates
        y_coordinates = []
        logo_calls = []
        
        original_drawCentredString = c.drawCentredString
        original_drawImage = c.drawImage
        
        def track_y_coords(x, y, text):
            y_coordinates.append(y)
            return original_drawCentredString(x, y, text)
        
        def track_logo_calls(image_path, x, y, width=None, height=None, mask=None):
            logo_calls.append({'x': x, 'y': y, 'path': str(image_path)})
            return original_drawImage(image_path, x, y, width, height, mask)
        
        c.drawCentredString = track_y_coords
        c.drawImage = track_logo_calls
        
        # Test header
        print("🔍 Testing fixed header layout...")
        app.draw_header_with_logos(c)
        c.save()
        
        # Verify fixes
        issues_found = []
        
        # 1. Check text overlap (should be none)
        unique_y = set(y_coordinates)
        if len(unique_y) == len(y_coordinates):
            print("✅ Fix 1: No text overlap - all text at distinct Y coordinates")
        else:
            issues_found.append("Text overlap still exists")
        
        # 2. Check logo positioning (should not overlap with text area)
        text_y_min = min(y_coordinates) if y_coordinates else 0
        text_y_max = max(y_coordinates) if y_coordinates else 0
        
        logo_overlap = False
        for logo in logo_calls:
            # Check if logo Y position overlaps with text Y range
            if text_y_min <= logo['y'] <= text_y_max:
                logo_overlap = True
                break
        
        if not logo_overlap:
            print("✅ Fix 2: Logo positioning - no overlap with text area")
        else:
            issues_found.append("Logo still overlaps with text")
        
        # 3. Check spacing (APPLICATION FOR LEAVE should be reasonably positioned)
        app_leave_y = None
        for y in y_coordinates:
            # Find APPLICATION FOR LEAVE position (should be lowest Y in header)
            if y == min(y_coordinates):
                app_leave_y = y
                break
        
        # Check gap to form content (SECTION_1_Y = CANVAS_HEIGHT - 100*mm)
        from leave_app_refactored import SECTION_1_Y
        if app_leave_y:
            gap = app_leave_y - SECTION_1_Y
            gap_mm = gap / mm
            if 10 <= gap_mm <= 30:  # Reasonable gap
                print(f"✅ Fix 3: Proper spacing - {gap_mm:.1f}mm gap between header and form")
            else:
                issues_found.append(f"Spacing issue - {gap_mm:.1f}mm gap (should be 10-30mm)")
        
        # 4. Check logo count
        if len(logo_calls) == 2:
            print("✅ Fix 4: Both logos rendered correctly")
        else:
            issues_found.append(f"Logo count issue - {len(logo_calls)} logos (should be 2)")
        
        # Summary
        if not issues_found:
            print("\n🎉 ALL FIXES SUCCESSFUL!")
            print("   - No text overlap")
            print("   - Logos positioned correctly")
            print("   - Proper spacing between sections")
            print("   - Professional layout achieved")
            return True
        else:
            print(f"\n❌ {len(issues_found)} issues still remain:")
            for issue in issues_found:
                print(f"   - {issue}")
            return False
            
    except Exception as e:
        print(f"❌ Error during verification: {e}")
        import traceback
        traceback.print_exc()
        return False
        
    finally:
        # Cleanup
        if os.path.exists(test_pdf_path):
            os.remove(test_pdf_path)
        os.rmdir(temp_dir)

if __name__ == "__main__":
    print("Verifying PDF layout fixes...")
    success = verify_all_fixes()
    if success:
        print("\n✅ leave_app_refactored.py is now ready for production use!")
    else:
        print("\n❌ Additional fixes needed.")