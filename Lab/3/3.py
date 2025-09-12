def employee(name, salary = 69000):
    tax = salary * 0.02
    salTax = salary - tax
    print(f"Employee:",name)
    print(f"Salary After Tax:", salTax)

employee("Khalid",183000)
print("\n")
employee("Anwer")    