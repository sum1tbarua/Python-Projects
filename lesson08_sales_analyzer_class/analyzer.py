# Step 1 — Create the Class

class SalesAnalyzer:
    def __init__(self, data):
        self.data = data
    
    # Step 2 — Count records
    def count_records(self):
        return len(self.data)

    # Step 3 — Total revenue
    def total_revenue(self):
        sum = 0
        for name, product, price in self.data:
            sum += price
        return sum

    # Step 4 — Revenue per product
    def revenue_per_product(self):
        product_revenue_dict = dict()
        
        for name, product, price in self.data:
            product_revenue_dict[product] = product_revenue_dict.get(product, 0) + price
        
        return product_revenue_dict

    # Step 5 — Top customer
    def top_customer(self):
        top_customer_dict = dict()
        
        for name, product, price in self.data:
            top_customer_dict[name] = top_customer_dict.get(name, 0) + price
            
        return max(top_customer_dict, key=top_customer_dict.get)
        

    # Step 6 — Top N sales
    def top_sales(self, top_n):
        return sorted(self.data, key=lambda x: x[2], reverse=True)[:top_n]
        