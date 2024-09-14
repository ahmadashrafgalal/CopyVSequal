def add_employee(department, employee_name):
    department.append(employee_name)

def transfer_employee(from_department, to_department, employee_name):
    if employee_name in from_department:
        from_department.remove(employee_name)
        to_department.append(employee_name)
    else:
        print(f"{employee_name} not found in {from_department}")

tech_department = ["Ahmed", "Sarah", "Khaled"]
hr_department = tech_department 
marketing_department = ["Mona", "Ali"]

add_employee(hr_department, "Nour")

transfer_employee(tech_department, marketing_department, "Ahmed")

print("Tech department employees:", tech_department)
print("HR department employees:", hr_department)
print("Marketing department employees:", marketing_department)

# copy() method
tech_department = ["Ahmed", "Sarah", "Khaled"]
hr_department = tech_department.copy()
marketing_department = ["Mona", "Ali"]

add_employee(hr_department, "Nour")

transfer_employee(tech_department, marketing_department, "Ahmed")

print("Tech department employees:", tech_department)
print("HR department employees:", hr_department)
print("Marketing department employees:", marketing_department)