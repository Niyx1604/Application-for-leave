"""
GUI Interface Component
Handles user interaction and display for the leave application system.
"""

import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime, date
from typing import Dict, Any, List, Optional
from tkcalendar import Calendar, DateEntry


class LeaveApplicationGUI:
    """Main GUI interface for leave application data entry."""
    
    def __init__(self):
        """Initialize GUI interface."""
        self.root = tk.Tk()
        self.root.title("Leave Application Encoder - Civil Service Form No. 6")
        self.root.geometry("600x550")
        
        # Form variables
        self.name_var = tk.StringVar()
        self.position_var = tk.StringVar()
        self.date_filing_var = tk.StringVar()
        self.working_days_var = tk.StringVar()
        
        # Date variables for calendar widgets
        self.start_date = None
        self.end_date = None
        
        # Position options including "Administrative Aide VI" as specified
        self.position_options = [
            "Administrative Aide VI",
            "Administrative Officer", 
            "Administrative Assistant",
            "Clerk",
            "Secretary",
            "Office Assistant",
            "Records Officer"
        ]
        
        # Working days options (1-31)
        self.working_days_options = [str(i) for i in range(1, 32)]
        
        self.create_widgets()
        
    def create_widgets(self):
        """Create and layout GUI widgets."""
        # Main frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Title
        title_label = ttk.Label(main_frame, text="Civil Service Form No. 6 (Revised 2020)", 
                               font=("Arial", 14, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Name field
        ttk.Label(main_frame, text="Name:").grid(row=1, column=0, sticky=tk.W, pady=5)
        name_entry = ttk.Entry(main_frame, textvariable=self.name_var, width=40)
        name_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5)
        
        # Position field with enhanced dropdown
        ttk.Label(main_frame, text="Position:").grid(row=2, column=0, sticky=tk.W, pady=5)
        position_combo = ttk.Combobox(main_frame, textvariable=self.position_var, 
                                     values=self.position_options, state="readonly", width=37)
        position_combo.grid(row=2, column=1, sticky=(tk.W, tk.E), pady=5)
        
        # Date Filing field
        ttk.Label(main_frame, text="Date Filing:").grid(row=3, column=0, sticky=tk.W, pady=5)
        date_filing_entry = ttk.Entry(main_frame, textvariable=self.date_filing_var, width=40)
        date_filing_entry.grid(row=3, column=1, sticky=(tk.W, tk.E), pady=5)
        
        # Auto-populate with today's date
        self.date_filing_var.set(datetime.now().strftime("%B %d, %Y"))
        
        # Inclusive Dates section with calendar widgets
        dates_frame = ttk.LabelFrame(main_frame, text="Inclusive Dates", padding="10")
        dates_frame.grid(row=4, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=10)
        
        ttk.Label(dates_frame, text="Start Date:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.start_date_entry = DateEntry(dates_frame, width=18, background='darkblue',
                                         foreground='white', borderwidth=2, 
                                         date_pattern='mm/dd/yyyy')
        self.start_date_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), pady=5, padx=(5, 0))
        
        ttk.Label(dates_frame, text="End Date:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.end_date_entry = DateEntry(dates_frame, width=18, background='darkblue',
                                       foreground='white', borderwidth=2,
                                       date_pattern='mm/dd/yyyy')
        self.end_date_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5, padx=(5, 0))
        
        # Working Days field with dropdown (1-31 days)
        ttk.Label(main_frame, text="Working Days:").grid(row=5, column=0, sticky=tk.W, pady=5)
        working_days_combo = ttk.Combobox(main_frame, textvariable=self.working_days_var,
                                         values=self.working_days_options, state="readonly", width=37)
        working_days_combo.grid(row=5, column=1, sticky=(tk.W, tk.E), pady=5)
        
        # Generate PDF button
        generate_button = ttk.Button(main_frame, text="Generate PDF", 
                                   command=self.on_generate_pdf)
        generate_button.grid(row=6, column=0, columnspan=2, pady=20)
        
        # Configure column weights for resizing
        main_frame.columnconfigure(1, weight=1)
        dates_frame.columnconfigure(1, weight=1)
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
    
    def get_user_inputs(self) -> Dict[str, Any]:
        """Retrieve all form data as structured dictionary.
        
        Returns:
            Dictionary containing all form inputs
        """
        # Get dates from calendar widgets
        start_date = self.start_date_entry.get_date()
        end_date = self.end_date_entry.get_date()
        
        return {
            'name': self.name_var.get().strip(),
            'position': self.position_var.get(),
            'date_filing': self.date_filing_var.get().strip(),
            'inclusive_dates': [start_date.strftime("%B %d, %Y"), end_date.strftime("%B %d, %Y")],
            'working_days': self.working_days_var.get()
        }
    
    def validate_inputs(self) -> bool:
        """Perform comprehensive input validation.
        
        Returns:
            True if all inputs are valid, False otherwise
        """
        user_inputs = self.get_user_inputs()
        errors = []
        
        # Check required fields
        if not user_inputs['name']:
            errors.append("Name is required")
        
        if not user_inputs['position']:
            errors.append("Position must be selected")
        
        if not user_inputs['date_filing']:
            errors.append("Date Filing is required")
        
        # Calendar widgets always have dates, but validate they make sense
        try:
            start_date = self.start_date_entry.get_date()
            end_date = self.end_date_entry.get_date()
            
            if start_date > end_date:
                errors.append("Start date must be before or equal to end date")
                
        except Exception as e:
            errors.append("Invalid date selection")
        
        if not user_inputs['working_days']:
            errors.append("Working Days must be selected")
        
        if errors:
            self.show_error("\n".join(errors))
            return False
        
        return True
    
    def on_generate_pdf(self):
        """Handle Generate PDF button click."""
        if self.validate_inputs():
            user_inputs = self.get_user_inputs()
            print("Generating PDF with data:", user_inputs)
            # TODO: Integrate with PDF generator when implemented
            messagebox.showinfo("Success", "PDF generation functionality will be implemented in later tasks")
    
    def show_error(self, message: str):
        """Display validation error message to user.
        
        Args:
            message: Error message to display
        """
        messagebox.showerror("Validation Error", message)
    
    def run(self):
        """Start the GUI application."""
        self.root.mainloop()