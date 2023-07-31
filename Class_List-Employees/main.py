employees_name = ["Laura", "Jonathan"]
employees_lastname = ["Weber", "Maurer"]


class Employee:
    def __init__(self, firstname, lastname):
        print("Firstname: {}  Lastname: {}\n".format(firstname, lastname))


for employees in employees_name:
    Employee(employees, employees_lastname[employees_name.index(employees)])
