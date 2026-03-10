# Function 1 — Top N sales
def top_sales(data, n):
    return sorted(data, key=lambda x: x[2], reverse=True)[:n]

# Function 2 — Sort by customer name
def sort_by_customer(data):
    return sorted(data, key=lambda x:x[0])

# Function 3 — Sort by product
def sort_by_product(data):
    return sorted(data, key=lambda x: x[1])

# Function 4 — Total sales per customer
def total_sales_per_customer(data):
    total_sales_dict = dict()
    
    for name, product, price in data:
        total_sales_dict[name] = total_sales_dict.get(name, 0) + price
    
    return total_sales_dict

# Function 5 — Top earning customer
def top_customer(data):
    max_earning = 0
    max_customer = None
    
    for key, value in total_sales_per_customer(data).items():
        if value > max_earning:
            max_earning = value
            max_customer = key
    
    return max_customer

# Function 6 — Top product by revenue
def top_product(data):
    top_product_dict = dict()
    top_product_name = None
    top_earning_product = 0
    
    for name, product, price in data:
        top_product_dict[product] = top_product_dict.get(product, 0) + price
    
    for key, value in top_product_dict.items():
        if value > top_earning_product:
            top_earning_product = value
            top_product_name = key

    return top_product_name
