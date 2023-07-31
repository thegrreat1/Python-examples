
class Employees:
    def __init__(self):
        self.employees_name = ["Laura", "Jonathan"]
        self.employees_lastname = ["Weber", "Maurer"]


for employee in Employees().employees_name:
    employee_name = employee
    employee_lastname = Employees().employees_lastname[Employees().employees_name.index(employee)]

    print("Firstname: {}\n"
          "Lastname: {}\n".format(employee_name, employee_lastname))
