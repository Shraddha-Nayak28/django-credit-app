def check_eligibility(application):
    """
    Custom logic to determine loan eligibility.
    Modify this based on rules like income, credit score, etc.
    """
    if application.credit_score < 600:
        return False, "Credit score too low"
    if application.loan_amount > (application.customer.income * 10):
        return False, "Loan amount exceeds eligibility"
    if application.interest_rate > 15:
        return False, "Interest rate too high"

    return True, "Eligible"
def check_eligibility(customer_id, loan_amount, interest_rate, tenure):
    # dummy implementation for now
    return {
        "eligible": True,
        "approved_limit": 1000000,
        "message": "Customer is eligible for the requested loan"
    }

def check_eligibility(customer, loan_amount, interest_rate, tenure):
    # Example logic
    corrected_rate = interest_rate
    if customer.employment_status.lower() == 'unemployed':
        corrected_rate += 4  # Penalize for unemployment

    monthly_installment = calculate_emi(loan_amount, corrected_rate, tenure)

    eligible = corrected_rate <= 16 and loan_amount <= customer.approved_limit

    return {
        "customer_id": customer.customer_id,
        "approval": eligible,
        "interest_rate": interest_rate,
        "corrected_interest_rate": corrected_rate,
        "tenure": tenure,
        "monthly_installment": round(monthly_installment, 2),
        "approval_details": "Customer eligible" if eligible else "High interest due to risk"
    }

def calculate_emi(principal, rate, tenure_months):
    r = rate / (12 * 100)
    return principal * r * ((1 + r) ** tenure_months) / (((1 + r) ** tenure_months) - 1)
