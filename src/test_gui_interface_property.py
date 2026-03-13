"""
Property-based tests for GUI Interface Component
Tests automatic field population and other GUI properties.
"""

import unittest
from unittest.mock import patch, MagicMock
from datetime import datetime, date
from hypothesis import given, strategies as st, settings
import tkinter as tk

from gui_interface import LeaveApplicationGUI


class TestGUIInterfaceProperties(unittest.TestCase):
    """Property-based tests for GUI interface component."""
    
    def setUp(self):
        """Set up test environment."""
        # Mock tkinter components to avoid GUI creation during tests
        self.tk_patcher = patch('gui_interface.tk')
        self.mock_tk = self.tk_patcher.start()
        
        # Mock StringVar
        self.mock_string_var = MagicMock()
        self.mock_tk.StringVar.return_value = self.mock_string_var
        
        # Mock Tk root window
        self.mock_root = MagicMock()
        self.mock_tk.Tk.return_value = self.mock_root
        
        # Mock ttk components
        self.ttk_patcher = patch('gui_interface.ttk')
        self.mock_ttk = self.ttk_patcher.start()
        
        # Mock tkcalendar components
        self.calendar_patcher = patch('gui_interface.DateEntry')
        self.mock_date_entry = self.calendar_patcher.start()
        
    def tearDown(self):
        """Clean up test environment."""
        self.tk_patcher.stop()
        self.ttk_patcher.stop()
        self.calendar_patcher.stop()
    
    @given(st.datetimes(min_value=datetime(2020, 1, 1), max_value=datetime(2030, 12, 31)))
    @settings(max_examples=100)
    def test_property_automatic_field_population(self, test_datetime):
        """
        **Property 6: Automatic Field Population**
        **Validates: Requirements 2.5, 3.1**
        
        For any application startup, the Date Filing field should automatically 
        populate with the current system date in the correct format.
        """
        with patch('gui_interface.datetime') as mock_datetime:
            # Mock datetime.now() to return our test datetime
            mock_datetime.now.return_value = test_datetime
            mock_datetime.strftime = datetime.strftime
            
            # Create GUI instance
            gui = LeaveApplicationGUI()
            
            # Verify that date_filing_var was set with the current date
            expected_date_string = test_datetime.strftime("%B %d, %Y")
            self.mock_string_var.set.assert_called_with(expected_date_string)
            
            # Verify the format is correct (Month Day, Year)
            actual_call_args = self.mock_string_var.set.call_args[0][0]
            self.assertRegex(actual_call_args, r'^[A-Z][a-z]+ \d{1,2}, \d{4}$')
            
            # Verify it matches the expected format exactly
            self.assertEqual(actual_call_args, expected_date_string)
    
    def test_automatic_field_population_on_startup(self):
        """
        Unit test to verify automatic date filing population on startup.
        Tests the specific behavior described in requirements 2.5 and 3.1.
        """
        # Test with a known date
        test_date = datetime(2024, 1, 15, 10, 30, 0)
        
        with patch('gui_interface.datetime') as mock_datetime:
            mock_datetime.now.return_value = test_date
            mock_datetime.strftime = datetime.strftime
            
            # Create GUI instance
            gui = LeaveApplicationGUI()
            
            # Verify the date filing field was auto-populated
            expected_date = "January 15, 2024"
            self.mock_string_var.set.assert_called_with(expected_date)
    
    def test_date_filing_format_consistency(self):
        """
        Test that the date filing format is consistent with the expected format.
        """
        test_cases = [
            (datetime(2024, 1, 1), "January 01, 2024"),
            (datetime(2024, 12, 31), "December 31, 2024"),
            (datetime(2024, 6, 15), "June 15, 2024"),
            (datetime(2024, 2, 29), "February 29, 2024"),  # Leap year
        ]
        
        for test_datetime, expected_format in test_cases:
            with patch('gui_interface.datetime') as mock_datetime:
                mock_datetime.now.return_value = test_datetime
                mock_datetime.strftime = datetime.strftime
                
                # Create GUI instance
                gui = LeaveApplicationGUI()
                
                # Verify the format matches expected
                self.mock_string_var.set.assert_called_with(expected_format)
    
    @given(st.integers(min_value=2020, max_value=2030),
           st.integers(min_value=1, max_value=12),
           st.integers(min_value=1, max_value=28))  # Use 28 to avoid invalid dates
    @settings(max_examples=50)
    def test_property_date_format_validity(self, year, month, day):
        """
        Property test to ensure date formatting works for any valid date.
        """
        try:
            test_datetime = datetime(year, month, day)
            
            with patch('gui_interface.datetime') as mock_datetime:
                mock_datetime.now.return_value = test_datetime
                mock_datetime.strftime = datetime.strftime
                
                # Create GUI instance
                gui = LeaveApplicationGUI()
                
                # Get the formatted date string
                call_args = self.mock_string_var.set.call_args[0][0]
                
                # Verify it's a valid date string format
                self.assertIsInstance(call_args, str)
                self.assertGreater(len(call_args), 0)
                
                # Verify it contains the year
                self.assertIn(str(year), call_args)
                
                # Verify it follows the Month Day, Year pattern
                self.assertRegex(call_args, r'^[A-Z][a-z]+ \d{1,2}, \d{4}$')
                
        except ValueError:
            # Skip invalid dates (like Feb 30)
            pass


if __name__ == '__main__':
    unittest.main()