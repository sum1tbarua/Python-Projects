# Lesson 7 – Log Stream Analyzer (Generators & Iterators)

This project is part of my **Python learning repository**, where I build small projects lesson-by-lesson to practice practical programming concepts.

Lesson 7 focuses on **generators and iterators**, which enable efficient processing of data streams without loading everything into memory.

The program simulates a **streaming log analyzer** that reads log files line-by-line and processes them using generator pipelines.

---

## Concepts Practiced

- Python generators using `yield`
- Iterators and lazy evaluation
- Streaming file processing
- Generator pipelines
- Filtering and processing log data

Generators are widely used in:

- log monitoring systems
- data pipelines
- machine learning dataset loaders
- streaming analytics systems
- ETL pipelines

---

## Dataset

The project uses a simple log file: `logs.txt`.

Example log file:
```brew
INFO User login
ERROR Database connection failed
INFO File uploaded
WARNING Disk usage high
INFO User logout
ERROR Timeout while processing request
INFO Backup completed
WARNING CPU temperature high
```


Each line follows the format:
```brew
LOG_LEVEL message
```


---

## Project Structure
```brew
lesson07_log_stream_analyzer
│
├── main.py
├── utilities.py
├── logs.txt
└── README.md
```


### File Descriptions

**logs.txt**

Sample log file used for analysis.

**utilities.py**

Contains generator-based functions for processing logs:

- `read_logs`
- `filter_logs`
- `count_logs_by_level`

These functions demonstrate how generators can be used to process large log files efficiently.

**main.py**

Entry point of the program that reads logs and performs streaming analysis.

---

## Features

The analyzer performs the following operations:

- Reads log files as a **stream using generators**
- Filters logs by log level (INFO, ERROR, WARNING)
- Counts logs by severity level
- Demonstrates generator-based data pipelines

---

## Example Output
```brew
=== Streaming Log Analyzer ===

All logs:
INFO User login
ERROR Database connection failed
INFO File uploaded
WARNING Disk usage high
INFO User logout
ERROR Timeout while processing request
INFO Backup completed
WARNING CPU temperature high

Error logs:
ERROR Database connection failed
ERROR Timeout while processing request

Log counts:
{'INFO': 4, 'WARNING': 2, 'ERROR': 2}
```


---

## How to Run

From the project directory:
```brew
python main.py
```


---

## Learning Goal

The purpose of this project is to demonstrate **lazy evaluation using generators**.

Instead of loading an entire file into memory, the program processes logs **one line at a time**, which is much more memory-efficient.

This pattern is widely used in:

- large-scale data processing
- machine learning data pipelines
- streaming analytics
- system monitoring tools


---

## Author

**Sumit Barua**  
MS Computer Science  
Western Michigan University