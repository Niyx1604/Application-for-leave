# Leave Application Encoder System

A Python desktop application that automates the data entry process for Civil Service Form No. 6 (Revised 2020) leave applications. The system maintains the exact layout and functionality of the original Excel template while providing a streamlined GUI interface and generating print-ready PDF outputs.

## Features

- **Template Preservation**: Maintains exact Excel template layout and formatting
- **GUI Interface**: Simple tkinter-based data entry interface
- **Automated Data Population**: Auto-fills Date Filing with current date
- **PDF Generation**: Creates print-ready PDF files identical to Excel template
- **Data Validation**: Comprehensive input validation and error handling
- **Multiple Date Formats**: Supports single-day, consecutive, and non-consecutive leave dates

## Requirements

- Python 3.7+
- openpyxl 3.1.2
- reportlab 4.0.7

## Installation

1. Clone or download the project
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Ensure the Excel template file `ALA.xlsx` is in the project directory

## Usage

Run the application:
```bash
python main.py
```

The GUI will open allowing you to:
1. Enter employee name and select position
2. Set inclusive dates for leave period
3. Select number of working days
4. Generate PDF output

## Project Structure

```
leave-application-encoder/
├── main.py                 # Main application entry point
├── requirements.txt        # Python dependencies
├── config.py              # Configuration settings
├── README.md              # This file
├── ALA.xlsx               # Excel template (Civil Service Form No. 6)
└── src/                   # Source code modules
    ├── __init__.py
    ├── gui_interface.py   # GUI components
    ├── data_encoder.py    # Data processing and validation
    ├── template_processor.py  # Excel template handling
    └── pdf_generator.py   # PDF generation
```

## Template File

The system requires the Civil Service Form No. 6 (Revised 2020) Excel template file named `ALA.xlsx` to be present in the project root directory. This template is used as the basis for all leave application processing.

## Output

Generated PDF files are saved as `Application_for_Leave.pdf` in the project directory. The PDF maintains identical layout, formatting, and interactive elements as the original Excel template for professional submission.

## Development Status

This is the initial project structure setup. Core functionality will be implemented in subsequent development phases following the task breakdown in the project specification.