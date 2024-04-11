"""
Report Generation Module

This module provides a function for generating reports based on employee data.
"""

def generate_reports():
    """
    Generate Reports Function

    This function generates various reports based on employee data, such as:
    - List of departments
    - List of all employees with ID, full name, and department
    - List of all departments with the average age and salary of employees
    - List of employees in each department with ID, full name, date of birth, salary,
      and total salary for department's employees
    """
def generate_reports():
    # Dummy data for demonstration
    departments = {
        'IT': [
            {'id': 1, 'full_name': 'Jefin joshy', 'date_of_birth': '1990-05-15', 'salary': 61000},
            {'id': 2, 'full_name': 'Anmol sighn', 'date_of_birth': '1975-10-20', 'salary': 80000},
            {'id': 3, 'full_name': 'Adwaith ajith', 'date_of_birth': '1985-13-05', 'salary': 47000}
        ],
        'HR': [
            {'id': 4, 'full_name': 'Daniel James', 'date_of_birth': '1968-22-10', 'salary': 77000},
            {'id': 5, 'full_name': 'Mikhil saji', 'date_of_birth': '1970-11-20', 'salary': 71000}
        ]
    }
    print("List of Departments:")
    for department in departments.keys():
        print("- " + department)
    print()

    print("List of All Employees:")
    for department, employees in departments.items():
        for employee in employees:
            print(f"- ID: {employee['id']}, Name: {employee['full_name']}, Department: {department}")
    print()

    print("List of Departments with Average Age and Salary:")
    for department, employees in departments.items():
        total_salary = sum(employee['salary'] for employee in employees)
        average_salary = total_salary / len(employees)
        print(f"- Department: {department}, Average Salary: ${average_salary:.2f}")
    print()

    print("List of Employees in Each Department:")
    for department, employees in departments.items():
        print(f"- Department: {department}")
        for employee in employees:
            print(f"  - ID: {employee['id']}, Name: {employee['full_name']}, "
                  f"DOB: {employee['date_of_birth']}, Salary: ${employee['salary']}")
        total_salary = sum(employee['salary'] for employee in employees)
        print(f"  Total Salary for {department}: ${total_salary}")
    print()

generate_reports()
