"""
Data Encoder Component
Handles data transformation, validation, and business rule processing.
"""

from datetime import datetime, date, timedelta
from typing import Dict, Any, List, Optional
import re


class DataEncoder:
    """Encodes and validates form data for leave applications."""
    
    def __init__(self):
        """Initialize data encoder."""
        self.position_options = [
            "Administrative Aide VI",
            "Administrative Officer",
            "Clerk",
            "Secretary"
        ]
    
    def encode_form_data(self, user_inputs: Dict[str, Any]) -> Dict[str, Any]:
        """Transform GUI inputs into Excel cell mappings.
        
        Args:
            user_inputs: Dictionary of form inputs from GUI
            
        Returns:
            Dictionary mapping field names to formatted values
        """
        encoded_data = {}
        
        # Encode basic fields
        if 'name' in user_inputs:
            encoded_data['name'] = user_inputs['name']
        
        if 'position' in user_inputs:
            encoded_data['position'] = user_inputs['position']
        
        if 'date_filing' in user_inputs:
            encoded_data['date_filing'] = self.format_date(user_inputs['date_filing'])
        
        if 'inclusive_dates' in user_inputs:
            encoded_data['inclusive_dates'] = self.format_date_range(user_inputs['inclusive_dates'])
        
        if 'working_days' in user_inputs:
            encoded_data['working_days'] = user_inputs['working_days']
        
        return encoded_data
    
    def format_date(self, date_value: Any) -> str:
        """Format date for Excel display.
        
        Args:
            date_value: Date value to format
            
        Returns:
            Formatted date string
        """
        if isinstance(date_value, date):
            return date_value.strftime("%B %d, %Y")
        elif isinstance(date_value, str):
            return date_value
        else:
            return str(date_value)
    
    def format_date_range(self, dates: Any) -> str:
        """Format date range for Excel display.
        
        Handles multiple date formats:
        - Single dates: "Nov 28"
        - Consecutive ranges: "Oct 29-30" 
        - Non-consecutive dates: "Dec 1&26"
        
        Args:
            dates: Date range to format (list, string, or single date)
            
        Returns:
            Formatted date range string
        """
        if isinstance(dates, list):
            if len(dates) == 1:
                # Single date
                return self.format_date(dates[0])
            elif len(dates) == 2:
                start_date, end_date = dates
                if start_date == end_date:
                    # Same date
                    return self.format_date(start_date)
                elif self._are_consecutive_dates(start_date, end_date):
                    # Consecutive dates - use short format for same month
                    if start_date.month == end_date.month and start_date.year == end_date.year:
                        return f"{start_date.strftime('%b')} {start_date.day}-{end_date.day}"
                    else:
                        return f"{self.format_date(start_date)} - {self.format_date(end_date)}"
                else:
                    # Non-consecutive dates - use & separator
                    if start_date.month == end_date.month and start_date.year == end_date.year:
                        return f"{start_date.strftime('%b')} {start_date.day}&{end_date.day}"
                    else:
                        return f"{self.format_date(start_date)} & {self.format_date(end_date)}"
            else:
                # Multiple non-consecutive dates
                formatted_dates = [self.format_date(d) for d in dates]
                return " & ".join(formatted_dates)
        elif isinstance(dates, str):
            return dates
        else:
            return str(dates)
    
    def _are_consecutive_dates(self, start_date: date, end_date: date) -> bool:
        """Check if two dates are consecutive (accounting for weekends).
        
        Args:
            start_date: First date
            end_date: Second date
            
        Returns:
            True if dates are consecutive working days
        """
        if start_date >= end_date:
            return False
        
        # Calculate the difference in days
        delta = (end_date - start_date).days
        
        # For working days, consecutive means next working day
        # This is a simple heuristic - could be enhanced for holidays
        return delta <= 3  # Allows for weekend gaps
    
    def calculate_working_days(self, start_date: date, end_date: date) -> int:
        """Calculate working days between two dates (inclusive).
        
        Args:
            start_date: Start date of leave period
            end_date: End date of leave period
            
        Returns:
            Number of working days (Monday-Friday, inclusive of both dates)
        """
        if start_date > end_date:
            return 0
        
        working_days = 0
        current_date = start_date
        
        while current_date <= end_date:
            # Count weekdays (Monday=0, Sunday=6)
            if current_date.weekday() < 5:  # Monday to Friday
                working_days += 1
            # Use timedelta to properly increment date
            from datetime import timedelta
            current_date = current_date + timedelta(days=1)
        
        return working_days
    
    def calculate_working_days_for_range(self, dates: Any) -> int:
        """Calculate working days for various date range formats.
        
        Args:
            dates: Date range (single date, list of dates, or date range)
            
        Returns:
            Total number of working days
        """
        if isinstance(dates, list):
            if len(dates) == 1:
                # Single date
                return 1 if dates[0].weekday() < 5 else 0
            elif len(dates) == 2:
                # Date range
                return self.calculate_working_days(dates[0], dates[1])
            else:
                # Multiple individual dates
                total_days = 0
                for date_val in dates:
                    if date_val.weekday() < 5:  # Monday to Friday
                        total_days += 1
                return total_days
        elif isinstance(dates, date):
            # Single date
            return 1 if dates.weekday() < 5 else 0
        else:
            return 0
    
    def validate_date_range(self, dates: Any) -> bool:
        """Validate that dates are in proper format and chronological order.
        
        Args:
            dates: Date range to validate (list, single date, or string)
            
        Returns:
            True if dates are valid, False otherwise
        """
        if not dates:
            return False
        
        if isinstance(dates, list):
            if len(dates) == 0:
                return False
            elif len(dates) == 1:
                # Single date is always valid
                return isinstance(dates[0], date)
            elif len(dates) == 2:
                # Two dates should be in chronological order
                return (isinstance(dates[0], date) and 
                       isinstance(dates[1], date) and 
                       dates[0] <= dates[1])
            else:
                # Multiple dates should all be valid date objects
                return all(isinstance(d, date) for d in dates)
        elif isinstance(dates, date):
            return True
        elif isinstance(dates, str):
            # Try to parse string date formats
            return self._validate_date_string(dates)
        
        return False
    
    def _validate_date_string(self, date_str: str) -> bool:
        """Validate string date formats like 'Oct 29-30', 'Dec 1&26', etc.
        
        Args:
            date_str: Date string to validate
            
        Returns:
            True if string represents valid date format
        """
        if not date_str or not isinstance(date_str, str):
            return False
        
        # Common date patterns
        patterns = [
            r'^[A-Za-z]{3}\s+\d{1,2}$',  # "Nov 28"
            r'^[A-Za-z]{3}\s+\d{1,2}-\d{1,2}$',  # "Oct 29-30"
            r'^[A-Za-z]{3}\s+\d{1,2}&\d{1,2}$',  # "Dec 1&26"
            r'^[A-Za-z]+\s+\d{1,2},\s+\d{4}$',  # "November 28, 2023"
        ]
        
        return any(re.match(pattern, date_str.strip()) for pattern in patterns)
    
    def validate_business_rules(self, user_inputs: Dict[str, Any]) -> List[str]:
        """Validate business rules for form data.
        
        Args:
            user_inputs: Form data to validate
            
        Returns:
            List of validation error messages
        """
        errors = []
        
        # Check required fields
        required_fields = ['name', 'position', 'date_filing', 'inclusive_dates', 'working_days']
        for field in required_fields:
            if field not in user_inputs or not user_inputs[field]:
                errors.append(f"Field '{field}' is required")
        
        # Validate name format (should contain at least first and last name)
        if 'name' in user_inputs and user_inputs['name']:
            name = user_inputs['name'].strip()
            if len(name.split()) < 2:
                errors.append("Name should include both first and last name")
        
        # Validate position selection
        if 'position' in user_inputs and user_inputs['position']:
            if user_inputs['position'] not in self.position_options:
                errors.append("Position must be selected from approved list")
        
        # Validate date range format and chronology
        if 'inclusive_dates' in user_inputs and user_inputs['inclusive_dates']:
            if not self.validate_date_range(user_inputs['inclusive_dates']):
                errors.append("Invalid date range format or chronological order")
        
        # Validate working days consistency
        if ('inclusive_dates' in user_inputs and 'working_days' in user_inputs and 
            user_inputs['inclusive_dates'] and user_inputs['working_days']):
            
            try:
                calculated_days = self.calculate_working_days_for_range(user_inputs['inclusive_dates'])
                entered_days = int(user_inputs['working_days'])
                
                if calculated_days != entered_days:
                    errors.append(f"Working days mismatch: calculated {calculated_days}, entered {entered_days}")
            except (ValueError, TypeError):
                errors.append("Invalid working days value")
        
        # Validate working days range (1-31 as per requirements)
        if 'working_days' in user_inputs and user_inputs['working_days']:
            try:
                days = int(user_inputs['working_days'])
                if days < 1 or days > 31:
                    errors.append("Working days must be between 1 and 31")
            except (ValueError, TypeError):
                errors.append("Working days must be a valid number")
        
        return errors
        
    def parse_date_input(self, date_input: Any) -> List[date]:
        """Parse various date input formats into a list of date objects.
        
        Args:
            date_input: Date input in various formats (string, date, list)
            
        Returns:
            List of parsed date objects
        """
        if isinstance(date_input, date):
            return [date_input]
        elif isinstance(date_input, list):
            return [d for d in date_input if isinstance(d, date)]
        elif isinstance(date_input, str):
            return self._parse_date_string(date_input)
        else:
            return []
    
    def _parse_date_string(self, date_str: str) -> List[date]:
        """Parse string date formats into date objects.
        
        Args:
            date_str: Date string to parse
            
        Returns:
            List of parsed date objects
        """
        dates = []
        
        try:
            # Handle formats like "Oct 29-30", "Dec 1&26", "Nov 28"
            if '-' in date_str:
                # Consecutive range format
                parts = date_str.split('-')
                if len(parts) == 2:
                    start_part = parts[0].strip()
                    end_part = parts[1].strip()
                    
                    # Parse start date
                    start_date = datetime.strptime(f"{start_part} {datetime.now().year}", "%b %d %Y").date()
                    
                    # Parse end date (might just be day number)
                    if ' ' in end_part:
                        end_date = datetime.strptime(f"{end_part} {datetime.now().year}", "%b %d %Y").date()
                    else:
                        # Same month, different day
                        end_date = start_date.replace(day=int(end_part))
                    
                    dates = [start_date, end_date]
            
            elif '&' in date_str:
                # Non-consecutive format
                parts = date_str.split('&')
                if len(parts) == 2:
                    start_part = parts[0].strip()
                    end_part = parts[1].strip()
                    
                    # Parse start date
                    start_date = datetime.strptime(f"{start_part} {datetime.now().year}", "%b %d %Y").date()
                    
                    # Parse end date (might just be day number)
                    if ' ' in end_part:
                        end_date = datetime.strptime(f"{end_part} {datetime.now().year}", "%b %d %Y").date()
                    else:
                        # Same month, different day
                        end_date = start_date.replace(day=int(end_part))
                    
                    dates = [start_date, end_date]
            
            else:
                # Single date format
                single_date = datetime.strptime(f"{date_str} {datetime.now().year}", "%b %d %Y").date()
                dates = [single_date]
                
        except (ValueError, AttributeError):
            # If parsing fails, return empty list
            dates = []
        
        return dates