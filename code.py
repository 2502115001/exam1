


with open("salary_slip_details.txt","w") as file:
    file.write('----------------------Employee Details-----------------')
    file.write('Employee Name : Hit Borsaniya \n')
    file.write('Employe ID : 2502115001\n')
    file.write('Department : Production\n')


    file.write('----------------------Employee Salary-----------------')
    file.write('Salary : 25000 \n')
    file.write('PFA : 3000\n')
    file.write('Graduety : 500\n')

print(f"Salary slip generated successfully")