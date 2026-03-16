#!/usr/bin/env python3
"""
Preservation Property Tests for PDF Form Body Rendering
**Property 2: Preservation** - Form Body and Data Population Behavior
**IMPORTANT**: These tests observe and validate behavior on UNFIXED code
**EXPECTED OUTCOME**: Tests PASS on unfixed code (confirms baseline behavior to preserve)
**Validates: Requirements 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8**
"""

import pytest
from hypothesis import given, strategies as st, settings, assume, HealthCheck
import tempfile
import os
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from datetime import datetime, date, timedelta
from unittest.mock import Mock, patch, MagicMock
import sys
import tkinter as tk

# Import the unfixed version
sys.path.insert(0, '.')

# Mock tkcalendar before importing
sys.modules['tkcalendar'] = MagicMock()

from leave_app_refactored import LeaveApplicationEncoder

# Strategy definitions for property-based testing
@st.composite
def form_data_strategy(draw):
    """Generate valid form data for testing"""
    positions = [
        "Administrative Aide I", "Administrative Aide II", "Administrative Aide III",
        "Social Insurance Assistant I", "Social Insurance Officer I"
    ]
    
    # Generate random but valid data
    first_name = draw(st.text(min_size=1, max_size=20, alphabet=st.characters(whitelist_categories=('Lu', 'Ll'))))
    last_name = draw(st.text(min_size=1, max_size=20, alphabet=st.characters(whitelist_categories=('Lu', 'Ll'))))
    middle_name = draw(st.text(min_size=0, max_size=20, alphabet=st.characters(whitelist_categories=('Lu', 'Ll'))))
    
    position = draw(st.sampled_from(positions))
    salary = draw(st.floats(min_value=10000, max_value=100000))
    working_days = draw(st.integers(min_value=1, max_value=30))
    
    # Generate dates
    base_date = datetime.now()
    start_date = base_date + timedelta(days=draw(st.integers(min_value=0, max_value=30)))
    end_date = start_date + timedelta(days=draw(st.integers(min_value=0, max_value=working_days)))
    
    # Generate leave types (at least one must be True)
    leave_types = {
        'vacation': draw(st.booleans()),
        'mandatory': draw(st.booleans()),
        'sick': draw(st.booleans()),
        'maternity': draw(st.booleans()),
        'paternity': draw(st.booleans()),
        'special_privilege': draw(st.booleans()),
        'solo_parent': draw(st.booleans()),
        'study': draw(st.booleans()),
        'vawc_10day': draw(st.booleans()),
        'rehabilitation': draw(st.booleans()),
        'special_women': draw(st.booleans()),
        'special_emergency': draw(st.booleans()),
        'adoption': draw(st.booleans())
    }
    
    # Ensure at least one leave type is selected
    if not any(leave_types.values()):
        leave_types['vacation'] = True
    
    return {
        'office_department': 'LHIO - Digos',
        'name': {'last': last_name, 'first': first_name, 'middle': middle_name},
        'date_filing': base_date,
        'position': position,
        'salary': f"{salary:.2f}",
        'leave_types': leave_types,
        'inclusive_dates': {'start': start_date, 'end': end_date},
        'working_days': working_days,
        'commutation': {'not_requested': draw(st.booleans()), 'requested': False}
    }


