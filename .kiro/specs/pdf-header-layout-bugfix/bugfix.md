# Bugfix Requirements Document

## Introduction

The PDF header rendering system in the leave application encoder has critical layout issues causing text overlap, incorrect logo placement, and poor vertical spacing. This bugfix addresses multiple layout problems where header elements are rendered without proper positioning and alignment compared to the reference image layout. The issues include: overlapping text elements, logos not positioned horizontally side-by-side, form metadata boxes floating outside the main border instead of being positioned inside, missing clear text hierarchy, and inconsistent spacing throughout. The bug affects the visual presentation and readability of the generated PDF documents, making them unprofessional and not matching the official reference layout.

## Bug Analysis

### Current Behavior (Defect)

1.1 WHEN the system renders header text lines (Republic of the Philippines, PHILIPPINE HEALTH INSURANCE CORPORATION, PhilHealth Regional Office XI, address, email, phone) THEN the system prints all lines at the same Y coordinate, causing complete text overlap

1.2 WHEN the system positions the PhilHealth and Bagong Pilipinas logos THEN the system places them with overlapping elements instead of positioning them horizontally side-by-side at the same Y-coordinate above the organization text

1.3 WHEN the system renders the space between "APPLICATION FOR LEAVE" title and "1. OFFICE/DEPARTMENT" section THEN the system creates a massive empty gap (approximately ⅓ of the page)

1.4 WHEN the system renders "Civil Service Form No. 6" and "Revised 2020" THEN the system positions them floating outside the main border instead of in a small box in the top-left corner INSIDE the main border

1.5 WHEN the system renders "Stamp of Date of Receipt" box THEN the system positions it with inconsistent margins instead of in the top-right corner INSIDE the main border, properly aligned

1.6 WHEN the system renders header text hierarchy THEN the system provides no proper line spacing between elements, mashing them together instead of showing clear hierarchy (logos at top, then Republic text, then PHILHEALTH CORPORATION bold, then Regional Office, then address/contact, then APPLICATION FOR LEAVE title)

1.7 WHEN the system renders the email line "teamphilhealth@philhealth.gov.ph" THEN the system prints it inside the same region as the title block, causing overlap

1.8 WHEN the system executes sequential drawImage()/drawString() calls THEN the system does not manage Y-axis positioning, causing elements to collide

1.9 WHEN the system renders both PhilHealth and Bagong Pilipinas logos THEN the system fails to arrange them horizontally at the same Y-coordinate with proper spacing between them

1.10 WHEN the system renders the header structure THEN the system fails to center "APPLICATION FOR LEAVE" below the horizontally-aligned logos as shown in the reference layout

1.11 WHEN the system renders overall spacing THEN the system creates text overlap and excessive gaps instead of consistent, professional spacing with no overlaps throughout the header

### Expected Behavior (Correct)

2.1 WHEN the system renders header text lines THEN the system SHALL print each line at a distinct Y coordinate with proper vertical spacing (4-5mm between lines)

2.2 WHEN the system positions the PhilHealth and Bagong Pilipinas logos THEN the system SHALL place them horizontally side-by-side at the same Y-coordinate at the top of the header, with proper spacing between them

2.3 WHEN the system renders the space between "APPLICATION FOR LEAVE" title and "1. OFFICE/DEPARTMENT" section THEN the system SHALL create appropriate spacing (10-15mm) without excessive gaps

2.4 WHEN the system renders "Civil Service Form No. 6" and "Revised 2020" THEN the system SHALL position them in a small box in the top-left corner INSIDE the main border as shown in the reference layout

2.5 WHEN the system renders "Stamp of Date of Receipt" box THEN the system SHALL position it in the top-right corner INSIDE the main border, properly aligned

2.6 WHEN the system renders header text hierarchy THEN the system SHALL display clear hierarchy: logos at top (horizontally aligned), then "Republic of the Philippines" centered, then "PHILIPPINE HEALTH INSURANCE CORPORATION" centered and bold, then "PhilHealth Regional Office XI" centered, then address and contact details centered in smaller font, then "APPLICATION FOR LEAVE" centered, bold, and larger

2.7 WHEN the system renders the email line THEN the system SHALL position it at its own Y coordinate below the phone line with proper spacing

2.8 WHEN the system executes sequential drawImage()/drawString() calls THEN the system SHALL decrement the Y-axis position after each element to prevent collisions

2.9 WHEN the system renders both logos THEN the system SHALL ensure they are horizontally aligned at the same Y-coordinate, positioned above the organization text

2.10 WHEN the system renders "APPLICATION FOR LEAVE" title THEN the system SHALL center it below the horizontally-aligned logos as shown in the reference layout

2.11 WHEN the system renders overall spacing THEN the system SHALL demonstrate consistent, professional spacing throughout with no text overlap or excessive gaps, matching the reference image layout

### Unchanged Behavior (Regression Prevention)

3.1 WHEN the system renders form body tables THEN the system SHALL CONTINUE TO maintain correct alignment and structure

3.2 WHEN the system inserts data into form fields THEN the system SHALL CONTINUE TO populate values correctly

3.3 WHEN the system renders table borders THEN the system SHALL CONTINUE TO display them with proper structure

3.4 WHEN the system processes leave type checkboxes THEN the system SHALL CONTINUE TO render them correctly

3.5 WHEN the system formats dates and working days THEN the system SHALL CONTINUE TO display them in the correct format

3.6 WHEN the system renders the signature sections THEN the system SHALL CONTINUE TO position them correctly

3.7 WHEN the system saves the PDF file THEN the system SHALL CONTINUE TO create valid PDF documents

3.8 WHEN the system handles logo files that don't exist THEN the system SHALL CONTINUE TO gracefully handle missing files without crashing
