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

    def rotate(self, count):
        for _ in range(count):
            item = self.dequeue()
            self.enqueue(item)

    def size(self):
        return len(self.queue)


def hot_potato(players, turns):
    queue = Queue()

    for player in players:
        queue.enqueue(player)

    while queue.size() > 1:
        for _ in range(turns):
            queue.rotate(1)

        eliminated_player = queue.dequeue()
        print(f"Gracz {eliminated_player} odpada z gry.")

    winner = queue.dequeue()
    print(f"Gracz {winner} wygrywa!")