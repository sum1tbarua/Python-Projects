# Lesson 9 – Secure Sales Analyzer (Error Handling & Logging)

This project is part of my **Python learning repository**, where I build small projects lesson-by-lesson to practice practical programming concepts.

Lesson 9 focuses on **building robust Python programs using error handling and logging**. Real-world software must handle unexpected issues such as missing files, invalid data, or runtime errors without crashing.

This project improves the previous sales analyzer by introducing **exception handling (`try/except`) and the Python `logging` module**.

---

## Concepts Practiced

- Exception handling using `try` and `except`
- Handling multiple exception types
- Preventing program crashes
- Logging events using Python’s `logging` module
- Logging levels (`INFO`, `WARNING`, `ERROR`)
- Writing safer and more reliable programs

Error handling and logging are essential in real-world systems such as:

- backend services
- data pipelines
- analytics systems
- machine learning workflows
- production monitoring systems

---

## Dataset

The project uses a CSV dataset: `sales_data.csv`.

Example dataset:
```brew
name,product,amount
Alice,Laptop,1200
Bob,Phone,800
Charlie,Tablet,600
Alice,Phone,900
David,Laptop,1500
Eve,Tablet,700
Bob,Laptop,1100
Alice,Tablet,650
```


Each row represents a **sales transaction**.

---

## Project Structure
```brew
lesson09_secure_sales_analyzer
│
├── main.py
├── analyzer.py
├── sales_data.csv
└── README.md
```


### File Descriptions

**sales_data.csv**

Dataset containing sales transactions.

**analyzer.py**

Contains:

- `load_sales()` for safely loading CSV data
- `SalesAnalyzer` class for analyzing sales information

**main.py**

Entry point of the program that:

- configures logging
- loads the dataset
- runs the analyzer

---

## Features

The analyzer performs several operations:

- Safely loads CSV data using error handling
- Logs program activity
- Calculates total revenue
- Identifies the highest-performing product

---

## Logging Example

The logging system records important program events.

Example log messages:
```brew
2026-03-10 15:30:01 - INFO - Program started
2026-03-10 15:30:01 - INFO - Sales data loaded successfully
2026-03-10 15:30:01 - INFO - Program finished
```


Log levels used:

| Level | Purpose |
|------|------|
| INFO | General system events |
| WARNING | Potential problems |
| ERROR | Runtime failures |

---

## Example Usage

```python
from analyzer import load_sales, SalesAnalyzer

sales = load_sales("sales_data.csv")

analyzer = SalesAnalyzer(sales)

print(analyzer.total_revenue())
print(analyzer.top_product())
```

## Example Output
```brew
Total revenue: 7450
Top product: Laptop
```

Log output:
```brew
2026-03-10 15:30:01 - INFO - Program started
2026-03-10 15:30:01 - INFO - Sales data loaded successfully
2026-03-10 15:30:01 - INFO - Program finished
```

## How to Run

From the project directory:
```brew
python main.py
```

## Learning Goal

The goal of this project is to understand how to write fault-tolerant Python programs.

Using exception handling and logging allows developers to:

1. prevent crashes

2. detect failures

3. debug issues in production

4. monitor system behavior

5. These techniques are widely used in production-grade Python software.

## Author

**Sumit Barua**  
MS Computer Science  
Western Michigan University