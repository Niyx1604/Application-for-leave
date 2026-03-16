#!/usr/bin/env python3
"""
Simple PDF test without GUI
"""

from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
import os

# Constants
CANVAS_WIDTH = A4[0]
CANVAS_HEIGHT = A4[1]
MARGIN_LEFT = 20*mm
MARGIN_RIGHT = 20*mm

# Section positions
SECTION_1_Y = CANVAS_HEIGHT - 200*mm

def create_test_pdf():
    """Create a test PDF with proper data"""
    print("Creating test PDF...")
    
    # Test data
    form_data = {
        'office_department': 'LHIO - Digos',
        'name': {
            'last': 'Mendoza',
            'first': 'Anthony',
            'middle': 'Berja'
        },
        'date_filing': datetime(2025, 3, 13),
        'position': 'Administrative Aide VI',
        'salary': '25000'
    }
    
    # Create output directory
    os.makedirs('output_pdf', exist_ok=True)
    
    # Create PDF
    filename = f"output_pdf/Debug_Test_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    c = canvas.Canvas(filename, pagesize=A4)
    
    # Draw header
    c.setFont("Helvetica-Bold", 14)
    c.drawCentredString(CANVAS_WIDTH/2, CANVAS_HEIGHT - 50*mm, "APPLICATION FOR LEAVE")
    
    # Draw section 1-5 table
    y_pos = SECTION_1_Y
    table_width = CANVAS_WIDTH - 2*MARGIN_LEFT
    table_height = 30*mm
    
    # Draw table border
    c.rect(MARGIN_LEFT, y_pos - table_height, table_width, table_height)
    
    # First row headers
    row1_y = y_pos - 5*mm
    c.setFont("Helvetica", 9)
    c.drawString(MARGIN_LEFT + 2*mm, row1_y, "1. OFFICE/DEPARTMENT")
    c.drawString(MARGIN_LEFT + 90*mm, row1_y, "2. NAME:")
    c.drawString(MARGIN_LEFT + 130*mm, row1_y, "(Last)")
    c.drawString(MARGIN_LEFT + 170*mm, row1_y, "(First)")
    c.drawString(MARGIN_LEFT + 210*mm, row1_y, "(Middle)")
    
    # Vertical dividers
    c.line(MARGIN_LEFT + 85*mm, y_pos, MARGIN_LEFT + 85*mm, y_pos - 15*mm)
    c.line(MARGIN_LEFT + 125*mm, y_pos - 5*mm, MARGIN_LEFT + 125*mm, y_pos - 15*mm)
    c.line(MARGIN_LEFT + 165*mm, y_pos - 5*mm, MARGIN_LEFT + 165*mm, y_pos - 15*mm)
    c.line(MARGIN_LEFT + 205*mm, y_pos - 5*mm, MARGIN_LEFT + 205*mm, y_pos - 15*mm)
    
    # Horizontal divider
    c.line(MARGIN_LEFT, y_pos - 15*mm, MARGIN_LEFT + table_width, y_pos - 15*mm)
    
    # First row data
    c.setFont("Helvetica", 10)
    c.drawString(MARGIN_LEFT + 2*mm, row1_y - 8*mm, form_data['office_department'])
    c.drawString(MARGIN_LEFT + 130*mm, row1_y - 8*mm, form_data['name']['last'])
    c.drawString(MARGIN_LEFT + 170*mm, row1_y - 8*mm, form_data['name']['first'])
    c.drawString(MARGIN_LEFT + 210*mm, row1_y - 8*mm, form_data['name']['middle'])
    
    # Second row headers
    row2_y = y_pos - 20*mm
    c.setFont("Helvetica", 9)
    c.drawString(MARGIN_LEFT + 2*mm, row2_y, "3. DATE OF FILING")
    c.drawString(MARGIN_LEFT + 90*mm, row2_y, "4. POSITION")
    c.drawString(MARGIN_LEFT + 170*mm, row2_y, "5. SALARY")
    
    # More vertical dividers
    c.line(MARGIN_LEFT + 85*mm, y_pos - 15*mm, MARGIN_LEFT + 85*mm, y_pos - table_height)
    c.line(MARGIN_LEFT + 165*mm, y_pos - 15*mm, MARGIN_LEFT + 165*mm, y_pos - table_height)
    
    # Second row data
    c.setFont("Helvetica", 10)
    date_str = form_data['date_filing'].strftime("%B %d, %Y")
    c.drawString(MARGIN_LEFT + 2*mm, row2_y - 5*mm, date_str)
    c.drawString(MARGIN_LEFT + 90*mm, row2_y - 5*mm, form_data['position'])
    c.drawString(MARGIN_LEFT + 170*mm, row2_y - 5*mm, form_data['salary'])
    
    # Save PDF
    c.save()
    print(f"✅ Test PDF created: {filename}")
    
    # Verify data
    print("\n📋 Data verification:")
    print(f"Office: {form_data['office_department']}")
    print(f"Name: {form_data['name']['last']}, {form_data['name']['first']} {form_data['name']['middle']}")
    print(f"Date: {date_str}")
    print(f"Position: {form_data['position']}")
    print(f"Salary: {form_data['salary']}")
    
    return filename

if __name__ == "__main__":
    create_test_pdf()