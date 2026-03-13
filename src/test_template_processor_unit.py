#!/usr/bin/env python3
"""
Unit tests for TemplateProcessor class
"""

import unittest
import tempfile
import os
from pathlib import Path
from unittest.mock import patch, MagicMock
from datetime import datetime, date

from template_processor import TemplateProcessor


class TestTemplateProcessor(unittest.TestCase):
    """Unit tests for TemplateProcessor class."""
    
    def setUp(self):
        """Set up test fixtures."""
        # Check for template in parent directory
        parent_template = Path("../ALA.xlsx")
        if parent_template.exists():
            self.test_template_path = str(parent_template)
        else:
            self.test_template_path = "ALA.xlsx"
        self.processor = TemplateProcessor(self.test_template_path)
    
    def test_initialization(self):
        """Test TemplateProcessor initialization."""
        self.assertEqual(str(self.processor.template_path), self.test_template_path)
        self.assertIsNone(self.processor.template_workbook)
        self.assertFalse(self.processor._template_validated)
        self.assertIsInstance(self.processor.CELL_MAPPINGS, dict)
        self.assertIn('name', self.processor.CELL_MAPPINGS)
        self.assertIn('position', self.processor.CELL_MAPPINGS)
    
    def test_cell_mappings_constants(self):
        """Test that cell mapping constants are properly defined."""
        expected_fields = ['name', 'position', 'date_filing', 'inclusive_dates', 'working_days']
        for field in expected_fields:
            self.assertIn(field, self.processor.CELL_MAPPINGS)
            self.assertIsInstance(self.processor.CELL_MAPPINGS[field], str)
    
    def test_get_cell_mappings(self):
        """Test get_cell_mappings returns a copy."""
        mappings = self.processor.get_cell_mappings()
        self.assertIsInstance(mappings, dict)
        self.assertEqual(len(mappings), len(self.processor.CELL_MAPPINGS))
        
        # Verify it's a copy, not the original
        mappings['test'] = 'A1'
        self.assertNotIn('test', self.processor.CELL_MAPPINGS)
    
    def test_validate_template_file_not_found(self):
        """Test validation with non-existent template file."""
        processor = TemplateProcessor("nonexistent.xlsx")
        with self.assertRaises(FileNotFoundError):
            processor.validate_template()
    
    def test_populate_fields_validation(self):
        """Test populate_fields input validation."""
        with self.assertRaises(ValueError):
            self.processor.populate_fields(None, {})
    
    def test_populate_fields_with_unmapped_field(self):
        """Test populate_fields handles unmapped fields gracefully."""
        # Create a mock workbook and worksheet
        mock_workbook = MagicMock()
        mock_worksheet = MagicMock()
        mock_workbook.active = mock_worksheet
        
        test_data = {
            'name': 'Test Name',
            'unmapped_field': 'Test Value'  # This field is not in CELL_MAPPINGS
        }
        
        # Should not raise an exception, just log a warning
        try:
            self.processor.populate_fields(mock_workbook, test_data)
        except Exception as e:
            self.fail(f"populate_fields raised an exception with unmapped field: {e}")
        
        # Verify the mapped field was processed (name gets formatted)
        mock_worksheet.__setitem__.assert_called_with('B8', 'Name, Test')
    
    def test_populate_text_field(self):
        """Test text field population with proper formatting."""
        mock_workbook = MagicMock()
        mock_worksheet = MagicMock()
        mock_workbook.active = mock_worksheet
        
        test_data = {
            'name': 'Anthony Berja Mendoza',
            'position': 'Administrative Aide VI'
        }
        
        self.processor.populate_fields(mock_workbook, test_data)
        
        # Verify name was formatted correctly (Last, First Middle)
        expected_calls = [
            unittest.mock.call('B8', 'Mendoza, Anthony Berja'),
            unittest.mock.call('B9', 'Administrative Aide VI')
        ]
        mock_worksheet.__setitem__.assert_has_calls(expected_calls, any_order=True)
    
    def test_populate_date_field(self):
        """Test date field population with different date formats."""
        mock_workbook = MagicMock()
        mock_worksheet = MagicMock()
        mock_workbook.active = mock_worksheet
        
        test_date = date(2024, 1, 15)
        test_data = {
            'date_filing': test_date
        }
        
        self.processor.populate_fields(mock_workbook, test_data)
        
        # Verify date was populated correctly
        mock_worksheet.__setitem__.assert_called_with('G8', test_date)
    
    def test_populate_number_field(self):
        """Test number field population."""
        mock_workbook = MagicMock()
        mock_worksheet = MagicMock()
        mock_workbook.active = mock_worksheet
        
        test_data = {
            'working_days': 5
        }
        
        self.processor.populate_fields(mock_workbook, test_data)
        
        # Verify number was populated correctly
        mock_worksheet.__setitem__.assert_called_with('G12', 5)
    
    def test_populate_date_range_field(self):
        """Test date range field population with different formats."""
        mock_workbook = MagicMock()
        mock_worksheet = MagicMock()
        mock_workbook.active = mock_worksheet
        
        # Test single date
        test_data = {
            'inclusive_dates': [date(2024, 11, 28)]
        }
        
        self.processor.populate_fields(mock_workbook, test_data)
        mock_worksheet.__setitem__.assert_called_with('B12', 'Nov 28')
        
        # Test date range
        mock_worksheet.reset_mock()
        test_data = {
            'inclusive_dates': [date(2024, 10, 29), date(2024, 10, 30)]
        }
        
        self.processor.populate_fields(mock_workbook, test_data)
        mock_worksheet.__setitem__.assert_called_with('B12', 'Oct 29-Oct 30')
    
    def test_format_employee_name(self):
        """Test employee name formatting."""
        # Test "First Middle Last" to "Last, First Middle" conversion
        result = self.processor._format_employee_name("Anthony Berja Mendoza")
        self.assertEqual(result, "Mendoza, Anthony Berja")
        
        # Test already formatted name
        result = self.processor._format_employee_name("Mendoza, Anthony Berja")
        self.assertEqual(result, "Mendoza, Anthony Berja")
        
        # Test single name
        result = self.processor._format_employee_name("Mendoza")
        self.assertEqual(result, "Mendoza")
        
        # Test two names
        result = self.processor._format_employee_name("Anthony Mendoza")
        self.assertEqual(result, "Mendoza, Anthony")
    
    def test_format_date_for_display(self):
        """Test date formatting for display."""
        test_date = date(2024, 11, 28)
        result = self.processor._format_date_for_display(test_date)
        self.assertEqual(result, "Nov 28")
        
        # Test datetime
        test_datetime = datetime(2024, 2, 16, 10, 30)
        result = self.processor._format_date_for_display(test_datetime)
        self.assertEqual(result, "Feb 16")
        
        # Test string
        result = self.processor._format_date_for_display("Dec 1&26")
        self.assertEqual(result, "Dec 1&26")


if __name__ == '__main__':
    # Check for template file in current or parent directory
    template_paths = [Path("ALA.xlsx"), Path("../ALA.xlsx")]
    template_exists = any(p.exists() for p in template_paths)
    
    if template_exists:
        unittest.main()
    else:
        print("Skipping unit tests - ALA.xlsx template not found")
        print("Run create_test_template.py first to create a test template")