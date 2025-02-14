class CustomStack:
    def __init__(self):
        self.values = []

    def push(self, value):
        self.values.insert(0, value)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.values.pop(0)

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.values[0]

    def is_empty(self):
        return len(self.values) == 0

    def __len__(self):
        return len(self.values)
        
    def size(self):
        return len(self.values)

    def clear(self):
        self.values.clear()

    def __contains__(self, value):
        return value in self.values