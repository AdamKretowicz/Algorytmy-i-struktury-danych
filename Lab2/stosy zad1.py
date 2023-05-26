class Stack:
    def __init__(self):
        self.stack = []

    def top(self):
        if self.is_empty():
            raise Exception("Stos jest pusty")
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if self.is_empty():
            raise Exception("Stos jest pusty")
        return self.stack.pop()