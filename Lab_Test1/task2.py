class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class BasicLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        """Insert a new node at the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def delete(self, data):
        """Delete the first node with the given data."""
        curr = self.head
        prev = None
        while curr:
            if curr.data == data:
                if prev:
                    prev.next = curr.next
                else:
                    self.head = curr.next
                return True
            prev = curr
            curr = curr.next
        return False

    def display(self):
        """Display the linked list elements."""
        elements = []
        curr = self.head
        while curr:
            elements.append(str(curr.data))
            curr = curr.next
        print(" -> ".join(elements) if elements else "List is empty.")

# Few-shot prompt with examples
def linked_list_prompt():
    ll = BasicLinkedList()
    print("Example: Insert elements 1, 2, 3")
    for i in [1, 2, 3]:
        ll.insert(i)
    ll.display()
    print("Example: Delete element 2")
    ll.delete(2)
    ll.display()
    print("--- Now it's your turn ---")

    ll = BasicLinkedList()
    while True:
        cmd = input("Enter command (insert <value>/delete <value>/display/exit): ").strip()
        if cmd.startswith("insert "):
            value = input("Enter value to insert: ")
            ll.insert(value)
        elif cmd.startswith("delete "):
            value = input("Enter value to delete: ")
            if ll.delete(value):
                print(f"Deleted {value} from list.")
            else:
                print(f"Value {value} not found.")
        elif cmd == "display":
            ll.display()
        elif cmd == "exit":
            break
        else:
            print("Invalid command. Try again.")

if __name__ == "__main__":
    linked_list_prompt()
