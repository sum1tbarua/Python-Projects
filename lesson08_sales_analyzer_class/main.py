from sales_data import sales
from analyzer import SalesAnalyzer

if __name__ == '__main__':

    analyzer = SalesAnalyzer(sales)

    print("=== Sales Analyzer (OOP) ===")
    print()

    print("Total records:", analyzer.count_records())
    print()

    print("Total revenue:", analyzer.total_revenue())
    print()

    print("Revenue per product:")
    print(analyzer.revenue_per_product())
    print()

    print("Top customer:")
    print(analyzer.top_customer())
    print()

    print("Top 3 sales:")
    print(analyzer.top_sales(3))