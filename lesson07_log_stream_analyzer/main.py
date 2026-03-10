from utilities import *

if __name__ == '__main__':

    print("=== Streaming Log Analyzer ===")
    print()

    log_stream = read_logs("logs.txt")

    print("All logs:")
    for log in read_logs("logs.txt"):
        print(log)

    print()

    print("Error logs:")
    for log in filter_logs(read_logs("logs.txt"),"ERROR"):
        print(log)

    print()

    print("Log counts:")
    print(count_logs_by_level(read_logs("logs.txt")))