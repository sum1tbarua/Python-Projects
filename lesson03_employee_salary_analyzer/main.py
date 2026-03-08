from data import employees
from utilities import *

if __name__ == "__main__":
    print("=== Employee Salary Analyzer ===")
    print()

    print("Total records:", count_records(employees))
    print()

    print("Unique departments:")
    print(get_unique_departments(employees))
    print()

    print("Employees per department:")
    print(count_per_department(employees))
    print()

    print("Average salary per department:")
    print(average_salary_per_department(employees))
    print()

    print("Highest salary:")
    print(highest_salary(employees))
    print()

    print("High earners (>90000):")
    print(high_earners(employees, 90000))
    