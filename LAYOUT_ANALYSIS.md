# Layout Analysis: Excel Template vs Current Output

## Issues Identified

Based on the Excel template data and the current PDF output, here are the key differences:

### 1. Header Issues
**Excel Template:**
- Simple header: "Civil Service Form No. 6"
- "Revised 2020"
- "APPLICATION FOR LEAVE"
- "Stamp of Date of Receipt" box in top right

**Current Output:**
- ❌ Includes PhilHealth-specific headers not in Excel
- ❌ Complex logo system not needed for basic template
- ✅ Has correct form title structure

### 2. Section 1 & 2 Layout
**Excel Template:**
```
1. OFFICE/DEPARTMENT          2. NAME: (Last)    (First)    (Middle)
   LHIO - Digos                  Mendoza        Anthony      Berja

3. DATE OF FILING ______       4. POSITION ______    5. SALARY ______
   October 14, 2025               Administrative Aide VI    [salary]
```

**Current Status:**
- ✅ Basic structure correct
- ⚠️ Positioning needs fine-tuning
- ⚠️ Underlines need to match Excel exactly

### 3. Section 6 - Leave Types
**Excel Template:**
- Has all 13 leave types with checkboxes
- Two-column layout: Types on left, Details on right
- Specific text formatting and positioning

**Current Status:**
- ✅ Has all leave types
- ✅ Two-column structure
- ⚠️ Checkbox positioning needs adjustment
- ⚠️ Text wrapping needs refinement

### 4. Section 6C & 6D
**Excel Template:**
```
6.C NUMBER OF WORKING DAYS APPLIED FOR    6.D COMMUTATION
    2 Days                                     ☐ Not Requested
                                              ☐ Requested
    INCLUSIVE DATES
    October 29-30, 2025
```

**Current Status:**
- ✅ Basic structure present
- ⚠️ Date formatting needs to match Excel
- ⚠️ Positioning adjustments needed

### 5. Section 7 - Approval Section
**Excel Template:**
- Complex approval workflow section
- Multiple signature lines
- Leave credits table

**Current Status:**
- ✅ Structure implemented
- ⚠️ Positioning and formatting need refinement

## Priority Fixes Needed

1. **Remove PhilHealth-specific headers** ✅ DONE
2. **Fix section positioning** - In progress
3. **Adjust underline positioning** - In progress  
4. **Refine checkbox positioning**
5. **Match date formatting exactly**
6. **Fine-tune text positioning**

## Next Steps

1. Test the current corrected version
2. Compare output with Excel template
3. Make incremental adjustments
4. Verify all data fields match exactly