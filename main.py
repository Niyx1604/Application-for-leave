#!/usr/bin/env python3
"""
Leave Application Encoder System
Main application entry point for Civil Service Form No. 6 (Revised 2020) processing.
"""

import sys
import os
from pathlib import Path

def main():
    """Main application entry point."""
    print("Leave Application Encoder System")
    print("Civil Service Form No. 6 (Revised 2020) Processing")
    print("=" * 50)
    
    # Check if template file exists
    template_path = Path("ALA.xlsx")
    if not template_path.exists():
        print("ERROR: Template file 'ALA.xlsx' not found in current directory.")
        print("Please ensure the Civil Service Form No. 6 template is present.")
        return 1
    
    print(f"Template file found: {template_path.absolute()}")
    print("System ready for initialization.")
    
    # Initialize and launch GUI interface
    try:
        # Add src directory to path for imports
        sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))
        
        from gui_interface import LeaveApplicationGUI
        
        print("Launching GUI interface...")
        gui = LeaveApplicationGUI()
        gui.run()
        
    except ImportError as e:
        print(f"ERROR: Failed to import GUI components: {e}")
        return 1
    except Exception as e:
        print(f"ERROR: Failed to launch application: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())