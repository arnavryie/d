class EventQueue:
    def __init__(self):
        self.queue = []

    def add_event(self, event):
        self.queue.append(event)
        print(f"Event '{event}' added.")

    def process_next(self):
        if not self.queue:
            print("No events to process.")
            return
        event = self.queue.pop(0)
        print(f"Processed event: {event}")

    def display_pending(self):
        if not self.queue:
            print("No pending events.")
        else:
            print("Pending Events:", self.queue)

    def cancel_event(self, event):
        if event in self.queue:
            self.queue.remove(event)
            print(f"Event '{event}' canceled.")
        else:
            print(f"Event '{event}' not found in pending queue.")

eq = EventQueue()
print("Demonstrating default events:")
eq.add_event("User_Login")
eq.add_event("File_Upload")
eq.add_event("Send_Email")
eq.display_pending()
eq.process_next()
eq.cancel_event("Send_Email")
eq.display_pending()

while True:
    print("\n1. Add Event | 2. Process Next | 3. Display Pending | 4. Cancel Event | 5. Exit")
    ch = input("Enter choice: ").strip()
    if ch == "1":
        ev = input("Enter event name: ")
        eq.add_event(ev)
    elif ch == "2":
        eq.process_next()
    elif ch == "3":
        eq.display_pending()
    elif ch == "4":
        ev = input("Enter event name to cancel: ")
        eq.cancel_event(ev)
    elif ch == "5":
        break
    else:
        print("Invalid choice")