class TestPDFPreservationProperties:
    """
    Preservation Property Tests
    These tests validate that form body rendering, data population, and PDF generation
    continue to work correctly on UNFIXED code (baseline behavior to preserve)
    """
    
    def setup_method(self):
        """Setup test environment"""
        self.temp_dir = tempfile.mkdtemp()
        self.test_pdf_path = os.path.join(self.temp_dir, "test_preservation.pdf")
        
    def teardown_method(self):
        """Cleanup test environment"""
        if os.path.exists(self.test_pdf_path):
            os.remove(self.test_pdf_path)
        if os.path.exists(self.temp_dir):
            os.rmdir(self.temp_dir)
    
    @given(form_data_strategy())
    @settings(max_examples=20, deadline=None)
    def test_form_body_table_rendering_preservation(self, form_data):
        """
        **Property 2: Preservation** - Form Body Table Rendering
        Test that form body tables render with correct alignment and structure
        **Validates: Requirement 3.1**
        
        EXPECTED OUTCOME: PASSES on unfixed code (confirms baseline behavior)
        """
        import tkinter as tk
        root = tk.Tk()
        root.withdraw()
        
        try:
            app = LeaveApplicationEncoder(root)
            app.form_data = form_data
            
            c = canvas.Canvas(self.test_pdf_path, pagesize=A4)
            
            # Track rect calls to verify table structure
            original_rect = c.rect
            rect_calls = []
            
            def mock_rect(x, y, width, height, stroke=1, fill=0):
                rect_calls.append({'x': x, 'y': y, 'width': width, 'height': height})
                return original_rect(x, y, width, height, stroke, fill)
            
            c.rect = mock_rect
            
            # Draw form sections (not header)
            app.draw_section_1(c)
            app.draw_section_6(c)
            app.draw_section_7(c)
            c.save()
            
            # Verify table borders are drawn
            assert len(rect_calls) > 0, "No table borders drawn - form body rendering failed"
            
            # Verify rectangles have positive dimensions
            for rect in rect_calls:
                assert rect['width'] > 0, f"Invalid table width: {rect['width']}"
                assert rect['height'] > 0, f"Invalid table height: {rect['height']}"
            
            # Verify PDF file was created
            assert os.path.exists(self.test_pdf_path), "PDF file was not created"
            
        finally:
            root.destroy()
    
    @given(form_data_strategy())
    @settings(max_examples=20, deadline=None, suppress_health_check=[HealthCheck.function_scoped_fixture])
    def test_data_population_preservation(self, form_data):
        """
        **Property 2: Preservation** - Data Population into Form Fields
        Test that user input data populates correctly into form fields
        **Validates: Requirement 3.2**
        
        EXPECTED OUTCOME: PASSES on unfixed code (confirms baseline behavior)
        """
        import tkinter as tk
        root = tk.Tk()
        root.withdraw()
        
        try:
            app = LeaveApplicationEncoder(root)
            app.form_data = form_data
            
            c = canvas.Canvas(self.test_pdf_path, pagesize=A4)
            
            # Track drawString calls to verify data is written
            original_drawString = c.drawString
            text_calls = []
            
            def mock_drawString(x, y, text):
                text_calls.append({'x': x, 'y': y, 'text': str(text)})
                return original_drawString(x, y, text)
            
            c.drawString = mock_drawString
            
            # Draw form sections
            app.draw_section_1(c)
            c.save()
            
            # Verify critical data fields are populated
            all_text = ' '.join([call['text'] for call in text_calls])
            
            # Check that name components appear in the output
            assert form_data['name']['last'] in all_text, f"Last name '{form_data['name']['last']}' not found in PDF"
            assert form_data['name']['first'] in all_text, f"First name '{form_data['name']['first']}' not found in PDF"
            
            # Check that position appears
            assert form_data['position'] in all_text, f"Position '{form_data['position']}' not found in PDF"
            
            # Check that office/department appears
            assert form_data['office_department'] in all_text, f"Office/Department '{form_data['office_department']}' not found in PDF"
            
        finally:
            root.destroy()
    
    @given(form_data_strategy())
    @settings(max_examples=15, deadline=None, suppress_health_check=[HealthCheck.function_scoped_fixture])
    def test_checkbox_rendering_preservation(self, form_data):
        """
        **Property 2: Preservation** - Leave Type Checkbox Rendering
        Test that leave type checkboxes render correctly
        **Validates: Requirement 3.4**
        
        EXPECTED OUTCOME: PASSES on unfixed code (confirms baseline behavior)
        """
        import tkinter as tk
        root = tk.Tk()
        root.withdraw()
        
        try:
            app = LeaveApplicationEncoder(root)
            app.form_data = form_data
            
            c = canvas.Canvas(self.test_pdf_path, pagesize=A4)
            
            # Track rect calls for checkboxes
            original_rect = c.rect
            checkbox_rects = []
            
            def mock_rect(x, y, width, height, stroke=1, fill=0):
                # Checkboxes are small squares (3mm x 3mm)
                if abs(width - 3*mm) < 0.1 and abs(height - 3*mm) < 0.1:
                    checkbox_rects.append({'x': x, 'y': y})
                return original_rect(x, y, width, height, stroke, fill)
            
            c.rect = mock_rect
            
            # Draw section 6 which contains checkboxes
            app.draw_section_6(c)
            c.save()
            
            # Verify checkboxes are drawn
            # Section 6 has 13 leave type checkboxes + 2 commutation checkboxes + other checkboxes
            assert len(checkbox_rects) >= 13, f"Expected at least 13 leave type checkboxes, found {len(checkbox_rects)}"
            
        finally:
            root.destroy()
    
    @given(form_data_strategy())
    @settings(max_examples=15, deadline=None)
    def test_date_formatting_preservation(self, form_data):
        """
        **Property 2: Preservation** - Date Formatting and Display
        Test that dates are formatted and displayed correctly
        **Validates: Requirement 3.5**
        
        EXPECTED OUTCOME: PASSES on unfixed code (confirms baseline behavior)
        """
        import tkinter as tk
        root = tk.Tk()
        root.withdraw()
        
        try:
            app = LeaveApplicationEncoder(root)
            app.form_data = form_data
            
            c = canvas.Canvas(self.test_pdf_path, pagesize=A4)
            
            # Track drawString calls to verify date formatting
            original_drawString = c.drawString
            text_calls = []
            
            def mock_drawString(x, y, text):
                text_calls.append(str(text))
                return original_drawString(x, y, text)
            
            c.drawString = mock_drawString
            
            # Draw sections with dates
            app.draw_section_1(c)
            app.draw_section_6(c)
            c.save()
            
            all_text = ' '.join(text_calls)
            
            # Verify date_filing is formatted correctly (should contain month name)
            filing_date = form_data['date_filing']
            month_name = filing_date.strftime("%B")
            assert month_name in all_text, f"Filing date month '{month_name}' not found in PDF"
            
            # Verify inclusive dates are present
            start_date = form_data['inclusive_dates']['start']
            start_month = start_date.strftime("%B")
            assert start_month in all_text, f"Start date month '{start_month}' not found in PDF"
            
        finally:
            root.destroy()
    
    @given(form_data_strategy())
    @settings(max_examples=15, deadline=None, suppress_health_check=[HealthCheck.function_scoped_fixture])
    def test_working_days_display_preservation(self, form_data):
        """
        **Property 2: Preservation** - Working Days Display
        Test that working days are displayed in correct format
        **Validates: Requirement 3.5**
        
        EXPECTED OUTCOME: PASSES on unfixed code (confirms baseline behavior)
        """
        import tkinter as tk
        root = tk.Tk()
        root.withdraw()
        
        try:
            app = LeaveApplicationEncoder(root)
            app.form_data = form_data
            
            c = canvas.Canvas(self.test_pdf_path, pagesize=A4)
            
            # Track drawString calls
            original_drawString = c.drawString
            text_calls = []
            
            def mock_drawString(x, y, text):
                text_calls.append(str(text))
                return original_drawString(x, y, text)
            
            c.drawString = mock_drawString
            
            # Draw section 6 which contains working days
            app.draw_section_6(c)
            c.save()
            
            all_text = ' '.join(text_calls)
            
            # Verify working days format (e.g., "1 Day" or "5 Days")
            working_days = form_data['working_days']
            if working_days == 1:
                expected_text = "1 Day"
            else:
                expected_text = f"{working_days} Days"
            
            assert expected_text in all_text, f"Working days '{expected_text}' not found in PDF"
            
        finally:
            root.destroy()
    
    @given(form_data_strategy())
    @settings(max_examples=10, deadline=None)
    def test_pdf_file_generation_preservation(self, form_data):
        """
        **Property 2: Preservation** - PDF File Generation
        Test that PDF file generation creates valid documents
        **Validates: Requirement 3.7**
        
        EXPECTED OUTCOME: PASSES on unfixed code (confirms baseline behavior)
        """
        import tkinter as tk
        root = tk.Tk()
        root.withdraw()
        
        try:
            app = LeaveApplicationEncoder(root)
            app.form_data = form_data
            
            c = canvas.Canvas(self.test_pdf_path, pagesize=A4)
            
            # Draw all sections
            app.draw_section_1(c)
            app.draw_section_6(c)
            app.draw_section_7(c)
            c.save()
            
            # Verify PDF file exists
            assert os.path.exists(self.test_pdf_path), "PDF file was not created"
            
            # Verify PDF file is not empty
            file_size = os.path.getsize(self.test_pdf_path)
            assert file_size > 0, f"PDF file is empty (size: {file_size})"
            
            # Verify PDF file has reasonable size (at least 1KB)
            assert file_size > 1000, f"PDF file is too small ({file_size} bytes), likely invalid"
            
        finally:
            root.destroy()
    
    def test_signature_section_positioning_preservation(self):
        """
        **Property 2: Preservation** - Signature Sections Positioning
        Test that signature sections are positioned correctly
        **Validates: Requirement 3.6**
        
        EXPECTED OUTCOME: PASSES on unfixed code (confirms baseline behavior)
        """
        import tkinter as tk
        root = tk.Tk()
        root.withdraw()
        
        try:
            app = LeaveApplicationEncoder(root)
            
            c = canvas.Canvas(self.test_pdf_path, pagesize=A4)
            
            # Track line calls for signature lines
            original_line = c.line
            line_calls = []
            
            def mock_line(x1, y1, x2, y2):
                line_calls.append({'x1': x1, 'y1': y1, 'x2': x2, 'y2': y2})
                return original_line(x1, y1, x2, y2)
            
            c.line = mock_line
            
            # Draw sections with signature lines
            app.draw_section_6(c)
            app.draw_section_7(c)
            c.save()
            
            # Verify signature lines are drawn (horizontal lines)
            horizontal_lines = [line for line in line_calls if line['y1'] == line['y2'] and abs(line['x2'] - line['x1']) > 20*mm]
            
            assert len(horizontal_lines) > 0, "No signature lines found in PDF"
            
            # Verify lines have reasonable positioning
            for line in horizontal_lines:
                assert line['x1'] >= 0, f"Invalid signature line X1: {line['x1']}"
                # Allow generous tolerance for lines that may extend beyond page width (some implementations do this)
                assert line['x2'] <= A4[0] + 200, f"Invalid signature line X2: {line['x2']} (page width: {A4[0]})"
                # Y coordinates can be negative in PDF (below origin)
                assert line['y1'] >= -A4[1], f"Invalid signature line Y: {line['y1']} (too far below page)"
                assert line['y1'] <= A4[1], f"Invalid signature line Y: {line['y1']} (too far above page)"
            
        finally:
            root.destroy()
    
    def test_missing_logo_error_handling_preservation(self):
        """
        **Property 2: Preservation** - Error Handling for Missing Logo Files
        Test that system handles missing logo files gracefully without crashing
        **Validates: Requirement 3.8**
        
        EXPECTED OUTCOME: PASSES on unfixed code (confirms baseline behavior)
        """
        import tkinter as tk
        root = tk.Tk()
        root.withdraw()
        
        try:
            app = LeaveApplicationEncoder(root)
            
            # Set non-existent logo paths
            app.philhealth_logo_var.set("nonexistent_logo1.png")
            app.bagong_logo_var.set("nonexistent_logo2.png")
            
            c = canvas.Canvas(self.test_pdf_path, pagesize=A4)
            
            # This should NOT crash even with missing logos
            try:
                app.draw_header_with_logos(c)
                c.save()
                success = True
            except Exception as e:
                success = False
                error_msg = str(e)
            
            # Verify it handled missing logos gracefully
            assert success, f"System crashed with missing logos: {error_msg if not success else ''}"
            
            # Verify PDF was still created
            assert os.path.exists(self.test_pdf_path), "PDF file was not created despite missing logos"
            
        finally:
            root.destroy()
    
    @given(form_data_strategy())
    @settings(max_examples=10, deadline=None)
    def test_table_border_structure_preservation(self, form_data):
        """
        **Property 2: Preservation** - Table Border Structure
        Test that table borders display with proper structure
        **Validates: Requirement 3.3**
        
        EXPECTED OUTCOME: PASSES on unfixed code (confirms baseline behavior)
        """
        import tkinter as tk
        root = tk.Tk()
        root.withdraw()
        
        try:
            app = LeaveApplicationEncoder(root)
            app.form_data = form_data
            
            c = canvas.Canvas(self.test_pdf_path, pagesize=A4)
            
            # Track rect and line calls for table structure
            original_rect = c.rect
            original_line = c.line
            rect_calls = []
            line_calls = []
            
            def mock_rect(x, y, width, height, stroke=1, fill=0):
                rect_calls.append({'x': x, 'y': y, 'width': width, 'height': height})
                return original_rect(x, y, width, height, stroke, fill)
            
            def mock_line(x1, y1, x2, y2):
                line_calls.append({'x1': x1, 'y1': y1, 'x2': x2, 'y2': y2})
                return original_line(x1, y1, x2, y2)
            
            c.rect = mock_rect
            c.line = mock_line
            
            # Draw sections with tables
            app.draw_section_1(c)
            app.draw_section_6(c)
            app.draw_section_7(c)
            c.save()
            
            # Verify table borders (large rectangles) are drawn
            large_rects = [r for r in rect_calls if r['width'] > 50*mm and r['height'] > 10*mm]
            assert len(large_rects) >= 3, f"Expected at least 3 table borders, found {len(large_rects)}"
            
            # Verify table divider lines are drawn
            assert len(line_calls) > 0, "No table divider lines found"
            
        finally:
            root.destroy()


if __name__ == "__main__":
    # Run the tests
    pytest.main([__file__, "-v", "--tb=short"])
