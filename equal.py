inventory = {
    "laptops": 10,
    "phones": 20,
    "tablets": 15
}

it_department_inventory = inventory
sales_department_inventory = inventory

def update_inventory(department_inventory, item, quantity):
    department_inventory[item] -= quantity
    print(f"{item} changed -> Remaining: {department_inventory[item]}")


update_inventory(it_department_inventory, "laptops", 2)

update_inventory(sales_department_inventory, "phones", 3)

print("IT department inventory:", it_department_inventory)
print("Sales department inventory:", sales_department_inventory)
print("Original inventory:", inventory)