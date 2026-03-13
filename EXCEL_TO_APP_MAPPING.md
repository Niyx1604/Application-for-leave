# Excel to Application Mapping

## Direct Cell Mapping

| Excel Cell | Excel Content | Application Field | Input Type | Default Value |
|------------|---------------|-------------------|------------|---------------|
| A1 | CIVIL SERVICE FORM NO. 6 | Title Label | Static Text | (preserved) |
| A2 | (Revised 2020) | Subtitle Label | Static Text | (preserved) |
| A3 | APPLICATION FOR LEAVE | Form Name Label | Static Text | (preserved) |
| A7 | Office/Department: | Field Label | Static Text | (preserved) |
| B7 | LHIO - Digos | Office/Department | Text Entry | "LHIO - Digos" |
| A8 | Name: | Field Label | Static Text | (preserved) |
| B8 | (empty) | Name | Text Entry | (empty) |
| F8 | Date of Filing: | Field Label | Static Text | (preserved) |
| G8 | (empty) | Date of Filing | Calendar Widget | Today's Date |
| A9 | Position: | Field Label | Static Text | (preserved) |
| B9 | (empty) | Position | Dropdown | (empty) |
| F9 | Salary: | Field Label | Static Text | (preserved) |
| G9 | (empty) | Salary | Text Entry | (empty) |
| A12 | Inclusive Dates: | Field Label | Static Text | (preserved) |
| B12 | (empty) | Inclusive Dates | Calendar Widgets | (empty) |
| F12 | Working Days: | Field Label | Static Text | (preserved) |
| G12 | (empty) | Working Days | Dropdown | (empty) |

## Field Behavior Comparison

### Office/Department
```
Excel:    B7 = "LHIO - Digos"
App:      Text Entry with default "LHIO - Digos"
Behavior: User can edit but defaults to Excel value
```

### Name
```
Excel:    B8 = (empty)
App:      Text Entry
Behavior: User enters name
```

### Date of Filing
```
Excel:    G8 = (empty)
App:      Calendar Widget
Behavior: Auto-populated with today, user can change
```

### Position
```
Excel:    B9 = (empty)
App:      Dropdown with 15 options
Behavior: User selects from list with roman numerals
Options:  Administrative Aide I-VI
          Social Insurance Assistant I-V
          Social Insurance Officer I-III
          Chief Social Insurance Officer I
```

### Salary
```
Excel:    G9 = (empty)
App:      Text Entry
Behavior: User enters salary (optional)
```

### Inclusive Dates
```
Excel:    B12 = (empty)
App:      Two Calendar Widgets (Start & End)
Behavior: User picks dates from calendar
Format:   "Month DD, YYYY - Month DD, YYYY"
```

### Working Days
```
Excel:    G12 = (empty)
App:      Dropdown (1-31)
Behavior: User selects from dropdown
Format:   "1 day", "2 days", ..., "31 days"
```

## Data Flow

### Input Flow (User → Excel)
```
User fills form
    ↓
Validates required fields
    ↓
Writes to exact Excel cells
    ↓
Saves as new file with timestamp
```

### Output Flow (User → PDF)
```
User fills form
    ↓
Validates required fields
    ↓
Generates PDF with identical layout
    ↓
Saves to output_pdf/ folder
```

## Preservation Rules Applied

1. ✅ **All labels preserved** - No renaming
2. ✅ **Cell locations preserved** - Same cells used
3. ✅ **Default values preserved** - "LHIO - Digos" kept
4. ✅ **Layout preserved** - Same field arrangement
5. ✅ **Text preserved** - Exact capitalization
6. ✅ **Structure preserved** - No reorganization

## Enhancement Rules Applied

1. ✅ **Input controls added** - For user data entry
2. ✅ **Auto-population added** - Date of Filing = today
3. ✅ **Dropdowns added** - Position and Working Days
4. ✅ **Calendar widgets added** - For date selection
5. ✅ **Validation added** - Required field checking
6. ✅ **PDF generation added** - A4 print-ready output

## Result

The application is a **faithful digital representation** of the Excel form:
- Same structure
- Same labels
- Same data locations
- Same default values
- Enhanced with input controls
- Generates identical PDF output
