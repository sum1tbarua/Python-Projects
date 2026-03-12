import csv, logging

class DatasetInspector:
    def __init__(self, data):
        self.data = data
    
    def row_count(self):
        return len(self.data)
    
    def columns(self):  
        if not self.data:
            return []
        
        return list(self.data[0].keys())
    
    def head(self, n):
        return self.data[:n]
    
    def summary(self):
        
        summary_dict = dict()
        
        for column in self.columns():
            values = {row[column] for row in self.data}
            summary_dict[column] = {
                'unique_values': len(values)
            }
        
        return summary_dict
            
    

def load_dataset(filename):
    data_list = list()
    
    try:
        with open(filename) as file:
            csv_reader = csv.DictReader(file)
            
            for rows in csv_reader:
                rows['id'] = int(rows['id'])
                data_list.append(rows)
            
    except FileNotFoundError:
        logging.error(f'File {filename} Not Found')
    
    finally:
        logging.info("File Import Process finished!")
    
    return data_list