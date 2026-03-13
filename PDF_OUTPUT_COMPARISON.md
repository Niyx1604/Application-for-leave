# PDF Output Comparison

## Visual Comparison: Simple vs Complete

### Simple Version (leave_app.py)
```
┌─────────────────────────────────────────┐
│                                         │
│   CIVIL SERVICE FORM NO. 6              │
│   (Revised 2020)                        │
│   APPLICATION FOR LEAVE                 │
│                                         │
│   Office/Department: LHIO - Digos       │
│   Name: Mendoza, Anthony Berja          │
│   Date of Filing: 10/29/2025            │
│   Position: Administrative Aide VI      │
│   Salary: 25000                         │
│   Inclusive Dates: Oct 29-30, 2025      │
│   Working Days: 2 days                  │
│                                         │
│   [End of PDF]                          │
└─────────────────────────────────────────┘
```
**Issues:**
- ❌ No official header
- ❌ No organization details
- ❌ Missing form sections
- ❌ No checkboxes
- ❌ No signature lines
- ❌ Not suitable for official use

---

### Complete Version (leave_app_complete.py) ⭐
```
┌─────────────────────────────────────────────────────────────┐
│                                                   ┌─────────┐│
│   Republic of the Philippines                    │ Stamp of││
│   PHILIPPINE HEALTH INSURANCE CORPORATION         │ Date of ││
│   PhilHealth Regional Office XI                   │ Receipt ││
│   J.P. Laurel Avenue, Bajada, Poblacion District │         ││
│   Davao City                                      └─────────┘│
│   (082) 295-2133 local 6000, (082) 295-3385                 │
│   ✉ teamphilhealth11 @ www.philhealth.gov.ph                │
│                                                              │
│              Civil Service Form No. 6                        │
│                   Revised 2020                               │
│            APPLICATION FOR LEAVE                             │
│                                                              │
│ 1. OFFICE/DEPARTMENT    2. NAME: (Last) (First) (Middle)    │
│    LHIO - Digos                                              │
│                                                              │
│ 3. DATE OF FILING: October 29, 2025                         │
│ 4. POSITION: Administrative Aide VI                         │
│ 5. SALARY: 25000                                            │
│                                                              │
│ 6. DETAILS OF APPLICATION                                   │
│                                                              │
│ 6.A TYPE OF LEAVE TO BE AVAILED OF                          │
│   ☐ Vacation Leave (Sec. 51, Rule XVI...)                   │
│   ☐ Mandatory/Forced Leave (Sec. 25, Rule XVI...)           │
│   ☐ Sick Leave (Sec. 43, Rule XVI...)                       │
│   ☐ Maternity Leave (R.A. No. 11210...)                     │
│   ☐ Paternity Leave (R.A. No. 8187...)                      │
│   ☐ Special Privilege Leave (Sec. 21, Rule XVI...)          │
│   ☐ Solo Parent Leave (RA No. 8972...)                      │
│   ☐ Study Leave (Sec. 68, Rule XVI...)                      │
│   ☐ 10-Day VAWC Leave (RA No. 9262...)                      │
│   ☐ Rehabilitation Privilege (Sec. 55, Rule XVI...)         │
│   ☐ Special Leave Benefits for Women (RA No. 9710...)       │
│   ☐ Special Emergency (Calamity) Leave (CSC MC No. 2...)    │
│   ☐ Adoption Leave (R.A. No. 8552)                          │
│                                                              │
│ 6.B DETAILS OF LEAVE                                         │
│   In case of Vacation/Special Privilege Leave:              │
│   Within the Philippines _________________________          │
│   Abroad (Specify) _______________________________          │
│                                                              │
│ 6.C NUMBER OF WORKING DAYS APPLIED FOR                       │
│     2 days                                                   │
│                                                              │
│ 6.D COMMUTATION                                              │
│   ☐ Not Requested                                            │
│   ☐ Requested                                                │
│                                                              │
│   INCLUSIVE DATES                                            │
│   October 29, 2025 - October 30, 2025                       │
│                                                              │
│                          _____________________________       │
│                          (Signature of Applicant)            │
│                                                              │
│ 7. DETAILS OF ACTION ON APPLICATION                          │
│                                                              │
│ 7.A CERTIFICATION OF LEAVE CREDITS                           │
│   As of _______________________                              │
│                                                              │
│            Vacation Leave    Sick Leave                      │
│   Total Earned                                               │
│   Less this application                                      │
│   Balance                                                    │
│                                                              │
│   _____________________    _____________________             │
│   (Authorized Officer)     (Authorized Officer)              │
│                                                              │
│ 7.B RECOMMENDATION                                           │
│   For approval                                               │
│   For disapproval due to _________________________           │
│                                                              │
│ 7.C APPROVED FOR:          7.D DISAPPROVED DUE TO:          │
│   _____ days with pay      _____________________________     │
│   _____ days without pay   _____________________________     │
│   _____ others (Specify)                                     │
│                                                              │
│                    _____________________________             │
│                    (Authorized Official)                     │
└─────────────────────────────────────────────────────────────┘
```

**Features:**
- ✅ Official PhilHealth header
- ✅ Complete organization details
- ✅ All form sections (1-7)
- ✅ All subsections (6.A-6.D, 7.A-7.D)
- ✅ 13 leave type checkboxes
- ✅ Leave credits certification table
- ✅ All signature lines
- ✅ Stamp of Date of Receipt box
- ✅ Professional formatting
- ✅ Ready for official submission

## Side-by-Side Feature Comparison

| Feature | Simple | Complete |
|---------|--------|----------|
| **Header** |
| Organization name | ❌ | ✅ |
| Office address | ❌ | ✅ |
| Contact details | ❌ | ✅ |
| Stamp box | ❌ | ✅ |
| **Form Sections** |
| Basic info (1-5) | ✅ | ✅ |
| Leave types (6.A) | ❌ | ✅ 13 options |
| Leave details (6.B) | ❌ | ✅ |
| Working days (6.C) | ✅ | ✅ |
| Commutation (6.D) | ❌ | ✅ |
| **Action Sections** |
| Leave credits (7.A) | ❌ | ✅ Table |
| Recommendation (7.B) | ❌ | ✅ |
| Approval (7.C) | ❌ | ✅ |
| Disapproval (7.D) | ❌ | ✅ |
| **Signatures** |
| Applicant | ❌ | ✅ |
| Authorized Officers | ❌ | ✅ 3 lines |
| **Overall** |
| Professional | ⚠️ Basic | ✅ Full |
| Official use | ❌ No | ✅ Yes |
| Print-ready | ⚠️ Partial | ✅ Complete |

## File Size Comparison

- Simple PDF: ~20 KB
- Complete PDF: ~35 KB (includes all sections)

## Print Quality

### Simple Version
- Basic layout
- Missing sections
- Needs manual completion
- Not suitable for submission

### Complete Version
- Professional layout
- All sections included
- Ready to sign and submit
- Matches official form exactly

## Recommendation

**Always use the Complete Version** (`leave_app_complete.py`) for:
- ✅ Official submissions
- ✅ Professional appearance
- ✅ Complete documentation
- ✅ Proper record keeping

The simple version is only for reference or testing purposes.

---

**Use:** `python leave_app_complete.py` for production!
