# Lesson 6 – Sales Ranking Analyzer (Sorting & Lambda Functions)

This project is part of my **Python learning repository**, where I build small projects lesson-by-lesson to practice practical programming concepts.

Lesson 6 focuses on **sorting data and using lambda functions**, which are widely used in Python for ranking, ordering, and selecting top results.

The program analyzes a small dataset of sales transactions and generates rankings such as top sales, top customers, and best-performing products.

---

## Concepts Practiced

- Sorting with `sorted()`
- Custom sorting using `key` functions
- Lambda functions
- Ranking records by value
- Aggregating data with dictionaries
- Selecting top-N results

Sorting and ranking patterns are used frequently in:

- analytics systems
- recommendation engines
- leaderboard systems
- machine learning result ranking
- backend data processing

---

## Dataset Format

The dataset is stored in `sales_data.py`.

Each record follows the structure:

```
(customer, product, amount)
```

Example:

```
("Alice", "Laptop", 1200)
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

---

## Project Structure

```
lesson06_sales_ranking_analyzer
│
├── main.py
├── utilities.py
├── sales_data.py
└── README.md
```

### File Descriptions

**sales_data.py**

Contains the dataset of sales transactions.

**utilities.py**

Contains reusable functions used to analyze and rank sales data:

- `top_sales`
- `sort_by_customer`
- `sort_by_product`
- `total_sales_per_customer`
- `top_customer`
- `top_product`

These functions demonstrate sorting, lambda functions, and data aggregation.

**main.py**

Entry point of the program that loads the dataset and prints analysis results.

---

## Features

The analyzer performs the following operations:

- Finds the top N highest-value sales
- Sorts sales records by customer
- Sorts sales records by product
- Computes total revenue per customer
- Identifies the top earning customer
- Determines the product generating the most revenue

---

## Example Output

```
=== Sales Ranking Analyzer ===

Top 3 sales:
('David', 'Laptop', 1500)
('Alice', 'Laptop', 1200)
('Bob', 'Laptop', 1100)

Sorted by customer:
('Alice', 'Laptop', 1200)
('Alice', 'Phone', 900)
('Alice', 'Tablet', 650)
...

Total sales per customer:
{'Alice': 2750, 'Bob': 1900, 'Charlie': 600, 'David': 1500, 'Eve': 700}

Top earning customer:
Alice

Top product by revenue:
Laptop
```

---

## How to Run

From the project directory:

```
python main.py
```

---

## Learning Goal

The purpose of this project is to practice **sorting and ranking data in Python**.

These skills are essential for:

- ranking machine learning predictions
- selecting top results from datasets
- building leaderboards
- performing analytics on structured data

---

## Repository Progress

This project is part of a structured Python learning path:

| Lesson | Project | Concepts |
|------|------|------|
| 1 | Log Analyzer | loops, file reading |
| 2 | Student Score Analyzer | lists, dictionaries, sets |
| 3 | Employee Salary Analyzer | functions, modular code |
| 4 | Sales Data Analyzer | CSV processing |
| 5 | Movie Ratings Analyzer | Python comprehensions |
| 6 | Sales Ranking Analyzer | sorting, lambda functions |

---

## Author

**Sumit Barua**  
MS Computer Science  
Western Michigan University