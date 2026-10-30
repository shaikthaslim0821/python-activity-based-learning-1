def calculate_deduction(gross):
    if gross <= 20000:
        deduction = gross * 0.05

    elif gross <= 40000:
        deduction = (20000 * 0.05) + ((gross - 20000) * 0.10)

    else:
        deduction = (20000 * 0.05) + (20000 * 0.10) + ((gross - 40000) * 0.15)

    return deduction

emp_id = input("Enter Employee ID: ")
name = input("Enter Employee Name: ")

basic = float(input("Enter Basic Salary: "))
allowances = float(input("Enter Allowances: "))
hours = float(input("Enter Overtime Hours: "))
rate = float(input("Enter Overtime Rate: "))
incentives = float(input("Enter Incentives: "))
overtime_pay = hours * rate


gross = basic + allowances + overtime_pay + incentives
deduction = calculate_deduction(gross)


net_salary = gross - deduction


print("\n======================================")
print("       EMPLOYEE SALARY STATEMENT")
print("======================================")
print("Employee ID       :", emp_id)
print("Employee Name     :", name)
print("--------------------------------------")
print("Basic Salary      : Rs.", basic)
print("Allowances        : Rs.", allowances)
print("Overtime Pay      : Rs.", overtime_pay)
print("Incentives        : Rs.", incentives)
print("--------------------------------------")
print("Gross Salary      : Rs.", gross)
print("Total Deductions  : Rs.", deduction)
print("--------------------------------------")
print("NET SALARY        : Rs.", net_salary)
print("======================================")
print("       PAYROLL COMPLETED")

