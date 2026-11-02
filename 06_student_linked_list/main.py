class Node:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks
        self.next = None

class StudentLinkedList:
    def __init__(self):
        self.head = None

    def add(self, roll, name, marks):
        new_node = Node(roll, name, marks)
        if not self.head:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node
        print(f"Student {name} (Roll: {roll}) added.")

    def delete(self, roll):
        curr = self.head
        prev = None
        while curr:
            if curr.roll == roll:
                if prev:
                    prev.next = curr.next
                else:
                    self.head = curr.next
                print(f"Student with Roll {roll} deleted.")
                return
            prev = curr
            curr = curr.next
        print(f"Student with Roll {roll} not found.")

    def update(self, roll, name, marks):
        curr = self.head
        while curr:
            if curr.roll == roll:
                curr.name = name
                curr.marks = marks
                print(f"Record for Roll {roll} updated.")
                return
            curr = curr.next
        print(f"Student with Roll {roll} not found.")

    def search(self, roll):
        curr = self.head
        while curr:
            if curr.roll == roll:
                print(f"Found -> Roll: {curr.roll}, Name: {curr.name}, Marks: {curr.marks}")
                return
            curr = curr.next
        print(f"Roll {roll} not found.")

    def to_list(self):
        records = []
        curr = self.head
        while curr:
            records.append((curr.roll, curr.name, curr.marks))
            curr = curr.next
        return records

    def sort_and_display(self, by="roll", descending=False):
        records = self.to_list()
        if not records:
            print("No records available.")
            return
        idx = 0 if by == "roll" else 2
        records.sort(key=lambda x: x[idx], reverse=descending)
        order_str = "Descending" if descending else "Ascending"
        print(f"\nStudent Records sorted by {by} ({order_str}):")
        for r in records:
            print(f"Roll: {r[0]}, Name: {r[1]}, Marks: {r[2]}")

s = StudentLinkedList()
s.add(101, "Rahul", 85.5)
s.add(103, "Sneha", 92.0)
s.add(102, "Amit", 74.0)

s.sort_and_display(by="roll", descending=False)
s.sort_and_display(by="marks", descending=True)

while True:
    print("\n1. Add | 2. Delete | 3. Update | 4. Search | 5. Display/Sort | 6. Exit")
    ch = input("Enter choice: ").strip()
    if ch == "1":
        r = int(input("Roll: "))
        n = input("Name: ")
        m = float(input("Marks: "))
        s.add(r, n, m)
    elif ch == "2":
        r = int(input("Roll to delete: "))
        s.delete(r)
    elif ch == "3":
        r = int(input("Roll to update: "))
        n = input("New Name: ")
        m = float(input("New Marks: "))
        s.update(r, n, m)
    elif ch == "4":
        r = int(input("Roll to search: "))
        s.search(r)
    elif ch == "5":
        by = input("Sort by (roll/marks): ").strip().lower()
        order = input("Order (asc/desc): ").strip().lower()
        s.sort_and_display(by=by, descending=(order == "desc"))
    elif ch == "6":
        break
    else:
        print("Invalid choice")
