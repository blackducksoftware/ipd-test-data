def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return arr

# Example usage
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = bubble_sort(arr)
print("Sorted array:", sorted_arr)


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


def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

if __name__ == "__main__":
    arr = [11, 12, 22, 25, 34, 64, 90]
    target = 25
    result = binary_search(arr, target)

    if result != -1:
        print(f"Element found at index {result}")
    else:
        print("Element not found")

