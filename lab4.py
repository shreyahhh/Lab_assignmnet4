class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"{self.emp_id}\t{self.name}\t{self.age}\t{self.salary}"


class EmployeeTable:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def sort_by_age(self):
        self.employees.sort(key=lambda emp: emp.age)

    def sort_by_name(self):
        self.employees.sort(key=lambda emp: emp.name)

    def sort_by_salary(self):
        self.employees.sort(key=lambda emp: emp.salary)

    def display_table(self):
        print("Employee ID\tName\tAge\tSalary")
        print("----------------------------------")
        for employee in self.employees:
            print(employee)

def main():
    employee_table = EmployeeTable()

    employee_table.add_employee(Employee("161E90", "Raman", 41, 56000))
    employee_table.add_employee(Employee("161F91", "Himadri", 38, 67500))
    employee_table.add_employee(Employee("161F99", "Jaya", 51, 82100))
    employee_table.add_employee(Employee("171E20", "Tejas", 30, 55000))
    employee_table.add_employee(Employee("171G30", "Ajay", 45, 44000))

    print("Choose sorting parameter:")
    print("1. Age\n2. Name\n3. Salary")
    choice = int(input())

    if choice == 1:
        employee_table.sort_by_age()
    elif choice == 2:
        employee_table.sort_by_name()
    elif choice == 3:
        employee_table.sort_by_salary()
    else:
        print("Invalid choice")

    employee_table.display_table()

if __name__ == "__main__":
    main()
