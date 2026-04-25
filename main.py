class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name


class Office:
    def __init__(self):
        self.name = 'office'
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def del_animal(self, employee_name):
        for employee in self.employees:
            if employee.name == employee_name:
                self.employees.remove(employee)
                return
        print(f"Людину '{employee_name}' не знайдено")

    def show_employees(self):
        for employee in self.employees:
            print(employee)


office = Office()
office.add_employee(Employee('Lauma', 20))
office.add_employee(Employee('Linnea', 20))
office.show_employees()
#zoo.del_animal("Linnea")
#zoo.show_animals()

