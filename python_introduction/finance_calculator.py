monthly_income = int(input("Enter your monthly income:"))
monthly_expenses = int(input("Enter your total monthly expenses: "))
monthly_savings = monthly_income - monthly_expenses
rate = 0.05
Projected_Savings = monthly_savings *12 + (monthly_savings *12 * rate)
print(f"Projected savings after one year, with interest, is: ${Projected_Savings}")