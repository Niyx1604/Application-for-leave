# 🚀 START HERE - Leave Application Encoder

## What You Have

A complete Python application that converts your Excel form into an encoding system while **preserving everything exactly as it is**.

## ✅ Verification Complete

All checks passed! Your system is ready to use.

## 🎯 Quick Start (3 Steps)

### Step 1: Run the Application
```bash
python leave_app.py
```

### Step 2: Fill the Form
- All fields match your Excel file exactly
- Office/Department defaults to "LHIO - Digos"
- Date of Filing auto-fills with today
- Use calendar widgets for dates
- Select position from dropdown

### Step 3: Generate Output
- Click "Generate PDF" → Creates print-ready A4 PDF
- Click "Save to Excel" → Saves to new Excel file
- Both outputs preserve exact Excel structure

## 📚 Documentation Files

1. **QUICK_START.md** - Step-by-step usage guide
2. **README_LEAVE_APP.md** - Complete documentation
3. **PRESERVATION_REPORT.md** - What was preserved from Excel
4. **EXCEL_TO_APP_MAPPING.md** - Cell-by-cell mapping
5. **IMPLEMENTATION_SUMMARY.md** - Full implementation details

## 🎨 What Makes This Special

### Your Excel File is Sacred
- ✅ No redesign
- ✅ No renaming
- ✅ No restructuring
- ✅ No layout changes
- ✅ All labels preserved
- ✅ All formatting preserved
- ✅ Default values preserved

### Enhanced with Input Controls
- ✅ Calendar widgets for dates
- ✅ Dropdowns for Position (with roman numerals)
- ✅ Dropdown for Working Days (1-31 with "day/days")
- ✅ Auto-population (Date of Filing = today)
- ✅ Validation for required fields

### Perfect Output
- ✅ PDF: A4 size, print-ready, identical layout
- ✅ Excel: Same cells, same formatting, same structure

## 📋 Position Options (Exact)

```
Administrative Aide I
Administrative Aide II
Administrative Aide III
Administrative Aide IV
Administrative Aide V
Administrative Aide VI
Social Insurance Assistant I
Social Insurance Assistant II
Social Insurance Assistant III
Social Insurance Assistant IV
Social Insurance Assistant V
Social Insurance Officer I
Social Insurance Officer II
Social Insurance Officer III
Chief Social Insurance Officer I
```

## 💾 Output Locations

- **PDFs**: `output_pdf/Application_for_Leave_YYYYMMDD_HHMMSS.pdf`
- **Excel**: `Leave_Application_YYYYMMDD_HHMMSS.xlsx`

## 🔧 Troubleshooting

### Application won't start?
```bash
python verify_setup.py
```
This will check all requirements.

### Missing libraries?
```bash
pip install openpyxl reportlab tkcalendar
```

### Template not found?
Make sure `ALA.xlsx` is in the same folder as `leave_app.py`

## 📖 Example Usage

```bash
# 1. Start application
python leave_app.py

# 2. Form opens with:
#    - Office/Department: "LHIO - Digos" (already filled)
#    - Date of Filing: Today's date (already filled)
#    - Other fields: Empty, ready for input

# 3. Fill in:
#    - Name: "Mendoza, Anthony Berja"
#    - Position: Select "Administrative Aide VI"
#    - Salary: "25000" (optional)
#    - Start Date: Pick from calendar
#    - End Date: Pick from calendar
#    - Working Days: Select "2 days"

# 4. Click "Generate PDF"
#    → Creates: output_pdf/Application_for_Leave_20240115_143022.pdf

# 5. Click "Save to Excel"
#    → Creates: Leave_Application_20240115_143022.xlsx

# 6. Click "Clear Form" to start next application
#    → Office/Department stays "LHIO - Digos"
#    → Ready for next entry
```

## 🎉 You're Ready!

Your application is complete and ready to use. The Excel file structure is preserved exactly, and you can now encode leave applications efficiently.

**Run it now:**
```bash
python leave_app.py
```

---

**Need help?** Check the documentation files listed above for detailed information.
