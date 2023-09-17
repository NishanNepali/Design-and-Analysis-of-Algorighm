def binary_search(arr, key):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] == key:
            return mid  # Key found
        elif arr[mid] < key:
            left = mid + 1
        else:
            right = mid - 1

    return -1  # Key not found

# Sorted list of numbers
arr = [2, 4, 5, 7, 8, 9, 11, 12, 13]

key = int(input("Enter the search item: "))  # Search Item
result = binary_search(arr, key)

if result != -1:
    print(f"Key found at index {result}")
else:
    print("Key not found")
