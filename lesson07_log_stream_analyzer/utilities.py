# Function 1 — Log Generator
def read_logs(filename):
    with open(filename) as file:
        for line in file:
            yield line.strip()

# Function 2 — Filter Logs by Level 
def filter_logs(logs, level):
    for line in logs:
        if line.startswith(level):
            yield line

# Function 3 — Count Logs by Level
def count_logs_by_level(logs):
    count_dict = dict()
    
    for line in logs:
        level = line.split()[0]
        
        count_dict[level] = count_dict.get(level, 0) + 1
    
    return count_dict