import csv

# Step 1 — Reading a CSV File
def load_sales_data(filename) -> list:
    data = list()
    
    with open(filename, 'r') as file:
        csvreader = csv.DictReader(file)
        
        for row in csvreader:
            row['amount'] = int(row['amount'])
            data.append(row)
    
    return data
            

# Function 1 — Count total records
def count_records(data) -> int:
    return len(data)

# Function 2 — Unique products
def get_unique_products(data):
    unique_products = set()
    
    for item in data:
        unique_products.add(item['product'])
    
    return sorted(unique_products)

# Function 3 — Total revenue
def total_revenue(data) -> int:
    total = 0
    
    for item in data:
        total += item['amount']
    
    return total

# Function 4 — Revenue per region
def revenue_per_region(data) -> dict:
    revenue_dict = dict()
    
    for item in data:
        revenue_dict[item['region']] = revenue_dict.get(item['region'], 0) + item['amount']
    
    return revenue_dict

# Function 5 — Best selling product
def best_selling_product(data):
    best_selling_dict = dict()
    max_value = 0
    max_product = None
    
    for item in data:
        best_selling_dict[item['product']] = best_selling_dict.get(item['product'], 0) + item['amount']
    
    for key, value in best_selling_dict.items():
        if value > max_value:
            max_value = value
            max_product = key
            
    return max_product

# Function 6 — High value transactions
def high_value_sales(data, threshold):
    high_sales_list = list()
    
    for item in data:
        if item['amount'] >= threshold:
            high_sales_list.append(item)
    
    return high_sales_list