import csv, logging

def load_sales(filename):
    sales_list = list()
    
    try:
        with open(filename) as file:
            csvreader = csv.DictReader(file)
            
            for item in csvreader:
                item['amount'] = int(item['amount'])
                sales_list.append(item)
    except FileNotFoundError:
        logging.error(f"File {filename} Not Found!")
    except ValueError:
        logging.error("Invalid numeric value in the dataset.")
    
    return sales_list

class SalesAnalyzer:
    def __init__(self, data):
        self.data = data
    
    def total_revenue(self):
        total = 0
        
        try:
            for item in self.data:
                total += item['amount']
                return total
        except Exception as e:
            logging.error(f"Revenue calculation failed: {e}")
            return 0
    
    def top_product(self):
        top_sales_dict = dict()
        
        for item in self.data:
            top_sales_dict[item['product']] = top_sales_dict.get(item['product'], 0) + item['amount']
            
        return max(top_sales_dict, key=top_sales_dict.get)
        