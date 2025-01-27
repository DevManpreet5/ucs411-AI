def calculate_compound_interest(principal, rate, time):
    amount = principal * (1 + rate / 100) ** time
    compound_interest = amount - principal
    return compound_interest