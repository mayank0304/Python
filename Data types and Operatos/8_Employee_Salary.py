# An employee’s total weekly pay equals the hourly wage multiplied by the total number of 
# regular hours plus any overtime pay. Overtime pay equals the total overtime hours 
# multiplied by 1.5 times the hourly wage. Write a program that takes as inputs the hourly 
# wage, total regular hours, and total overtime hours and displays an employee’s total 
# weekly pay.


hourly_wage = float(input("Enter Hour wage: "))
regular_hours = int(input("Enter number of regular hours in a week: "))
overtime_hours = int(input("Enter overtime hours in a week : "))
overtime_salary = overtime_hours * (1.5*hourly_wage)
regular_salary = hourly_wage * regular_hours
employee_salary = regular_salary + overtime_salary
print(f"Employee's week salary: {employee_salary}")
