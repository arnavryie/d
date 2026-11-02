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

ids = [104, 101, 115, 108, 120, 102]
print("Customer IDs:", ids)

user_in = input("Enter customer ID to search: ").strip()
target = int(user_in) if user_in else 108

idx = linear_search(ids, target)
if idx != -1:
    print(f"Linear Search: Customer {target} found at index {idx}")
else:
    print(f"Linear Search: Customer {target} not found")

sorted_ids = sorted(ids)
print("\nSorted IDs for Binary Search:", sorted_ids)
b_idx = binary_search(sorted_ids, target)
if b_idx != -1:
    print(f"Binary Search: Customer {target} found at index {b_idx}")
else:
    print(f"Binary Search: Customer {target} not found")
