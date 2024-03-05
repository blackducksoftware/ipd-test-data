import random

def shuffle_sort(arr):
    n = len(arr)
    for i in range(n-1):
        j = random.randint(i, n-1)
        arr[i], arr[j] = arr[j], arr[i]
    
    return arr

# Example usage
arr = [5, 2, 8, 3, 9, 1]
sorted_arr = shuffle_sort(arr)
print(sorted_arr)
