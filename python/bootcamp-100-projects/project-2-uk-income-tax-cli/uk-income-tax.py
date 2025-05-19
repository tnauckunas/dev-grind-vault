import tkinter as tk
import re
from tkinter import ttk
from tkinter import messagebox

# Step 1: Main Salary Input Window
def open_next_window(amount, frequency):
    root.destroy()  # close first window

    next_win = tk.Tk()
    next_win.title("Step 2: Pension Question")
    next_win.geometry("400x250")
    next_win.configure(bg="#1e1e1e")

    tk.Label(next_win, text="Are you a Pensioner?", fg="white", bg="#1e1e1e", font=("Arial", 14)).pack(pady=10)

    pension_var = tk.StringVar()

    tk.Radiobutton(next_win, text="Yes", variable=pension_var, value="Yes",
                   fg="white", bg="#1e1e1e", selectcolor="#333", font=("Arial", 12)).pack()
    tk.Radiobutton(next_win, text="No", variable=pension_var, value="No",
                   fg="white", bg="#1e1e1e", selectcolor="#333", font=("Arial", 12)).pack()

    user_data = {
        "amount": amount,
        "frequency": frequency
    }
    
    def continue_from_pension(user_data):
        choice = pension_var.get() 
        if not choice:
            messagebox.showerror("Error", "Please select Yes or No.")
            return
        
        user_data["Pensioner"] = choice
        next_win.destroy()  # close pension question window
        open_summary_window(user_data)

        tk.Button(next_win, text="Continue", command=lambda: continue_from_pension(user_data),
          bg="#00a651", fg="white", font=("Arial", 12)).pack(pady=15)
        
        next_win.mainloop()
    tk.Button(next_win, text="Continue", command=lambda: continue_from_pension(user_data),
              bg="#00a651", fg="white", font=("Arial", 12)).pack(pady=15)  
    
def is_valid_tax_code(code):
    """
    Valid UK tax codes include:
    - 1257L (most common)
    - K497 (K-prefix)
    - S1257L (Scottish)
    - SK497 (Scottish + K)
    """
    code = code.strip().upper()
    pattern = r"^(S)?(K)?\d{3,4}L$"
    return re.match(pattern, code) is not None

def submit():
    amount = amount_entry.get()
    frequency = freq_var.get()
    
    if not amount or not frequency:
        messagebox.showerror("Error", "Please enter amount and select frequency.")
        return
    
    try:
        float(amount)
    except ValueError:
        messagebox.showerror("Error", "Amount must be a number.")
        return
    
    # Open next window with passed data
    open_next_window(amount, frequency)

