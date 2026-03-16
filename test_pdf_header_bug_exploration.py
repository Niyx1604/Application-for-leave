#!/usr/bin/env python3
import pytest
import tempfile
import os
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
import sys
import tkinter as tk
from unittest.mock import MagicMock

sys.path.insert(0, '.')

# Mock tkcalendar before importing
sys.modules['tkcalendar'] = MagicMock()

from leave_app_refactored import LeaveApplicationEncoder

class TestPDFHeaderBugCondition:
    def setup_method(self):
        self.temp_dir = tempfile.mkdtemp()
        self.test_pdf_path = os.path.join(self.temp_dir, "test_header.pdf")
        
    def teardown_method(self):
        if os.path.exists(self.test_pdf_path):
            os.remove(self.test_pdf_path)
        if os.path.exists(self.temp_dir):
            os.rmdir(self.temp_dir)
    
    def test_header_text_lines_distinct_y_coordinates(self):
        root = tk.Tk()
        root.withdraw()
        
        try:
            app = LeaveApplicationEncoder(root)
            c = canvas.Canvas(self.test_pdf_path, pagesize=A4)
            width, height = A4
            
            y_coordinates = []
            original_drawCentredString = c.drawCentredString
            
            def mock_drawCentredString(x, y, text):
                y_coordinates.append(y)
                return original_drawCentredString(x, y, text)
            
            c.drawCentredString = mock_drawCentredString
            app.draw_header_with_logos(c)
            c.save()
            
            assert len(y_coordinates) >= 5, f"Expected at least 5 text elements, got {len(y_coordinates)}"
            unique_y_coords = set(y_coordinates)
            assert len(unique_y_coords) == len(y_coordinates), f"Text overlap detected! Y coordinates: {y_coordinates}"
            
        finally:
            root.destroy()

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
