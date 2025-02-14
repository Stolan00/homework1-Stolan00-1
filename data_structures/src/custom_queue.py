class CustomQueue:
    def __init__(self):
        self.values = []

    def enqueue(self, value):
        self.values.append(value)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.values.pop(0)

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self.values[0]

    def is_empty(self):
        return len(self.values) == 0

    def size(self):
        return len(self.values)

    def clear(self):
        self.values.clear()

    def __len__(self):
        return len(self.values)

    def __contains__(self, value):
        return value in self.values