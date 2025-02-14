class CustomList:
    def __init__(self, value=None):
        if value is None:
            self.values = []
        else:
            self.values = value

    def __contains__(self, value):
        return value in self.values

    def __len__(self):
        return len(self.values)

    def get(self, index):
        return self.values[index]

    def delete(self, index):
        del self.values[index]

    def insert(self, value, index = None):
        if index is None:
            self.values.append(value)
        else:
            # Add bounds checking
            if index > len(self.values) or index < -len(self.values) - 1:
                raise IndexError("list index out of range")
            self.values.insert(index, value)