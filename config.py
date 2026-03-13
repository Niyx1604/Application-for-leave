"""
Configuration settings for Leave Application Encoder System.
"""

from pathlib import Path

# Application settings
APP_NAME = "Leave Application Encoder System"
APP_VERSION = "1.0.0"
FORM_TITLE = "Civil Service Form No. 6 (Revised 2020)"

# File paths
TEMPLATE_FILE = "ALA.xlsx"
OUTPUT_PDF_NAME = "Application_for_Leave.pdf"

# GUI settings
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 500
WINDOW_TITLE = f"{APP_NAME} - {FORM_TITLE}"

# Excel cell mappings for Civil Service Form No. 6
CELL_MAPPINGS = {
    'name': 'B8',
    'position': 'B9',
    'date_filing': 'G8',
    'inclusive_dates': 'B12',
    'working_days': 'G12'
}

# Position dropdown options
POSITION_OPTIONS = [
    "Administrative Aide VI",
    "Administrative Officer",
    "Clerk",
    "Secretary"
]

# Working days range (1-31)
WORKING_DAYS_RANGE = list(range(1, 32))

# Office designation
OFFICE_DESIGNATION = "LHIO - Digos"