from sales_data import sales
from utilities import *

if __name__ == '__main__':
    print("=== Sales Ranking Analyzer ===")
    print()

    print("Top 3 sales:")
    print(top_sales(sales,3))
    print()

    print("Sorted by customer:")
    print(sort_by_customer(sales))
    print()

    print("Sorted by product:")
    print(sort_by_product(sales))
    print()

    print("Total sales per customer:")
    print(total_sales_per_customer(sales))
    print()

    print("Top earning customer:")
    print(top_customer(sales))
    print()

    print("Top product by revenue:")
    print(top_product(sales))