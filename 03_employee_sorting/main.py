def selection_sort(arr):
    a = arr.copy()
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a

def bubble_sort(arr):
    a = arr.copy()
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

salaries = [45000.50, 78000.0, 32000.75, 95000.20, 60000.0, 88000.80, 52000.0, 99000.0]
print("Original Salaries:", salaries)

sel_sorted = selection_sort(salaries)
print("\nSorted with Selection Sort:", sel_sorted)

bub_sorted = bubble_sort(salaries)
print("Sorted with Bubble Sort:", bub_sorted)

print("\nTop 5 Highest Salaries:")
for s in bub_sorted[-5:][::-1]:
    print(s)
