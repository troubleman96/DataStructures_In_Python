class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = [None] * size
        self.top = -1
    
    def is_full(self):
        return self.top == self.size - 1
    
    def is_empty(self):
        return self.top == -1
    
    def push(self, item):
        if self.is_full():
            print("Stack is full! Cannot push item.")
        else:
            self.top += 1
            self.stack[self.top] = item
            print(f"Pushed {item} to stack")
    
    def pop(self):
        if self.is_empty():
            print("Stack is empty! Cannot pop item.")
            return None
        else:
            item = self.stack[self.top]
            self.stack[self.top] = None
            self.top -= 1
            print(f"Popped {item} from stack")
            return item
    
    def display(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            print("Stack contents (top to bottom):")
            for i in range(self.top, -1, -1):
                print(self.stack[i])

def main():
    size = int(input("Enter the size of the stack: "))
    stack = Stack(size)
    
    while True:
        print("\n1. Push")
        print("2. Pop")
        print("3. Display")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            item = input("Enter item to push: ")
            stack.push(item)
        elif choice == '2':
            stack.pop()
        elif choice == '3':
            stack.display()
        elif choice == '4':
            print("Exiting program")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()