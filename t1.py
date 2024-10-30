import csv
from collections import defaultdict

def read_csv(file_path):
    data = []
    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row)
    return data

def calculate_statistics(data):
    stats = defaultdict(lambda: {'count': 0, 'total': 0})
    for row in data:
        for key, value in row.items():
            try:
                value = float(value)
                stats[key]['count'] += 1
                stats[key]['total'] += value
            except ValueError:
                continue
    return stats

def print_statistics(stats):
    for key, value in stats.items():
        count = value['count']
        total = value['total']
        average = total / count if count != 0 else 0
        print(f"Column: {key}")
        print(f"  Count: {count}")
        print(f"  Total: {total}")
        print(f"  Average: {average:.2f}")

if __name__ == "__main__":
    file_path = 'data.csv'  # Replace with your CSV file path
    data = read_csv(file_path)
    stats = calculate_statistics(data)
    print_statistics(stats)
