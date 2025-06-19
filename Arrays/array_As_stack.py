# Stack implementation using a Python list (array)
class Stack:
    # Constructor to initialize the stack
    def __init__(self, capacity):
        # capacity: maximum number of elements the stack can hold
        self.capacity = capacity
        # stack: list to store stack elements
        self.stack = []
        # top: index of the top element (points to empty slot initially) or check = if the stack is empty
        self.top = -1

    # Push operation to add an element to the top of the stack
    def push(self, item):
        # Check if stack is full (overflow condition)
        if self.top + 1 >= self.capacity:
            print("Stack Overflow! Cannot push item:", item)
            return False
        # Increment top and append item to stack
        self.top += 1
        self.stack.append(item)
        print(f"Pushed {item} to stack")
        return True

    # Pop operation to remove and return the top element
    def pop(self):
        # Check if stack is empty (underflow condition)
        if self.top < 0:
            print("Stack Underflow! Cannot pop from empty stack")
            return None
        # Get top element, remove it, and decrement top
        item = self.stack.pop()
        self.top -= 1
        print(f"Popped {item} from stack")
        return item

    # Peek operation to view the top element without removing it
    def peek(self):
        # Check if stack is empty
        if self.top < 0:
            print("Stack is empty! Nothing to peek")
            return None
        # Return top element
        return self.stack[self.top]

    # Check if stack is empty
    def is_empty(self):
        return self.top < 0

    # Check if stack is full
    def is_full(self):
        return self.top + 1 >= self.capacity

    # Get current size of stack
    def size(self):
        return self.top + 1

# Example usage of the Stack class
if __name__ == "__main__":
    # Create a stack with capacity 5
    stack = Stack(5)
    
    # Test push operations
    stack.push(1)  # Stack: [1]
    stack.push(2)  # Stack: [1, 2]
    stack.push(3)  # Stack: [1, 2, 3]
    
    # Test peek
    print("Top element:", stack.peek())  # Should print 3
    
    # Test pop operations
    stack.pop()  # Stack: [1, 2]
    stack.pop()  # Stack: [1]
    
    # Test size
    print("Current stack size:", stack.size())  # Should print 1
    
    # Test is_empty and is_full
    print("Is stack empty?", stack.is_empty())  # Should print False
    print("Is stack full?", stack.is_full())    # Should print False
    
    # Test overflow
    stack.push(4)  # Stack: [1, 4]
    stack.push(5)  # Stack: [1, 4, 5]
    stack.push(6)  # Stack: [1, 4, 5, 6]
    stack.push(7)  # Should print Stack Overflow
    
    # Test underflow
    stack.pop()  # Stack: [1, 4, 5]
    stack.pop()  # Stack: [1, 4]
    stack.pop()  # Stack: [1]
    stack.pop()  # Stack: []
    stack.pop()  # Should print Stack Underflow