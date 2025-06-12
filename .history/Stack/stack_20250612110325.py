class Stack:
    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.append(item) # to add item on top since its a list or array in python we use the sae isnert at the top which is append

    def pop(self):
        if not self.is_empty():
            return self.items.pop() #remove the top elemnt
        
    return print("stack is full")    