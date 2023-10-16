def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1

# Example usage:
arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
target = 12

linear_result = linear_search(arr, target)
binary_result = binary_search(arr, target)

if linear_result != -1:
    print(f"Linear search: Element {target} found at index {linear_result}")
else:
    print(f"Linear search: Element {target} not found")

if binary_result != -1:
    print(f"Binary search: Element {target} found at index {binary_result}")
else:
    print(f"Binary search: Element {target} not found")
