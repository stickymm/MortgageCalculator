import tkinter as tk
from tkinter import ttk

class MortgageCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Mortgage Calculator")

        self.cash_amount = tk.DoubleVar()
        self.home_price = tk.DoubleVar()
        self.interest_rate = tk.DoubleVar()
        self.loan_term_years = tk.IntVar()
        self.property_taxes = tk.DoubleVar()
        self.homeowners_insurance = tk.DoubleVar()

        self.create_widgets()

    def create_widgets(self):
        top_label = tk.Label(self.root, text="Amount per Month: $0.00", font=("Helvetica", 16))
        top_label.pack(pady=10)

        downpayment_frame = ttk.LabelFrame(self.root, text="Down Payment")
        downpayment_frame.pack(fill="both", expand="yes", padx=10, pady=5)

        cash_amount_label = ttk.Label(downpayment_frame, text="Cash Amount:")
        cash_amount_label.grid(row=0, column=0, sticky="w")

        self.cash_amount_entry = ttk.Entry(downpayment_frame, textvariable=self.cash_amount)
        self.cash_amount_entry.grid(row=0, column=1, padx=5)

        home_equity_label = ttk.Label(downpayment_frame, text="Home Equity:")
        home_equity_label.grid(row=1, column=0, sticky="w")

        self.home_equity_entry = ttk.Entry(downpayment_frame)
        self.home_equity_entry.grid(row=1, column=1, padx=5)

        home_price_frame = ttk.LabelFrame(self.root, text="Home Price")
        home_price_frame.pack(fill="both", expand="yes", padx=10, pady=5)

        self.home_price_entry = ttk.Entry(home_price_frame, textvariable=self.home_price)
        self.home_price_entry.pack(pady=5)

        interest_rate_frame = ttk.LabelFrame(self.root, text="Interest Rate and Loan Length")
        interest_rate_frame.pack(fill="both", expand="yes", padx=10, pady=5)

        self.interest_rate_entry = ttk.Entry(interest_rate_frame, textvariable=self.interest_rate)
        self.interest_rate_entry.pack(pady=5)

        loan_term_label = ttk.Label(interest_rate_frame, text="Loan Term (years):")
        loan_term_label.pack(pady=5)

        self.loan_term_entry = ttk.Entry(interest_rate_frame, textvariable=self.loan_term_years)
        self.loan_term_entry.pack(pady=5)

        taxes_insurance_frame = ttk.LabelFrame(self.root, text="Property Taxes and Homeowners Insurance")
        taxes_insurance_frame.pack(fill="both", expand="yes", padx=10, pady=5)

        property_taxes_label = ttk.Label(taxes_insurance_frame, text="Property Taxes:")
        property_taxes_label.grid(row=0, column=0, sticky="w")

        self.property_taxes_entry = ttk.Entry(taxes_insurance_frame, textvariable=self.property_taxes)
        self.property_taxes_entry.grid(row=0, column=1, padx=5)

        homeowners_insurance_label = ttk.Label(taxes_insurance_frame, text="Homeowners Insurance:")
        homeowners_insurance_label.grid(row=1, column=0, sticky="w")

        self.homeowners_insurance_entry = ttk.Entry(taxes_insurance_frame, textvariable=self.homeowners_insurance)
        self.homeowners_insurance_entry.grid(row=1, column=1, padx=5)

        calculate_button = ttk.Button(self.root, text="Calculate", command=self.calculate)
        calculate_button.pack(pady=10)

    def calculate(self):
        loan_amount = self.calculate_loan_amount()
        monthly_payment = self.calculate_monthly_payment(loan_amount)

        top_label = f"Amount per Month: ${monthly_payment:.2f}"
        self.root.children["!label"].config(text=top_label)

    def calculate_loan_amount(self):
        cash_amount = self.cash_amount.get()
        home_equity = self.home_equity_entry.get()
        total_downpayment = cash_amount + float(home_equity or 0)

        home_price = self.home_price.get()
        return home_price - total_downpayment

    def calculate_monthly_payment(self, loan_amount):
        interest_rate = self.interest_rate.get()
        loan_term_years = self.loan_term_years.get()

        monthly_interest_rate = (interest_rate / 12) / 100
        total_payments = loan_term_years * 12

        monthly_payment = loan_amount * (monthly_interest_rate * (1 + monthly_interest_rate) ** total_payments) / \
                          ((1 + monthly_interest_rate) ** total_payments - 1)

        property_taxes = self.property_taxes.get()
        homeowners_insurance = self.homeowners_insurance.get()

        monthly_payment += (property_taxes + homeowners_insurance) 

        return monthly_payment


if __name__ == "__main__":
    root = tk.Tk()
    app = MortgageCalculatorApp(root)
    root.mainloop()
