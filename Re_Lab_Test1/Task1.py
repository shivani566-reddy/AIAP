import time
import random

# ------------------------------
# Bubble Sort Implementation
# ------------------------------
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


# ------------------------------
# Insertion Sort Implementation
# ------------------------------
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key


# ------------------------------
# Compare Execution Time
# ------------------------------
# Create a random list of numbers
size = 5000
data = [random.randint(1, 10000) for _ in range(size)]

# Copy lists for fair comparison
arr1 = data.copy()
arr2 = data.copy()

# Bubble Sort timing
start = time.time()
bubble_sort(arr1)
bubble_time = time.time() - start

# Insertion Sort timing
start = time.time()
insertion_sort(arr2)
insertion_time = time.time() - start

print("Execution Time Comparison:")
print(f"Bubble Sort:    {bubble_time:.6f} seconds")
print(f"Insertion Sort: {insertion_time:.6f} seconds")
