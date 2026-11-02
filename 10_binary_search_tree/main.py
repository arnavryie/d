class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, val):
        def _insert(root, val):
            if not root:
                return Node(val)
            if val < root.val:
                root.left = _insert(root.left, val)
            elif val > root.val:
                root.right = _insert(root.right, val)
            return root
        self.root = _insert(self.root, val)
        print(f"Inserted {val}")

    def search(self, val):
        curr = self.root
        while curr:
            if curr.val == val:
                print(f"Found {val} in BST")
                return True
            elif val < curr.val:
                curr = curr.left
            else:
                curr = curr.right
        print(f"{val} not found in BST")
        return False

    def delete(self, val):
        def _min_value_node(node):
            curr = node
            while curr.left:
                curr = curr.left
            return curr

        def _delete(root, val):
            if not root:
                return root
            if val < root.val:
                root.left = _delete(root.left, val)
            elif val > root.val:
                root.right = _delete(root.right, val)
            else:
                if not root.left:
                    return root.right
                elif not root.right:
                    return root.left
                temp = _min_value_node(root.right)
                root.val = temp.val
                root.right = _delete(root.right, temp.val)
            return root

        if self.search(val):
            self.root = _delete(self.root, val)
            print(f"Deleted {val}")

    def display(self):
        res = []
        def inorder(root):
            if root:
                inorder(root.left)
                res.append(root.val)
                inorder(root.right)
        inorder(self.root)
        print("Inorder BST:", res if res else "Tree is empty")

tree = BST()
for x in [50, 30, 70, 20, 40, 60, 80]:
    tree.insert(x)

tree.display()
tree.search(40)
tree.delete(30)
tree.display()

while True:
    print("\n1. Insert | 2. Search | 3. Delete | 4. Display | 5. Exit")
    ch = input("Enter choice: ").strip()
    if ch == "1":
        v = int(input("Value to insert: "))
        tree.insert(v)
    elif ch == "2":
        v = int(input("Value to search: "))
        tree.search(v)
    elif ch == "3":
        v = int(input("Value to delete: "))
        tree.delete(v)
    elif ch == "4":
        tree.display()
    elif ch == "5":
        break
    else:
        print("Invalid choice")
