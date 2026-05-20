from datetime import datetime
employee = {
    "employee_id": "EMP101",
    "name": "John Doe",
    "department": "IT",
    "designation": "Software Engineer"
}

salary = {
    "basic": 50000,
    "hra": 20000,
    "allowances": 10000,
    "deductions": 5000
}

gross_salary = (
    salary["basic"]
    + salary["hra"]
    + salary["allowances"]
)

net_salary = gross_salary - salary["deductions"]

filename = f"salary_slip_{employee['employee_id']}.txt"

with open(filename, "w") as file:
    file.write("=========== EMPLOYEE SALARY SLIP ===========\n")
    file.write(f"Generated On : {datetime.now()}\n\n")

    file.write("Employee Details\n")
    file.write("--------------------------------------------\n")
    file.write(f"Employee ID : {employee['employee_id']}\n")
    file.write(f"Name        : {employee['name']}\n")
    file.write(f"Department  : {employee['department']}\n")
    file.write(f"Designation : {employee['designation']}\n\n")

    file.write("Salary Breakdown\n")
    file.write("--------------------------------------------\n")
    file.write(f"Basic Salary : {salary['basic']}\n")
    file.write(f"HRA          : {salary['hra']}\n")
    file.write(f"Allowances   : {salary['allowances']}\n")
    file.write(f"Deductions   : {salary['deductions']}\n\n")

    file.write(f"Gross Salary : {gross_salary}\n")
    file.write(f"Net Salary   : {net_salary}\n")
    file.write("============================================\n")

print(f"Salary slip generated successfully: {filename}")