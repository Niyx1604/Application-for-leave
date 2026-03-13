# ⭐ USE THIS VERSION - Complete Application

## 🎯 Which File to Run

```bash
python leave_app_complete.py
```

## Why This Version?

The **complete version** (`leave_app_complete.py`) generates PDFs that match the official Civil Service Form No. 6 exactly, including:

✅ Official PhilHealth header with logos placement
✅ Complete organization details
✅ All form sections (1-7 with subsections)
✅ All checkboxes for leave types
✅ Certification of Leave Credits table
✅ All signature lines
✅ Stamp of Date of Receipt box
✅ Professional A4 print-ready format

## Quick Comparison

### Simple Version (leave_app.py)
```
❌ Basic PDF with minimal layout
❌ Missing official headers
❌ Missing form sections
❌ Not suitable for official submission
```

### Complete Version (leave_app_complete.py) ⭐
```
✅ Full official layout
✅ PhilHealth header
✅ All form sections
✅ Ready for official submission
✅ Professional appearance
```

## Installation (One Time)

```bash
pip install openpyxl reportlab tkcalendar
```

## Usage

```bash
# 1. Run the complete application
python leave_app_complete.py

# 2. Fill the form (same as before)
#    - Office/Department: LHIO - Digos (pre-filled)
#    - Name: Your name
#    - Date of Filing: Today (pre-filled)
#    - Position: Select from dropdown
#    - Salary: Enter amount
#    - Dates: Pick from calendar
#    - Working Days: Select from dropdown

# 3. Generate PDF
#    Click "Generate PDF" button
#    → Creates complete official PDF in output_pdf/

# 4. Print or submit
#    The PDF is ready for official use!
```

## What You Get

### PDF Output Includes:

**Header Section:**
```
Republic of the Philippines
PHILIPPINE HEALTH INSURANCE CORPORATION
PhilHealth Regional Office XI
J.P. Laurel Avenue, Bajada, Poblacion District, Davao City
(082) 295-2133 local 6000, (082) 295-3385
✉ teamphilhealth11 ✉ teamphilhealth @ www.philhealth.gov.ph

[Stamp of Date of Receipt box in top right]
```

**Form Title:**
```
Civil Service Form No. 6
Revised 2020
APPLICATION FOR LEAVE
```

**All Form Sections:**
- Section 1-5: Basic information
- Section 6.A: Type of Leave (13 options with checkboxes)
- Section 6.B: Details of Leave
- Section 6.C: Number of Working Days
- Section 6.D: Commutation options
- Section 7.A: Certification of Leave Credits (table)
- Section 7.B: Recommendation
- Section 7.C: Approved For
- Section 7.D: Disapproved Due To
- All signature lines for applicant and authorized officers

## File Locations

```
/project
├── leave_app_complete.py    ← USE THIS! ⭐
├── leave_app.py             ← Old simple version
├── ALA.xlsx                 ← Excel template
└── output_pdf/              ← Your PDFs go here
    └── Application_for_Leave_*.pdf
```

## Verification

After generating a PDF, open it and verify:
- ✓ PhilHealth header is present
- ✓ All sections are visible
- ✓ Form looks professional
- ✓ Ready to print on A4 paper

## Support Files

- **README_COMPLETE.md** - Full documentation
- **QUICK_START.md** - Quick guide
- **verify_setup.py** - Check if everything works

## Troubleshooting

### "Module not found"
```bash
pip install openpyxl reportlab tkcalendar
```

### "Template not found"
Make sure `ALA.xlsx` is in the same folder

### "PDF looks incomplete"
Make sure you're running `leave_app_complete.py` not `leave_app.py`

## Summary

**Always use:** `python leave_app_complete.py`

This generates the complete, official-looking PDF that's ready for submission!

---

**Ready?** Run: `python leave_app_complete.py`
