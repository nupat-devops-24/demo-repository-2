
"""interest_rate: The annual interest rate (as a decimal, e.g., 0.05 for 5%).

amount_borrowed: The total amount of money borrowed.

loan_term_years: The number of years for the loan repayment


The function should calculate the monthly payment amount and return it as a floating-point number.

"""""


def calculate_monthly_payment(interest_rate, amount_borrowed, loan_term_years):


    interest_rate= float(interest_rate/12) # converting to a monthly interest rate

    principal= amount_borrowed #correcting the formular, alternatively, I could just edit the principal

    monthly_payment = (principal * interest_rate) / (1 - (1 + interest_rate) ** (-loan_term_years * 12))

   # monthly_payment = 0 

    return float(monthly_payment)

interest_rate = 0.05  # 5% annual interest

amount_borrowed = 10000

loan_term_years = 2

monthly_payment = calculate_monthly_payment(interest_rate, amount_borrowed, loan_term_years)

print(f"Monthly payment: ${monthly_payment:.2f}")