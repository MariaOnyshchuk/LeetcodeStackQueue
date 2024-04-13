class Queue:
    def __init__(self):
        self.start = self.end = None #front node = strat; last node = end

    def push(self, value):
        if value:
            node = Node(value)
            self.end.next = node
            self.start.next = self.end