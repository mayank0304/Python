# Tax calculator program

print("Mayank - 2203855")
salary=int(input("Please enter your salary:"))
tax = float(input("Please enter tax in percentage:"))
totalTax = salary * tax /100
remainingSalary = salary - totalTax
print("Tax you have to pay on your salary:", round(totalTax ,2) )
print("Your remaining salary after tax:", round(remainingSalary,2) )