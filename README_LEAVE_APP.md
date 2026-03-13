# Leave Application Encoder
## Civil Service Form No. 6 (Revised 2020)

This Python application preserves the **exact structure** of your Excel template and generates identical PDF output.

## Features

✅ **Preserves Excel Structure** - All labels, formatting, and layout remain exactly as in the original spreadsheet
✅ **Default Values** - Office/Department defaults to "LHIO - Digos" (editable)
✅ **Auto-Population** - Date of Filing automatically set to today's date
✅ **Calendar Widgets** - Easy date selection for Inclusive Dates
✅ **Position Dropdown** - All positions with roman numerals preserved:
   - Administrative Aide I through VI
   - Social Insurance Assistant I through V
   - Social Insurance Officer I through III
   - Chief Social Insurance Officer I
✅ **Working Days Format** - Dropdown 1-31 with proper "day/days" format
✅ **Dual Output** - Save to Excel AND generate PDF
✅ **Offline** - Works completely offline

## Installation

1. Install required libraries:
```bash
pip install openpyxl reportlab tkcalendar
```

2. Ensure `ALA.xlsx` is in the same directory

## Usage

Run the application:
```bash
python leave_app.py
```

### Form Fields:
- **Office/Department**: Defaults to "LHIO - Digos" (editable)
- **Name**: Enter employee name
- **Date of Filing**: Auto-populated with today (editable)
- **Position**: Select from dropdown
- **Salary**: Enter salary (optional)
- **Inclusive Dates**: Select start and end dates using calendar
- **Working Days**: Select from dropdown (1-31 days)

### Buttons:
- **Generate PDF**: Creates A4 PDF in `output_pdf/` folder
- **Save to Excel**: Saves data to new Excel file with timestamp
- **Clear Form**: Resets all fields (keeps Office/Department default)

## File Structure

```
/project
├── ALA.xlsx                    # Original Excel template (master)
├── leave_app.py                # Main application
├── output_pdf/                 # Generated PDFs
└── Leave_Application_*.xlsx    # Saved Excel files
```

## Important Notes

- The Excel file `ALA.xlsx` is the **master template**
- All original labels and structure are preserved
- PDF output matches Excel layout exactly
- Files are saved with timestamps to avoid overwriting

## Requirements

- Python 3.7+
- openpyxl
- reportlab
- tkcalendar
- tkinter (included with Python)
