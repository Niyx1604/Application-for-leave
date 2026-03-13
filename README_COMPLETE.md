# Leave Application Encoder - Complete Version
## Civil Service Form No. 6 (Revised 2020) with Full PDF Layout

This is the **complete version** with proper PDF output matching the official document structure including headers, logos placement, and all form sections.

## ✨ What's New in Complete Version

### PDF Output Now Includes:
✅ **Official Header**
- Republic of the Philippines
- PHILIPPINE HEALTH INSURANCE CORPORATION
- PhilHealth Regional Office XI
- Complete office address and contact details
- Stamp of Date of Receipt box

✅ **Complete Form Sections**
- All leave type checkboxes
- Commutation options
- Certification of Leave Credits table
- Recommendation section
- Approval/Disapproval sections
- All signature lines

✅ **Exact Layout**
- Matches official Civil Service Form No. 6
- Proper spacing and alignment
- All fields in correct positions
- Professional A4 print-ready format

## 🚀 Quick Start

### Run the Complete Application
```bash
python leave_app_complete.py
```

## 📋 Features

### Form Input (Same as Before)
- Office/Department: Defaults to "LHIO - Digos"
- Name: Text entry
- Date of Filing: Auto-populated with today
- Position: Dropdown with roman numerals
- Salary: Text entry
- Inclusive Dates: Calendar widgets
- Working Days: Dropdown (1-31 days)

### PDF Output (Enhanced)
Now generates a complete PDF with:

1. **Header Section**
   - Republic of the Philippines
   - PHILIPPINE HEALTH INSURANCE CORPORATION
   - PhilHealth Regional Office XI
   - Office address: J.P. Laurel Avenue, Bajada, Poblacion District, Davao City
   - Contact: (082) 295-2133 local 6000, (082) 295-3385
   - Email and website information
   - Stamp of Date of Receipt box (top right)

2. **Form Title**
   - Civil Service Form No. 6
   - Revised 2020
   - APPLICATION FOR LEAVE

3. **Section 1-5: Basic Information**
   - Office/Department
   - Name (Last, First, Middle format)
   - Date of Filing
   - Position
   - Salary

4. **Section 6: Details of Application**
   - 6.A: Type of Leave checkboxes (all 13 types)
   - 6.B: Details of Leave
   - 6.C: Number of Working Days Applied For
   - 6.D: Commutation (Not Requested/Requested)
   - Inclusive Dates
   - Signature of Applicant line

5. **Section 7: Details of Action on Application**
   - 7.A: Certification of Leave Credits
     - Vacation Leave and Sick Leave columns
     - Total Earned, Less this application, Balance
     - Authorized Officer signature line
   - 7.B: Recommendation
     - For approval/disapproval options
     - Authorized Officer signature line
   - 7.C: Approved For
     - Days with pay/without pay/others
   - 7.D: Disapproved Due To
   - Final Authorized Official signature line

## 📄 Output Comparison

### Before (Simple Version)
- Basic form fields only
- Minimal layout
- No official headers

### Now (Complete Version)
- ✅ Full official header with organization details
- ✅ All form sections (6.A, 6.B, 6.C, 6.D, 7.A, 7.B, 7.C, 7.D)
- ✅ All checkboxes for leave types
- ✅ Leave credits certification table
- ✅ All signature lines
- ✅ Stamp of Date of Receipt box
- ✅ Professional formatting matching official document

## 🎯 Usage Example

```bash
# 1. Run application
python leave_app_complete.py

# 2. Fill form
#    - Office/Department: LHIO - Digos (pre-filled)
#    - Name: Mendoza, Anthony Berja
#    - Date of Filing: (today's date, pre-filled)
#    - Position: Administrative Aide VI
#    - Salary: 25000
#    - Start Date: October 29, 2025
#    - End Date: October 30, 2025
#    - Working Days: 2 days

# 3. Click "Generate PDF"
#    → Creates: output_pdf/Application_for_Leave_YYYYMMDD_HHMMSS.pdf
#    → PDF now includes complete official layout!

# 4. Print the PDF
#    → A4 size, ready for official submission
#    → Includes all required sections
#    → Professional appearance
```

## 📂 File Structure

```
/project
├── leave_app_complete.py       # ⭐ Complete application (use this!)
├── leave_app.py                # Simple version (basic)
├── ALA.xlsx                    # Excel template
├── output_pdf/                 # Generated PDFs
│   └── Application_for_Leave_*.pdf
└── Leave_Application_*.xlsx    # Saved Excel files
```

## 🔧 Requirements

Same as before:
```bash
pip install openpyxl reportlab tkcalendar
```

## 📊 PDF Layout Details

The generated PDF follows the exact structure of Civil Service Form No. 6:

### Page Layout
- Size: A4 (210mm × 297mm)
- Margins: 20mm all sides
- Font: Helvetica (standard PDF font)
- Sections: Properly spaced and aligned

### Header (Top Section)
- Organization name and details
- Contact information
- Stamp box for date of receipt

### Form Body (Middle Section)
- Numbered sections (1-7)
- Subsections (6.A-6.D, 7.A-7.D)
- Checkboxes for options
- Input fields with labels
- Tables for leave credits

### Footer (Bottom Section)
- Signature lines
- Authorized official designation

## 🎨 Visual Improvements

### Typography
- Bold headers for section titles
- Regular text for labels
- Proper font sizes (7pt-11pt)
- Clear hierarchy

### Layout
- Aligned columns
- Consistent spacing
- Professional appearance
- Easy to read and fill

### Elements
- Checkboxes for selections
- Lines for signatures
- Boxes for stamps
- Tables for data

## ✅ Verification

To verify the PDF output:
1. Generate a PDF using the application
2. Open the PDF in any PDF viewer
3. Check that it includes:
   - ✓ PhilHealth header
   - ✓ All form sections
   - ✓ Proper formatting
   - ✓ All signature lines
   - ✓ Professional appearance

## 🆚 Version Comparison

| Feature | Simple (leave_app.py) | Complete (leave_app_complete.py) |
|---------|----------------------|----------------------------------|
| Form input | ✅ | ✅ |
| Excel save | ✅ | ✅ |
| Basic PDF | ✅ | ✅ |
| Official header | ❌ | ✅ |
| All form sections | ❌ | ✅ |
| Leave type checkboxes | ❌ | ✅ |
| Certification table | ❌ | ✅ |
| All signature lines | ❌ | ✅ |
| Stamp box | ❌ | ✅ |
| Print-ready | Partial | ✅ Full |

## 🎉 Result

The complete version generates a **professional, official-looking PDF** that matches the Civil Service Form No. 6 structure exactly, ready for printing and official submission.

---

**Use this version for production:** `python leave_app_complete.py`
