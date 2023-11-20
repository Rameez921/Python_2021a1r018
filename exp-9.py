class Employee:
    def __init__(self, name, age, salary):
        self.name, self.age, self.salary = name, age, salary

    def display_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}")


class Manager(Employee):
    def __init__(self, name, age, salary, department):
        super().__init__(name, age, salary)
        self.department = department

    def display_details(self):
        super().display_details()
        print(f"Department: {self.department}")


class EmployeeManagementSystem:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def display_employees(self):
        [emp.display_details() for emp in self.employees] or print("No employees found.")


def main():
    emp_system = EmployeeManagementSystem()

    while True:
        print("\nEmployee Management System\n1. Add Employee\n2. Display Employees\n3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            name, age, salary = input("Enter name, age, salary: ").split()
            department = input("Enter department: ")
            emp_type = input("Is the employee a manager? (yes/no): ").lower()
            employee = Manager(name, int(age), float(salary), department) if emp_type == 'yes' else Employee(name, int(age), float(salary))
            emp_system.add_employee(employee)
            print("Employee added!")

        elif choice == '2':
            emp_system.display_employees()

        elif choice == '3':
            print("Exiting Employee Management System.")
            break

        else:
            print("Invalid choice. Please enter a valid option (1-3).")


if __name__ == "__main__":
    main()
