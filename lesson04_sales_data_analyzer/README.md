# Lesson 4 – Sales Data Analyzer (CSV Processing)

This project is part of my **Python learning repository**, where I build small projects lesson-by-lesson to practice real programming concepts.

Lesson 4 focuses on **reading and analyzing CSV data using Python**.

The program loads a sales dataset from a CSV file and performs several analytics operations such as computing revenue statistics and identifying high-value transactions.

---

# Concepts Practiced

- Reading CSV files using `csv.DictReader`
- Converting CSV data into Python objects
- Working with lists of dictionaries
- Data aggregation using dictionaries
- Writing reusable utility functions
- Organizing code into modules

---

# Dataset Format

The dataset is stored in `sales_data.csv`.

Each row represents a sales transaction and follows this format:
```brew
name,region,product,amount
```

Example:
```brew
Alice,North,Laptop,1200
```


After loading the file, each row becomes a Python dictionary:

```brew  
{
"name": "Alice",
"region": "North",
"product": "Laptop",
"amount": 1200
}
```

---

# Project Structure
```brew 
lesson04_sales_data_analyzer
│
├── main.py
├── utilities.py
├── sales_data.csv
└── README.md
```


### File Descriptions

**sales_data.csv**

Contains the sales dataset used for analysis.

**utilities.py**

Contains reusable functions used to process the dataset:

- load_sales_data
- count_records
- get_unique_products
- total_revenue
- revenue_per_region
- best_selling_product
- high_value_sales

**main.py**

Program entry point that loads the dataset and prints analysis results.

---

# Features

The analyzer performs the following operations:

- Counts total records
- Identifies unique products
- Computes total revenue
- Calculates revenue per region
- Determines the best-selling product
- Finds transactions above a specified value

---

# Example Output
```brew
=== Sales Data Analyzer ===

Total records: 8

Unique products:

Laptop

Phone

Tablet

Total revenue:
7450

Revenue per region:

North: 3350

South: 2600

West: 1500

Best selling product:

Laptop

High value sales (>1000):

Alice | North | Laptop | 1200

David | West | Laptop | 1500

Bob | South | Laptop | 1100
```


---

# How to Run

From the project directory:
```brew
python main.py
```


---

# Learning Goal

The purpose of this project is to practice **processing structured data stored in CSV files** using Python.

File-based data processing is a common task in:

- data science
- machine learning pipelines
- backend analytics
- automation scripts

Future lessons will expand this repository with projects involving:

- more advanced data processing
- cleaner Python patterns
- algorithmic problem solving
- automation tools