# Lesson 8 – Sales Analyzer (Object-Oriented Programming)

This project is part of my **Python learning repository**, where I build small projects lesson-by-lesson to practice real-world programming concepts.

Lesson 8 introduces **Object-Oriented Programming (OOP)** in Python. Instead of organizing logic as standalone functions, this project groups related data and behavior inside a class.

The program analyzes a dataset of sales transactions and provides methods to compute revenue statistics and rankings.

---

## Concepts Practiced

- Python classes
- Object initialization using `__init__`
- Instance attributes
- Methods inside classes
- Encapsulation (data + behavior)
- Using objects to organize code

Object-oriented design is widely used in real-world Python systems such as:

- data processing frameworks
- machine learning libraries
- backend systems
- analytics tools

---

## Dataset

The dataset is stored in `sales_data.py`.

Each record follows the format:
```brew
(customer, product, amount)
```


Example dataset:

```python
sales = [
    ("Alice", "Laptop", 1200),
    ("Bob", "Phone", 800),
    ("Charlie", "Tablet", 600),
    ("Alice", "Phone", 900),
    ("David", "Laptop", 1500),
    ("Eve", "Tablet", 700),
    ("Bob", "Laptop", 1100),
    ("Alice", "Tablet", 650)
]
```

## Project Structure
```brew
lesson08_sales_analyzer_class
│
├── main.py
├── utilities.py
├── sales_data.py
└── README.md
```

## File Descriptions

sales_data.py

Contains the dataset of sales transactions.

utilities.py

Defines the SalesAnalyzer class and its analysis methods.

Class methods include:

count_records

total_revenue

revenue_per_product

top_customer

top_sales

main.py

Creates a SalesAnalyzer object and calls its methods to analyze the dataset.

## Features
The analyzer performs several operations:

1. Counts total sales records

2. Calculates total revenue

3. Computes revenue per product

4. Identifies the top-spending customer

5. Returns the highest-value sales transactions

## Expected output
```brew
=== Sales Analyzer ===

Total records: 8

Total revenue:
7450

Revenue per product:
{'Laptop': 3800, 'Phone': 1700, 'Tablet': 1950}

Top customer:
Alice

Top 3 sales:
[('David', 'Laptop', 1500),
 ('Alice', 'Laptop', 1200),
 ('Bob', 'Laptop', 1100)]
```

## Learning Goal

The goal of this project is to understand how Object-Oriented Programming improves code organization.

Compared to procedural code, OOP allows developers to:

1. group related data and logic

2. reuse components easily

3. extend functionality cleanly

4. build scalable software systems

Most production Python libraries rely heavily on OOP.


## Author

**Sumit Barua**  
MS Computer Science  
Western Michigan University