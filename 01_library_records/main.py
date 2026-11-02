records = {
    "Rahul": ["Math", "Physics"],
    "Sneha": ["Chemistry"],
    "Amit": [],
    "Pooja": ["Math", "History", "Physics"],
    "Rohan": []
}

def average_borrowed(data):
    total = sum(len(books) for books in data.values())
    return total / len(data) if data else 0

def book_stats(data):
    counts = {}
    for books in data.values():
        for b in books:
            counts[b] = counts.get(b, 0) + 1
    if not counts:
        return None, None, None
    highest = max(counts, key=counts.get)
    lowest = min(counts, key=counts.get)
    mode = highest
    return highest, lowest, mode

def zero_borrowers(data):
    return sum(1 for books in data.values() if len(books) == 0)

print("--- Library Borrowing Records ---")
avg = average_borrowed(records)
hi, lo, mode = book_stats(records)
zero = zero_borrowers(records)

print("Average books borrowed per member:", avg)
print("Highest borrowed book:", hi)
print("Lowest borrowed book:", lo)
print("Most frequently borrowed book (Mode):", mode)
print("Members with zero borrowings:", zero)

print("\n--- Time and Space Complexity ---")
print("Average Calculation: Time O(N), Space O(1)")
print("Highest/Lowest/Mode: Time O(N*M), Space O(U)")
print("Zero Borrowers Count: Time O(N), Space O(1)")
