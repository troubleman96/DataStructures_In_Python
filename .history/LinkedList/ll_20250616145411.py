# Define a Node - the building block of a linked list
class Node:
    def __init__(self, data):
        self.data = data  # The value stored in the node
        self.next = None  # Pointer to the next node

# Define the LinkedList class to manage nodes
class LinkedList:
    def __init__(self):
        self.head = None  # Start with an empty list

    # Add a new node at the end of the list
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            # If the list is empty, set head to the new node
            self.head = new_node
        else:
            # Traverse to the end of the list and add the node
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    # Add a node at the beginning
    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head  # Point new node to the old head
        self.head = new_node       # Move head to point to the new node

    # Insert at a specific position (0-based index)
    def insert_at_position(self, position, data):
        if position < 0:
            print("Invalid position!")
            return

        if position == 0:
            self.prepend(data)
            return

        new_node = Node(data)
        current = self.head
        index = 0

        while current and index < position - 1:
            current = current.next
            index += 1

        if current is None:
            print("Position out of bounds")
            return

        new_node.next = current.next
        current.next = new_node

    # Delete a node by value
    def delete_by_value(self, value):
        current = self.head

        if current is None:
            print("List is empty")
            return

        if current.data == value:
            self.head = current.next  # Delete head
            return

        prev = None
        while current and current.data != value:
            prev = current
            current = current.next

        if current is None:
            print("Value not found")
            return

        prev.next = current.next  # Bypass the node to delete it

    # Search for a value in the list
    def search(self, value):
        current = self.head
        position = 0
        while current:
            if current.data == value:
                return position
            current = current.next
            position += 1
        return -1  # Not found

    # Display all elements in the list
    def display(self):
        current = self.head
        if current is None:
            print("List is empty")
            return

        print("Linked List Elements:")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # Return the length of the list
    def length(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count


# 🔍 Testing the LinkedList
if __name__ == "__main__":
    ll = LinkedList()

    # Add elements
    ll.append(10)
    ll.append(20)
    ll.append(30)

    ll.display()  # 10 -> 20 -> 30 -> None

    # Insert at beginning
    ll.prepend(5)
    ll.display()  # 5 -> 10 -> 20 -> 30 -> None

    # Insert at position
    ll.insert_at_position(2, 15)
    ll.display()  # 5 -> 10 -> 15 -> 20 -> 30 -> None

    # Delete by value
    ll.delete_by_value(20)
    ll.display()  # 5 -> 10 -> 15 -> 30 -> None

    # Search
    pos = ll.search(15)
    print(f"Value 15 found at position: {pos}")

    # Length
    print(f"Length of list: {ll.length()}")
