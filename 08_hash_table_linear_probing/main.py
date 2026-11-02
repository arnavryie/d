class HashTableLinearProbing:
    def __init__(self, size=10):
        self.size = size
        self.table = [None] * size

    def hash_func(self, key):
        return key % self.size

    def insert(self, key):
        start = self.hash_func(key)
        idx = start
        while self.table[idx] is not None and self.table[idx] != "__DELETED__":
            if self.table[idx] == key:
                print(f"Key {key} already exists.")
                return
            idx = (idx + 1) % self.size
            if idx == start:
                print("Hash Table is Full!")
                return
        self.table[idx] = key
        print(f"Inserted key {key} at index {idx}")

    def search(self, key):
        start = self.hash_func(key)
        idx = start
        while self.table[idx] is not None:
            if self.table[idx] == key:
                print(f"Key {key} found at index {idx}")
                return idx
            idx = (idx + 1) % self.size
            if idx == start:
                break
        print(f"Key {key} not found")
        return -1

    def delete(self, key):
        idx = self.search(key)
        if idx != -1:
            self.table[idx] = "__DELETED__"
            print(f"Deleted key {key}")

    def display(self):
        print("\n--- Hash Table (Linear Probing) ---")
        for i in range(self.size):
            print(f"Index [{i}]: {self.table[i]}")

ht = HashTableLinearProbing(10)
ht.insert(15)
ht.insert(25)
ht.insert(35)
ht.insert(42)
ht.display()
ht.search(25)
ht.delete(25)
ht.display()

while True:
    print("\n1. Insert | 2. Search | 3. Delete | 4. Display | 5. Exit")
    ch = input("Enter choice: ").strip()
    if ch == "1":
        k = int(input("Key (int): "))
        ht.insert(k)
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
