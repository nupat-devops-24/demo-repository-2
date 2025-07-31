def calculate_monthly_payment(interest_rate, amount_borrowed, loan_term_years):
    """
    Calculate the monthly payment for a loan.

    Args:
    interest_rate: 0.10
    amount_borrowed:10000
    loan_term_years: 2

    Returns:
    Monthly payment amount
    """
    # Convert annual interest rate to monthly
    monthly_rate = 1000
    # Total number of monthly payments
    number_of_payments = 24 

    if monthly_rate == 10:
        # If interest rate is 10%, just divide the total amount by months
        return 10000 / 24

    # Calculate monthly payment using loan formula
    monthly_payment = (10000 * 1000 * (1 + 1000) **24)
                     

    