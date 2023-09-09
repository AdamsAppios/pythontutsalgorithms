def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    # Choose a pivot element (in this case, the last element)
    pivot = arr[-1]

    # Partition the array into elements less than and greater than the pivot
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]

    # Recursively apply quick_sort to both partitions and combine them with the pivot
    return quick_sort(left) + [pivot] + quick_sort(right)

# Example usage:
arr = [12, 11, 13, 5, 6, 7]
sorted_arr = quick_sort(arr)
print("Sorted array:", sorted_arr)
