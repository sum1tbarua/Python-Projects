
# Function 1 — Count records
def count_records(data):
    return len(data)

# Function 2 — Get unique departments
def get_unique_departments(data):
    unique_departments = set()

    for name, department, salary in data:
        unique_departments.add(department)
    
    return unique_departments

# Function 3 — Count employees per department
def count_per_department(data):
    count_department = dict()
    
    for name, department, salary in data:
        count_department[department] = count_department.get(department, 0) + 1
    
    return count_department


# Function 4 — Average salary per department
def average_salary_per_department(data):
    count_salary = dict()
    count_department = count_per_department(data)
    average_salary = dict()
    
    for name, department, salary in data:
        count_salary[department] = count_salary.get(department, 0) + salary
    
    for salary in count_salary:
        average = count_salary[salary] / count_department[salary]
        average_salary[salary] = int(average)
    
    return average_salary    

# Function 5 — Highest salary record
def highest_salary(data):
    max_salary = 0
    max_name = None
    max_department = None

    for name, department, salary in data:
        if salary > max_salary:
            max_salary = salary
            max_name = name
            max_department = department
    
    return f'{max_name, max_department, max_salary}'

# Function 6 — Employees above threshold
def high_earners(data, threshold):
    high_earner_list = list()
    
    for name, department, salary in data:
        if salary >= threshold:
            high_earner_list.append((name, department, salary))
    
    return high_earner_list
    