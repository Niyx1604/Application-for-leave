# Quick Start Guide

## Run the Application

```bash
python leave_app.py
```

## What You'll See

A window with the exact form structure from your Excel file:

```
┌─────────────────────────────────────────────┐
│  CIVIL SERVICE FORM NO. 6                   │
│  (Revised 2020)                             │
│  APPLICATION FOR LEAVE                      │
├─────────────────────────────────────────────┤
│  Office/Department: [LHIO - Digos]          │
│  Name: [_____________________]              │
│  Date of Filing: [📅 Today's Date]          │
│  Position: [▼ Select Position]              │
│  Salary: [_____________________]            │
│                                             │
│  ┌─ Inclusive Dates ──────────────┐        │
│  │  Start Date: [📅 Calendar]     │        │
│  │  End Date:   [📅 Calendar]     │        │
│  └────────────────────────────────┘        │
│                                             │
│  Working Days: [▼ 1 day - 31 days]         │
│                                             │
│  [Generate PDF] [Save to Excel] [Clear]    │
└─────────────────────────────────────────────┘
```

## Key Features

### 1. Preserved Defaults
- **Office/Department** starts with "LHIO - Digos" (you can change it)
- **Date of Filing** auto-fills with today's date

### 2. Easy Date Selection
- Click calendar icons to pick dates
- No manual typing needed

### 3. Position Dropdown
All positions with roman numerals:
- Administrative Aide I, II, III, IV, V, VI
- Social Insurance Assistant I, II, III, IV, V
- Social Insurance Officer I, II, III
- Chief Social Insurance Officer I

### 4. Working Days Format
Select from dropdown:
- 1 day
- 2 days
- 3 days
- ... up to 31 days

## Output

### Generate PDF
- Creates: `output_pdf/Application_for_Leave_YYYYMMDD_HHMMSS.pdf`
- Format: A4 size, print-ready
- Layout: Identical to Excel

### Save to Excel
- Creates: `Leave_Application_YYYYMMDD_HHMMSS.xlsx`
- Preserves all Excel formatting
- Uses exact cell locations from template

## Example Workflow

1. **Open Application**
   ```bash
   python leave_app.py
   ```

2. **Fill Form**
   - Name: "Mendoza, Anthony Berja"
   - Position: Select "Administrative Aide VI"
   - Dates: Pick from calendar
   - Working Days: Select "2 days"

3. **Generate Output**
   - Click "Generate PDF" → Creates PDF in `output_pdf/`
   - Click "Save to Excel" → Creates Excel file

4. **Clear for Next Entry**
   - Click "Clear Form"
   - Office/Department stays "LHIO - Digos"
   - Ready for next application

## Troubleshooting

### "Template file not found"
- Make sure `ALA.xlsx` is in the same folder as `leave_app.py`

### "Module not found"
- Install missing library:
  ```bash
  pip install openpyxl reportlab tkcalendar
  ```

### Calendar not showing
- Make sure `tkcalendar` is installed:
  ```bash
  pip install tkcalendar
  ```

## Notes

- All original Excel labels are preserved
- No redesign or restructuring
- Excel file is the master template
- PDF output matches Excel exactly
