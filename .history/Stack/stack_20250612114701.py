class Stack:
    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.append(item) # to add item on top since its a list or array in python we use the sae isnert at the top which is append

    def pop(self):
        if not self.is_empty():
            return self.items.pop() #remove the top elemnt
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]   ##provide the top elemnt
        return None

    def is_empty(self):
        return len(self.items) == 0  ##compare the legnth of the stack to check if its empty

    def size(self):
        return len(self.items) 
    
    def display(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            print("Stack items (top to bottom):")
            for item in reversed(self.items):
                print(item)    
    

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.peek())
stack.display()
print("the size of the stack is: ", stack.size())
stack.pop()
stack.display()