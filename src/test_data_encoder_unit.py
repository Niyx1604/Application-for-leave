"""
Unit tests for DataEncoder class functionality.
"""

import unittest
from datetime import date, datetime
from data_encoder import DataEncoder


class TestDataEncoder(unittest.TestCase):
    """Test cases for DataEncoder class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.encoder = DataEncoder()
    
    def test_format_single_date(self):
        """Test formatting of single dates."""
        test_date = date(2023, 11, 28)
        result = self.encoder.format_date_range([test_date])
        self.assertEqual(result, "November 28, 2023")
    
    def test_format_consecutive_dates_same_month(self):
        """Test formatting of consecutive dates in same month."""
        start_date = date(2023, 10, 29)
        end_date = date(2023, 10, 30)
        result = self.encoder.format_date_range([start_date, end_date])
        self.assertEqual(result, "Oct 29-30")
    
    def test_format_non_consecutive_dates_same_month(self):
        """Test formatting of non-consecutive dates in same month."""
        start_date = date(2023, 12, 1)
        end_date = date(2023, 12, 26)
        result = self.encoder.format_date_range([start_date, end_date])
        self.assertEqual(result, "Dec 1&26")
    
    def test_calculate_working_days_single_weekday(self):
        """Test working days calculation for single weekday."""
        monday = date(2023, 11, 27)  # Monday
        result = self.encoder.calculate_working_days(monday, monday)
        self.assertEqual(result, 1)
    
    def test_calculate_working_days_single_weekend(self):
        """Test working days calculation for single weekend day."""
        saturday = date(2023, 11, 25)  # Saturday
        result = self.encoder.calculate_working_days(saturday, saturday)
        self.assertEqual(result, 0)
    
    def test_calculate_working_days_week_range(self):
        """Test working days calculation for a week range."""
        monday = date(2023, 11, 27)  # Monday
        friday = date(2023, 12, 1)   # Friday
        result = self.encoder.calculate_working_days(monday, friday)
        self.assertEqual(result, 5)
    
    def test_calculate_working_days_for_range_single_date(self):
        """Test working days calculation for single date range."""
        monday = date(2023, 11, 27)  # Monday
        result = self.encoder.calculate_working_days_for_range([monday])
        self.assertEqual(result, 1)
    
    def test_validate_business_rules_valid_data(self):
        """Test business rules validation with valid data."""
        valid_data = {
            'name': 'Mendoza, Anthony Berja',
            'position': 'Administrative Aide VI',
            'date_filing': date.today(),
            'inclusive_dates': [date(2023, 11, 27), date(2023, 11, 28)],
            'working_days': 2
        }
        errors = self.encoder.validate_business_rules(valid_data)
        self.assertEqual(len(errors), 0)
    
    def test_validate_business_rules_missing_fields(self):
        """Test business rules validation with missing required fields."""
        invalid_data = {
            'name': 'John Doe',
            # Missing other required fields
        }
        errors = self.encoder.validate_business_rules(invalid_data)
        self.assertGreater(len(errors), 0)
        self.assertTrue(any("required" in error for error in errors))
    
    def test_validate_business_rules_invalid_position(self):
        """Test business rules validation with invalid position."""
        invalid_data = {
            'name': 'John Doe',
            'position': 'Invalid Position',
            'date_filing': date.today(),
            'inclusive_dates': [date(2023, 11, 27)],
            'working_days': 1
        }
        errors = self.encoder.validate_business_rules(invalid_data)
        self.assertTrue(any("approved list" in error for error in errors))
    
    def test_validate_business_rules_working_days_mismatch(self):
        """Test business rules validation with working days mismatch."""
        invalid_data = {
            'name': 'John Doe',
            'position': 'Administrative Aide VI',
            'date_filing': date.today(),
            'inclusive_dates': [date(2023, 11, 27), date(2023, 11, 28)],  # 2 working days
            'working_days': 5  # Incorrect working days
        }
        errors = self.encoder.validate_business_rules(invalid_data)
        self.assertTrue(any("mismatch" in error for error in errors))
    
    def test_validate_business_rules_invalid_name_format(self):
        """Test business rules validation with invalid name format."""
        invalid_data = {
            'name': 'John',  # Only first name
            'position': 'Administrative Aide VI',
            'date_filing': date.today(),
            'inclusive_dates': [date(2023, 11, 27)],
            'working_days': 1
        }
        errors = self.encoder.validate_business_rules(invalid_data)
        self.assertTrue(any("first and last name" in error for error in errors))
    
    def test_validate_business_rules_working_days_out_of_range(self):
        """Test business rules validation with working days out of valid range."""
        invalid_data = {
            'name': 'John Doe',
            'position': 'Administrative Aide VI',
            'date_filing': date.today(),
            'inclusive_dates': [date(2023, 11, 27)],
            'working_days': 35  # Out of 1-31 range
        }
        errors = self.encoder.validate_business_rules(invalid_data)
        self.assertTrue(any("between 1 and 31" in error for error in errors))
    
    def test_validate_date_range_valid_range(self):
        """Test date range validation with valid range."""
        valid_dates = [date(2023, 11, 27), date(2023, 11, 28)]
        result = self.encoder.validate_date_range(valid_dates)
        self.assertTrue(result)
    
    def test_validate_date_range_invalid_order(self):
        """Test date range validation with invalid chronological order."""
        invalid_dates = [date(2023, 11, 28), date(2023, 11, 27)]
        result = self.encoder.validate_date_range(invalid_dates)
        self.assertFalse(result)
    
    def test_validate_date_range_single_date(self):
        """Test date range validation with single date."""
        single_date = [date(2023, 11, 27)]
        result = self.encoder.validate_date_range(single_date)
        self.assertTrue(result)
    
    def test_validate_date_range_empty_list(self):
        """Test date range validation with empty list."""
        empty_dates = []
        result = self.encoder.validate_date_range(empty_dates)
        self.assertFalse(result)
    
    def test_encode_form_data_complete(self):
        """Test complete form data encoding."""
        input_data = {
            'name': 'Mendoza, Anthony Berja',
            'position': 'Administrative Aide VI',
            'date_filing': date(2023, 11, 15),
            'inclusive_dates': [date(2023, 11, 27), date(2023, 11, 28)],
            'working_days': 2
        }
        result = self.encoder.encode_form_data(input_data)
        
        self.assertEqual(result['name'], 'Mendoza, Anthony Berja')
        self.assertEqual(result['position'], 'Administrative Aide VI')
        self.assertEqual(result['date_filing'], 'November 15, 2023')
        self.assertEqual(result['working_days'], 2)
        self.assertIn('inclusive_dates', result)


if __name__ == '__main__':
    unittest.main()