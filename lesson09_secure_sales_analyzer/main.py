import logging
from analyzer import *


if __name__ == '__main__':
    # Step 1 — Logging Setup
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    
    logging.info("Program started")

    sales = load_sales("sales_data.csv")
    # print(sales)

    analyzer = SalesAnalyzer(sales)

    print("Total revenue:", analyzer.total_revenue())
    print("Top product:", analyzer.top_product())

    logging.info("Program finished")