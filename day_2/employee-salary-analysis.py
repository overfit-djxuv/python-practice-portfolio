
"""
=========================================================
        DAY 2 - EMPLOYEE SALARY ANALYSIS
=========================================================

Description:
A Python project that analyses employee salary data.

Concepts practised:
- Functions
- Lists and dictionaries
- List comprehensions
- Lambda functions
- max(), min(), sorted()
- Filtering and sets
- Data analysis and reporting

Author: Your Name
=========================================================
"""

# =========================================================
# 1. EMPLOYEE DATA
# =========================================================

employees = [
    {"name": "Alex", "salary": 45000, "department": "IT"},
    {"name": "Sarah", "salary": 65000, "department": "HR"},
    {"name": "John", "salary": 55000, "department": "IT"},
    {"name": "Emma", "salary": 75000, "department": "Finance"},
    {"name": "David", "salary": 50000, "department": "HR"},
    {"name": "Lisa", "salary": 85000, "department": "Finance"}
]


# =========================================================
# 2. SALARY CALCULATIONS
# =========================================================

def calculate_average_salary(employees):
    """Calculate the average salary of all employees."""
    if not employees:
        return 0

    salaries = [employee['salary'] for employee in employees]
    return sum(salaries) / len(salaries)


def calculate_total_salary_expenditure(employees):
    """Calculate the total salary expenditure."""
    salaries = [employee['salary'] for employee in employees]
    return sum(salaries)


# =========================================================
# 3. HIGHEST AND LOWEST PAID EMPLOYEES
# =========================================================

def find_the_highest_paid_employee(employees):
    """Find the employee with the highest salary."""
    if not employees:
        return None

    return max(employees, key=lambda employee: employee['salary'])


def find_the_lowest_paid_employee(employees):
    """Find the employee with the lowest salary."""
    if not employees:
        return None

    return min(employees, key=lambda employee: employee['salary'])


# =========================================================
# 4. SORT EMPLOYEES BY SALARY
# =========================================================

def sort_employees_by_salary(employees):
    """Sort employees from lowest to highest salary."""
    return sorted(
        employees,
        key=lambda employee: employee['salary']
    )


# =========================================================
# 5. FILTER EMPLOYEES BY DEPARTMENT
# =========================================================

def filter_employees_by_department(employees, department):
    """Return employees belonging to a specific department."""
    return [
        employee for employee in employees
        if employee['department'].lower() == department.lower()
    ]


# =========================================================
# 6. EMPLOYEES EARNING ABOVE AVERAGE
# =========================================================

def find_employees_above_average(employees):
    """Find employees earning more than the average salary."""
    if not employees:
        return []

    average = calculate_average_salary(employees)

    return [
        employee for employee in employees
        if employee['salary'] > average
    ]


# =========================================================
# 7. DEPARTMENT-WISE REPORT
# =========================================================

def generate_department_report(employees):
    """Generate salary statistics for each department."""

    departments = {employee['department'] for employee in employees}

    print("\n" + "=" * 55)
    print("              DEPARTMENT-WISE REPORT")
    print("=" * 55)

    for department in sorted(departments):

        department_employees = filter_employees_by_department(
            employees, department
        )

        employee_count = len(department_employees)

        total_salary = calculate_total_salary_expenditure(
            department_employees
        )

        average_salary = calculate_average_salary(
            department_employees
        )

        print(f"\nDepartment : {department}")
        print("-" * 40)
        print(f"Employees  : {employee_count}")
        print(f"Total      : ${total_salary:,.2f}")
        print(f"Average    : ${average_salary:,.2f}")

    print("=" * 55)


# =========================================================
# 8. MAIN PROGRAM
# =========================================================

def main():

    print("\n" + "=" * 55)
    print("             EMPLOYEE SALARY ANALYSIS")
    print("=" * 55)

    if not employees:
        print("No employee data available.")
        return

    print(f"\nTotal employees : {len(employees)}")
    print(f"Average salary  : ${calculate_average_salary(employees):,.2f}")
    print(f"Total expenditure: ${calculate_total_salary_expenditure(employees):,.2f}")

    # Highest-paid employee
    print("\n[ HIGHEST-PAID EMPLOYEE ]")
    print(find_the_highest_paid_employee(employees))

    # Lowest-paid employee
    print("\n[ LOWEST-PAID EMPLOYEE ]")
    print(find_the_lowest_paid_employee(employees))

    # Sorted employees
    print("\n[ EMPLOYEES SORTED BY SALARY ]")

    for employee in sort_employees_by_salary(employees):
        print(
            f"{employee['name']:<10} "
            f"${employee['salary']:>10,} "
            f"| {employee['department']}"
        )

    # IT department
    print("\n[ IT DEPARTMENT EMPLOYEES ]")

    for employee in filter_employees_by_department(employees, "IT"):
        print(f"{employee['name']} - ${employee['salary']:,}")

    # Above-average employees
    print("\n[ EMPLOYEES EARNING ABOVE AVERAGE ]")

    for employee in find_employees_above_average(employees):
        print(f"{employee['name']} - ${employee['salary']:,}")

    # Department report
    generate_department_report(employees)

    print("\n" + "=" * 55)
    print("          END OF EMPLOYEE SALARY REPORT")
    print("=" * 55)


# =========================================================
# PROGRAM ENTRY POINT
# =========================================================

if __name__ == "__main__":
    main()
