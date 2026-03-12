import logging, argparse
from inspector import *


if __name__ == '__main__':
    logging.basicConfig(
        level = logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    
    logging.info("Program started")
    
    parser = argparse.ArgumentParser(
        description="Dataset Inspector CLI Tool"
    )
    
    parser.add_argument("--file", required=True)
    parser.add_argument("--rows", action="store_true")
    parser.add_argument("--columns", action="store_true")
    parser.add_argument("--head", type=int)
    parser.add_argument("--summary", action="store_true")
    
    
    args = parser.parse_args()
    data = load_dataset(args.file)
    inspect = DatasetInspector(data)
    
    # print(data)
    
    if args.rows:
        print("Total rows: ", inspect.row_count())
    
    if args.columns:
        print("Columns: ", inspect.columns())
        
    if args.head:
        print(inspect.head(args.head))
    
    if args.summary:
        print(inspect.summary())
    
    logging.info("Program finished!")
    
    