#!/usr/bin/env python3
"""
Basic setup test for Leave Application Encoder System.
Verifies that all components can be initialized and basic functionality works.
"""

import sys
from pathlib import Path

def test_imports():
    """Test that all modules can be imported."""
    try:
        from src.template_processor import TemplateProcessor
        from src.data_encoder import DataEncoder
        from src.gui_interface import LeaveApplicationGUI
        from src.pdf_generator import PDFGenerator
        print("✓ All modules imported successfully")
        return True
    except ImportError as e:
        print(f"✗ Import error: {e}")
        return False

def test_component_initialization():
    """Test that all components can be initialized."""
    try:
        from src.template_processor import TemplateProcessor
        from src.data_encoder import DataEncoder
        from src.pdf_generator import PDFGenerator
        
        # Test TemplateProcessor initialization
        template_processor = TemplateProcessor("ALA.xlsx")
        print("✓ TemplateProcessor initialized")
        
        # Test DataEncoder initialization
        data_encoder = DataEncoder()
        print("✓ DataEncoder initialized")
        
        # Test PDFGenerator initialization
        pdf_generator = PDFGenerator()
        print("✓ PDFGenerator initialized")
        
        return True
    except Exception as e:
        print(f"✗ Component initialization error: {e}")
        return False

def test_data_encoder_functionality():
    """Test basic DataEncoder functionality."""
    try:
        from src.data_encoder import DataEncoder
        
        encoder = DataEncoder()
        
        # Test position options
        assert "Administrative Aide VI" in encoder.position_options
        print("✓ Position options configured correctly")
        
        # Test date formatting
        from datetime import date
        test_date = date(2024, 1, 15)
        formatted = encoder.format_date(test_date)
        assert "January 15, 2024" == formatted
        print("✓ Date formatting works correctly")
        
        # Test validation
        test_inputs = {
            'name': 'Test User',
            'position': 'Administrative Aide VI',
            'date_filing': 'January 15, 2024',
            'inclusive_dates': ['January 15, 2024', 'January 16, 2024'],
            'working_days': '2'
        }
        errors = encoder.validate_business_rules(test_inputs)
        assert len(errors) == 0
        print("✓ Data validation works correctly")
        
        return True
    except Exception as e:
        print(f"✗ DataEncoder functionality error: {e}")
        return False

def test_configuration():
    """Test configuration file."""
    try:
        import config
        
        assert config.APP_NAME == "Leave Application Encoder System"
        assert config.TEMPLATE_FILE == "ALA.xlsx"
        assert config.OUTPUT_PDF_NAME == "Application_for_Leave.pdf"
        assert "Administrative Aide VI" in config.POSITION_OPTIONS
        print("✓ Configuration loaded correctly")
        
        return True
    except Exception as e:
        print(f"✗ Configuration error: {e}")
        return False

def main():
    """Run all setup tests."""
    print("Leave Application Encoder System - Setup Test")
    print("=" * 50)
    
    tests = [
        test_imports,
        test_component_initialization,
        test_data_encoder_functionality,
        test_configuration
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()
    
    print(f"Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("✓ All setup tests passed! Project structure is ready.")
        return 0
    else:
        print("✗ Some tests failed. Please check the setup.")
        return 1

if __name__ == "__main__":
    sys.exit(main())