class HashTableChaining:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_func(self, key):
        return key % self.size

    def insert(self, key, value):
        idx = self.hash_func(key)
        for item in self.table[idx]:
            if item[0] == key:
                item[1] = value
                print(f"Updated key {key}")
                return
        self.table[idx].append([key, value])
        print(f"Inserted ({key}, '{value}') at bucket {idx}")

    def search(self, key):
        idx = self.hash_func(key)
        for item in self.table[idx]:
            if item[0] == key:
                print(f"Found -> Key: {key}, Value: {item[1]}")
                return item[1]
        print(f"Key {key} not found")
        return None

    def delete(self, key):
        idx = self.hash_func(key)
        for i, item in enumerate(self.table[idx]):
            if item[0] == key:
                del self.table[idx][i]
                print(f"Deleted key {key}")
                return
        print(f"Key {key} not found to delete")

    def display(self):
        print("\n--- Hash Table (Chaining) ---")
        for i in range(self.size):
            print(f"Index [{i}]: {self.table[i]}")

ht = HashTableChaining(10)
ht.insert(12, "Apples")
ht.insert(22, "Bananas")
ht.insert(35, "Cherries")
ht.insert(42, "Dates")
ht.display()
ht.search(22)
ht.delete(35)
ht.display()

while True:
    print("\n1. Insert | 2. Search | 3. Delete | 4. Display | 5. Exit")
    ch = input("Enter choice: ").strip()
    if ch == "1":
        k = int(input("Key (int): "))
        v = input("Value: ")
        ht.insert(k, v)
    elif ch == "2":
        k = int(input("Key to search: "))
        ht.search(k)
    elif ch == "3":
        k = int(input("Key to delete: "))
        ht.delete(k)
    elif ch == "4":
        ht.display()
    elif ch == "5":
        break
    else:
        print("Invalid choice")