def open_summary_window(user_data):
    win3 = tk.Tk()
    win3.title("Income Summary & Optional Questions")
    win3.geometry("500x650")
    win3.configure(bg="#1e1e1e")

    # Title
    tk.Label(win3, text="Your Income", fg="white", bg="#1e1e1e", font=("Arial", 16, "bold")).pack(pady=10)

    # Summary Section
    income_str = f"£{user_data['amount']} every {user_data['frequency'].lower()}"
    tk.Label(win3, text=f"Gross income: {income_str}", fg="white", bg="#1e1e1e", font=("Arial", 12)).pack()
    tk.Label(win3, text=f"Over State Pension Age: {user_data['Pensioner']}", fg="white", bg="#1e1e1e", font=("Arial", 12)).pack()
    tk.Label(win3, text="\nAdditional Questions (Optional)", fg="white", bg="#1e1e1e", font=("Arial", 14, "bold")).pack(pady=10)

    # --- Optional Inputs ---
    # Tax Code
    tk.Label(win3, text="Tax Code:", fg="white", bg="#1e1e1e", font=("Arial", 12)).pack()
    tax_codes = ["1257L", "K497L", "S1257L", "SK497L", "I don't know"]

    tax_code_var = tk.StringVar()
    tax_code_dropdown = ttk.Combobox(win3, textvariable=tax_code_var, values=tax_codes, state="readonly", font=("Arial", 12))
    tax_code_dropdown.set("1257L")  # Default value
    tax_code_dropdown.pack(pady=5)

    # Scottish Tax
    scottish_tax_var = tk.StringVar()
    tk.Label(win3, text="Scottish Income Tax:", fg="white", bg="#1e1e1e", font=("Arial", 12)).pack()
    tk.Radiobutton(win3, text="Yes", variable=scottish_tax_var, value="Yes", fg="white", bg="#1e1e1e", selectcolor="#333").pack()
    tk.Radiobutton(win3, text="No", variable=scottish_tax_var, value="No", fg="white", bg="#1e1e1e", selectcolor="#333").pack()

    # Pension Contributions
    tk.Label(win3, text="Pension Contributions:", fg="white", bg="#1e1e1e", font=("Arial", 12)).pack()
    tax_code_entry = tk.Entry(win3, font=("Arial", 12))
    tax_code_entry.pack(pady=5)

    # Student Loan
    student_loan = tk.StringVar()
    tk.Label(win3, text="Student Loan:", fg="white", bg="#1e1e1e", font=("Arial", 12)).pack()
    tk.Radiobutton(win3, text="Plan 1", variable=student_loan, value="Plan 1", fg="white", bg="#1e1e1e", selectcolor="#333").pack()
    tk.Radiobutton(win3, text="Plan 2", variable=student_loan, value="Plan 2", fg="white", bg="#1e1e1e", selectcolor="#333").pack()
    tk.Radiobutton(win3, text="Plan 4", variable=student_loan, value="Plan 4", fg="white", bg="#1e1e1e", selectcolor="#333").pack()
    tk.Radiobutton(win3, text="No", variable=student_loan, value="No", fg="white", bg="#1e1e1e", selectcolor="#333").pack()

    # Postgrad Loan
    postgrad_loan = tk.StringVar()
    tk.Label(win3, text="Postgraduate Loan:", fg="white", bg="#1e1e1e", font=("Arial", 12)).pack()
    tk.Radiobutton(win3, text="Yes", variable=postgrad_loan, value="Yes", fg="white", bg="#1e1e1e", selectcolor="#333").pack()
    tk.Radiobutton(win3, text="No", variable=postgrad_loan, value="No", fg="white", bg="#1e1e1e", selectcolor="#333").pack()

    # --- Final Submit ---
    def calculate_pay():
        tax_code = tax_code_var.get()
        if tax_code == "I don't know":
            tax_code = "1257L"
        user_data["Tax Code"] = tax_code
        user_data["Scottish Tax"] = scottish_tax_var.get() == "Yes"
        user_data["Pension Contributions"] = f"{tax_code_entry.get()}% of gross income"
        user_data["Student Loan"] = student_loan.get()
        user_data["Postgrad Loan"] = postgrad_loan.get() == "Yes"
        # For now, just display the data
        summary = "\n".join(f"{k.title()}: {v}" for k, v in user_data.items())
        messagebox.showinfo("Summary", f"Your Data:\n\n{summary}")

    tk.Button(win3, text="Calculate take-home pay", command=calculate_pay,
              bg="#00a651", fg="white", font=("Arial", 12)).pack(pady=15)

    win3.mainloop()

# Step 0: First Window Setup
root = tk.Tk()
root.title("Salary Input")
root.geometry("400x400")
root.configure(bg="#1e1e1e")

# UI Elements
tk.Label(root, text="How much are you paid?", fg="white", bg="#1e1e1e", font=("Arial", 16, "bold")).pack(pady=10)
tk.Label(root, text="Gross amount, in pounds (£):", fg="white", bg="#1e1e1e", font=("Arial", 12)).pack()
amount_entry = tk.Entry(root, font=("Arial", 12))
amount_entry.pack(pady=5)

tk.Label(root, text="How often are you paid this amount?", fg="white", bg="#1e1e1e", font=("Arial", 12)).pack(pady=10)
freq_var = tk.StringVar()
frequencies = ["Yearly", "Monthly", "Every 4 weeks", "Weekly", "Daily", "Hourly"]
for freq in frequencies:
    tk.Radiobutton(root, text=freq, variable=freq_var, value=freq,
                   fg="white", bg="#1e1e1e", selectcolor="#333", font=("Arial", 11)).pack(anchor="w", padx=50)

tk.Button(root, text="Continue", command=submit, bg="#00a651", fg="white", font=("Arial", 12)).pack(pady=15)

root.mainloop()
