from utilities import *

if __name__ == '__main__':
    
    print("=== Sales Data Analyzer ===")
    print()
    
    # Loading the data
    data = load_sales_data('sales_data.csv')
    
    # Total records
    print(f'Total records: {count_records(data)}')
    print()
    
    # Unique products
    print('Unique products:')
    print(get_unique_products(data))
    print()
    
    # Total revenue
    print("Total revenue:")
    print(total_revenue(data))
    print()
    
    print("Revenue per region:")
    print(revenue_per_region(data))
    print()

    print("Best selling product:")
    print(best_selling_product(data))
    print()

    print("High value sales (>1000):")
    print(high_value_sales(data, 1000))