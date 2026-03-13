#!/usr/bin/env python3
"""
Direct PDF generation test
"""

from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
import os

# Import constants from the refactored version
exec(open('leave_app_refactored.py').read())

def create_test_pdf():
    """Create a test PDF directly"""
    print("Creating test PDF...")
    
    # Create output directory
    os.makedirs('output_pdf', exist_ok=True)
    
    # Test data matching Excel template
    form_data = {
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
            'vacation': True,  # This should be checked
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
    
    # Create PDF
    filename = f"output_pdf/Test_Application_for_Leave_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    c = canvas.Canvas(filename, pagesize=A4)
    
    # Create a mock encoder instance to use the drawing methods
    class MockEncoder:
        def __init__(self):
            self.form_data = form_data
            self.philhealth_logo_var = type('obj', (object,), {'get': lambda: ''})()
            self.bagong_logo_var = type('obj', (object,), {'get': lambda: ''})()
        
        def draw_checkbox(self, c, x, y, is_checked):
            """Draw a checkbox"""
            size = 3*mm
            c.rect(x, y, size, size)
            if is_checked:
                c.line(x, y, x + size, y + size)
                c.line(x, y + size, x + size, y)
        
        def wrap_text(self, text, max_chars):
            """Simple text wrapping"""
            if len(text) <= max_chars:
                return [text]
            return [text[:max_chars], text[max_chars:]]
        
        def truncate_text(self, text, max_chars):
            """Truncate text with ellipsis"""
            if len(text) <= max_chars:
                return text
            return text[:max_chars-3] + "..."
        
        def draw_logo(self, c, logo_path, x, y, max_width, max_height):
            """Placeholder for logo drawing"""
            pass
    
    # Create mock encoder and draw sections
    encoder = MockEncoder()
    
    # Use the methods from the refactored version
    encoder.draw_header_with_logos = lambda c: draw_header_with_logos(encoder, c)
    encoder.draw_section_1 = lambda c: draw_section_1(encoder, c)
    encoder.draw_section_2 = lambda c: draw_section_2(encoder, c)
    
    # Draw the PDF
    encoder.draw_header_with_logos(c)
    encoder.draw_section_1(c)
    encoder.draw_section_2(c)
    
    # Save PDF
    c.save()
    print(f"✅ Test PDF created: {filename}")
    return filename

def draw_header_with_logos(encoder, c):
    """Draw header section matching Excel template exactly"""
    # Reserve header block
    header_y_start = CANVAS_HEIGHT - 30*mm
    
    # Stamp of Date of Receipt box (top right) - matches Excel position
    stamp_x = CANVAS_WIDTH - MARGIN_RIGHT - 50*mm
    stamp_y = header_y_start
    c.rect(stamp_x, stamp_y, 45*mm, 20*mm)
    c.setFont("Helvetica", 8)
    c.drawString(stamp_x + 2*mm, stamp_y + 16*mm, "Stamp of Date of Receipt")
    
    # Form title - matches Excel template exactly
    c.setFont("Helvetica-Bold", 12)
    c.drawCentredString(CANVAS_WIDTH/2, header_y_start - 35*mm, "Civil Service Form No. 6")
    c.setFont("Helvetica", 10)
    c.drawCentredString(CANVAS_WIDTH/2, header_y_start - 40*mm, "Revised 2020")
    
    c.setFont("Helvetica-Bold", 14)
    c.drawCentredString(CANVAS_WIDTH/2, header_y_start - 50*mm, "APPLICATION FOR LEAVE")

def draw_section_1(encoder, c):
    """Draw Section 1: Office/Department and Name - matching Excel template exactly"""
    y_pos = SECTION_1_Y
    
    # Section 1 & 2 headers (same line) - exact Excel positioning
    c.setFont("Helvetica", 9)
    c.drawString(MARGIN_LEFT, y_pos, "1.   OFFICE/DEPARTMENT")
    c.drawString(MARGIN_LEFT + 120*mm, y_pos, "2.  NAME :            (Last)                               (First)                         (Middle)")
    
    # Draw underlines for the fields (matching Excel)
    y_underline = y_pos - 6*mm
    
    # Office/Department underline
    c.line(MARGIN_LEFT + 5*mm, y_underline, MARGIN_LEFT + 100*mm, y_underline)
    
    # Name underlines
    name_x_start = MARGIN_LEFT + 120*mm
    c.line(name_x_start + 20*mm, y_underline, name_x_start + 55*mm, y_underline)  # Last
    c.line(name_x_start + 75*mm, y_underline, name_x_start + 105*mm, y_underline)  # First  
    c.line(name_x_start + 125*mm, y_underline, name_x_start + 155*mm, y_underline)  # Middle
    
    # Data values (positioned above underlines)
    c.setFont("Helvetica", 10)
    c.drawString(MARGIN_LEFT + 5*mm, y_pos - 4*mm, encoder.form_data['office_department'])
    
    # Name values
    c.drawString(name_x_start + 20*mm, y_pos - 4*mm, encoder.form_data['name']['last'])
    c.drawString(name_x_start + 75*mm, y_pos - 4*mm, encoder.form_data['name']['first'])  
    c.drawString(name_x_start + 125*mm, y_pos - 4*mm, encoder.form_data['name']['middle'])

def draw_section_2(encoder, c):
    """Draw Section 2: Date, Position, Salary - matching Excel template exactly"""
    y_pos = SECTION_2_Y
    
    c.setFont("Helvetica", 9)
    
    # Date of Filing with underline
    c.drawString(MARGIN_LEFT, y_pos, "3.   DATE OF FILING  ")
    date_underline_start = MARGIN_LEFT + 45*mm
    c.line(date_underline_start, y_pos - 2*mm, date_underline_start + 40*mm, y_pos - 2*mm)
    
    # Date value
    date_str = encoder.form_data['date_filing'].strftime("%B %d, %Y")
    c.setFont("Helvetica", 10)
    c.drawString(date_underline_start, y_pos - 1*mm, date_str)
    
    # Position with underline
    c.setFont("Helvetica", 9)
    position_x = MARGIN_LEFT + 120*mm
    c.drawString(position_x, y_pos, "4.   POSITION  ")
    pos_underline_start = position_x + 30*mm
    c.line(pos_underline_start, y_pos - 2*mm, pos_underline_start + 50*mm, y_pos - 2*mm)
    
    # Position value
    c.setFont("Helvetica", 10)
    c.drawString(pos_underline_start, y_pos - 1*mm, encoder.form_data['position'])
    
    # Salary with underline
    c.setFont("Helvetica", 9)
    salary_x = MARGIN_LEFT + 200*mm
    c.drawString(salary_x, y_pos, "5.  SALARY  ")
    sal_underline_start = salary_x + 25*mm
    c.line(sal_underline_start, y_pos - 2*mm, sal_underline_start + 30*mm, y_pos - 2*mm)
    
    # Salary value
    c.setFont("Helvetica", 10)
    c.drawString(sal_underline_start, y_pos - 1*mm, encoder.form_data['salary'])

if __name__ == "__main__":
    create_test_pdf()