class Queue:
    def __init__(self):
        self.items = []

    def enequeue(self, item):
        self.items.append(item) ## to add to the queue

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0) #pop and return the front item
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        return None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    def display(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            print("Queue (front to rear): ", self.items)    


queue = Queue()
queue.enequeue(0)
queue.enequeue(1)
queue.enequeue(2)
queue.dequeue()