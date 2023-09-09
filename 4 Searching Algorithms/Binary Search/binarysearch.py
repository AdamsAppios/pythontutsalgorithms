def binary_search(arr, target):
    left = 0  # Leftmost index of the search range
    right = len(arr) - 1  # Rightmost index of the search range

    while left <= right:
        mid = (left + right) // 2  # Calculate the middle index

        if arr[mid] == target:
            return mid  # Target element found, return its index
        elif arr[mid] < target:
            left = mid + 1  # Target is in the right half
        else:
            right = mid - 1  # Target is in the left half

    return -1  # Target element not found in the array

# Example usage:
arr = [2, 4, 7, 10, 23, 45, 56, 67, 78, 89]
target = 4
result = binary_search(arr, target)

if result != -1:
    print(f"Element {target} found at index {result}")
else:
    print(f"Element {target} not found in the array")
