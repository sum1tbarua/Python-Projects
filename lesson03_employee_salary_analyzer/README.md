# Lesson 3 – Employee Salary Analyzer

This project is part of my **Python learning repository**, where I build small projects lesson-by-lesson to practice real programming concepts.

This lesson focuses on **Python functions and modular code organization**.

The program analyzes a small dataset of employee salary records and generates summary statistics.

---

# Concepts Practiced

- Python functions
- Modular programming
- Separating logic into reusable utilities
- Working with lists, tuples, dictionaries, and sets
- Basic data aggregation

---

# Dataset Format

The dataset is stored in `data.py`.

Each record follows this structure:

(name, department, salary)

Example:
```brew
("Alice", "Engineering", 95000)
```


---

# Project Structure
```brew
lesson03_employee_salary_analyzer
│
├── main.py
├── utilities.py
├── data.py
└── README.md
```


### File Descriptions

**data.py**

Contains the dataset of employee records.

**utilities.py**

Contains reusable functions used to analyze the dataset:

- count_records
- get_unique_departments
- count_per_department
- average_salary_per_department
- highest_salary
- high_earners

**main.py**

Entry point of the program.  
Calls the utility functions and prints results.

---

# Features

The analyzer performs the following operations:

• Counts total employee records  
• Identifies unique departments  
• Counts employees per department  
• Computes average salary per department  
• Finds the highest salary record  
• Identifies employees earning above a salary threshold  

---

# Example Output
```brew
=== Employee Salary Analyzer ===

Total records: 7

Unique departments:
{'Engineering', 'HR', 'Marketing'}

Employees per department:
{'Engineering': 3, 'HR': 2, 'Marketing': 2}

Average salary per department:
{'Engineering': 93666, 'HR': 66500, 'Marketing': 73500}

Highest salary:
('David', 'Engineering', 99000)

High earners (>90000):
[('Alice', 'Engineering', 95000), ('David', 'Engineering', 99000)]
```


---

# How to Run

From the project directory:
```brew
python main.py
```


---

# Learning Goal

The purpose of this project is to practice **writing reusable functions and organizing Python programs into multiple modules**, which is an essential skill for real-world software development.

Future lessons will expand this repository with projects involving:

- file processing
- CSV data analysis
- automation scripts
- algorithmic problem solving