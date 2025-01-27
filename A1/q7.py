
from comp_int import calculate_compound_interest

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the interest rate: "))
time = float(input("Enter the time in years: "))

interest = calculate_compound_interest(principal, rate, time)
print(f"The compound interest is: {interest}")
