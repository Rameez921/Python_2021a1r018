# Function to add an employee to the database
def add_employee(database):
    name = input("Enter employee name: ")
    age = int(input("Enter employee age: "))
    position = input("Enter employee position: ")

    employee = (name, age, position)
    database.append(employee)
    print("Employee added successfully!")

# Function to display all employees in the database
def display_employees(database):
    if not database:
        print("No employees in the database.")
    else:
        print("Employee Database:")
        print("Name\tAge\tPosition")
        for employee in database:
            print(f"{employee[0]}\t{employee[1]}\t{employee[2]}")

# Main function to manage the employee database
def main():
    employee_database = []

    while True:
        print("\nEmployee Database Management")
        print("1. Add Employee")
        print("2. Display Employees")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            add_employee(employee_database)
        elif choice == "2":
            display_employees(employee_database)
        elif choice == "3":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
