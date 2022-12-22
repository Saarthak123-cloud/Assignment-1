grossincome=int(input("Enter your gross income"))
dependents=int(input("Enter number of dependents"))
standard_deduction=10000
additional_deduction=dependents*3000
taxable_income=(grossincome-standard_deduction-int(additional_deduction))
print("taxable income:",taxable_income)
tax_rate=0.20
tax=taxable_income*tax_rate
print("Tax:",tax)


