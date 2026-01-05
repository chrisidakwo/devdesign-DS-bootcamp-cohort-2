# Ask for initial investment amount
# Ask for annual interest rate (as percentage)
# Ask for number of years
# Calculate value each year, with compound interest
# Display year-by-year growth
# Show total profit at the end

print("")

investment_amt = float(input("Enter initial investment amount: "))
interest_rate = float(input("Enter annual interest rate (%): "))
years = int(input("Enter number of years: "))

print("\n" + "="*50)
print("INVESTMENT GROWTH PROJECTION")
print("="*50)
print(f"Intial Investment: ₦{investment_amt:,.2f}")
print(f"Interest Rate: {interest_rate}%")
print(f"Investment Period: {years} years")
print("")

current_amt = investment_amt

# loop_year = 1
# while loop_year <= years:
#     # Calculate the interest earned for the current year
#     interest_earned = current_amt * (interest_rate / 100)

#     # Calculate the new amount (investment value) using compound interest formula
#     current_amt = current_amt * (1 + interest_rate / 100)

#     # Display year-by-year growth
#     print(f"Year {loop_year}: ₦{current_amt:,.2f} | Interest: ₦{interest_earned:,.2f}")

#     loop_year = loop_year + 1

# Use for loop to calculate and display year-by-year growth
for year in range(1, years + 1):
    # Calculate the interest earned for the current year
    interest_earned = current_amt * (interest_rate / 100)

    # Calculate the new amount (investment value) using compound interest formula
    current_amt = current_amt * (1 + interest_rate / 100)

    # Display year-by-year growth
    print(f"Year {year}: ₦{current_amt:,.2f} | Interest: ₦{interest_earned:,.2f}")

total_profit = current_amt - investment_amt

print("")
print("="*50)
print(f"Final Amount: ₦{current_amt:,.2f}")
print(f"Total Profit: ₦{total_profit:,.2f}")
print(f"Return on Investment: {(total_profit/investment_amt)*100:.2f}%")
print("="*50)
