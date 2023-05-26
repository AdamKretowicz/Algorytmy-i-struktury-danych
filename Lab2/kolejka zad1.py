class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Kolejka jest pusta")
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)


def perform_operations(operations):
    queue = Queue()
    results = []

    for op in operations:
        if op == 'q.isEmpty()':
            results.append(queue.is_empty())
        elif op.startswith('q.enqueue('):
            value = op.split('(')[1].split(')')[0]
            queue.enqueue(value)
        elif op == 'q.size()':
            results.append(queue.size())
        elif op == 'q.dequeue()':
            results.append(queue.dequeue())

    return results
