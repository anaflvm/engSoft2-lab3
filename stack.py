class Stack:
    def __init__(self):
        self.elements = []
        self.size = 0
    
    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False
    
    def push(self, element):
        self.elements.append(element)
        self.size += 1
    
    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty!")

        element = self.elements.pop()
        self.size -= 1
        return element