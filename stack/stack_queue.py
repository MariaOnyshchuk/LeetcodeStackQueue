class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        # if self.value:
        #     self = self.push(value)

    def push(self, value):
        node = Node(value)
        if not self.top:
            self.top = node
        node.next = self.top
        self.top = node

    def pull(self):
        if self.top:
            node = self.top
            self.top = self.top.next
            node.next = None

class Queue:
    def __init__(self):
        self.start = self.end = None #front node = strat; last node = end

    def push(self, value):
        if value:
            node = Node(value)
            self.end.next = node
            self.start.next = self.end


class MyQueue:
    def __init__(self):
        

    def push(self, x: int) -> None:
        

    def pop(self) -> int:
        

    def peek(self) -> int:
        

    def empty(self) -> bool:
        
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()