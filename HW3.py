import sys

def quickSort(arr, l, r):
    if r - l <= 11:
        return insertionSort(arr, l, r)
    pivot = medianOfMedians(arr, l, r)
    i = l - 1
    for j in range(l, r):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    pivotIndex = i + 1
    quickSort(arr, l, pivotIndex - 1)
    quickSort(arr, pivotIndex + 1, r)
    return arr

def medianOfMedians(arr, l, r):
    n = r - l + 1
    sublists = [arr[l + i:l + i + 5] for i in range(0, n, 5)]
    medians = [sorted(sublist)[len(sublist) // 2] for sublist in sublists]
    return quickSort(medians, 0, len(medians) - 1)[len(medians) // 2]

def insertionSort(arr, l, r):
    for i in range(l + 1, r + 1):
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j = j - 1
    return arr

# Choosing the value of r as 11
r = 11

# Read in the input elements from the file
input_file = sys.argv[1]
with open(input_file, "r") as f:
    arr = list(map(int, f.readline().split()))

# Sort the elements
arr = quickSort(arr, 0, len(arr) - 1)

# Print the sorted elements
print(" ".join(str(x) for x in arr))
