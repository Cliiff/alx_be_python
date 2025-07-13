income = float(input("Enter your income: "))
expenses = float(input("Enter your total monthly expenses: "))

savings = income - expenses
print("Your monthly savings are:", savings)

months = 12
rate = 0.05  # Annual interest rate
projected_savings = savings * months + (savings * rate * months)

print("Your monthly saving are $",savings)
print("Projected savings after one year, with interest, is:", projected_savings)