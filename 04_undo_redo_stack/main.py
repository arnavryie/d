class TextEditor:
    def __init__(self):
        self.doc = ""
        self.undo_stack = []
        self.redo_stack = []

    def make_change(self, text):
        self.undo_stack.append(self.doc)
        self.doc += text
        self.redo_stack.clear()
        print("Updated Document:", self.doc)

    def undo(self):
        if not self.undo_stack:
            print("Nothing to undo.")
            return
        self.redo_stack.append(self.doc)
        self.doc = self.undo_stack.pop()
        print("After Undo:", self.doc)

    def redo(self):
        if not self.redo_stack:
            print("Nothing to redo.")
            return
        self.undo_stack.append(self.doc)
        self.doc = self.redo_stack.pop()
        print("After Redo:", self.doc)

    def display(self):
        print("Current Document State: [" + self.doc + "]")

editor = TextEditor()
print("Demonstrating default actions:")
editor.make_change("Hello ")
editor.make_change("World!")
editor.display()
editor.undo()
editor.display()
editor.redo()
editor.display()

while True:
    print("\n1. Make Change | 2. Undo | 3. Redo | 4. Display | 5. Exit")
    ch = input("Enter choice: ").strip()
    if ch == "1":
        t = input("Enter text to append: ")
        editor.make_change(t)
    elif ch == "2":
        editor.undo()
    elif ch == "3":
        editor.redo()
    elif ch == "4":
        editor.display()
    elif ch == "5":
        break
    else:
        print("Invalid choice")
